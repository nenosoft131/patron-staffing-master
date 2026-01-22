from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_async_db
from app.database.crud.user_crud import UserSQLAlchemyRepository
from app.infrastructure.security.password_hasher import BcryptPasswordHasher
from app.infrastructure.services.create_user import CreateUser
from app.interfaces.user_repository import IUserRepository
from app.interfaces.password_hasher import IPasswordHasher
from app.infrastructure.services.login_user import LoginUser
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwt_handler import decode_access_token

def get_user_repository(
    session: AsyncSession = Depends(get_async_db)
) -> IUserRepository:
    return UserSQLAlchemyRepository(session)

def get_password_hasher() -> IPasswordHasher:
    return BcryptPasswordHasher()

def get_create_user_use_case(
    repo: IUserRepository = Depends(get_user_repository),
    hasher: IPasswordHasher = Depends(get_password_hasher),
) -> CreateUser:
    return CreateUser(user_repo=repo, password_hasher=hasher)

def get_login_user_use_case(
    repo: IUserRepository = Depends(get_user_repository),
    hasher: IPasswordHasher = Depends(get_password_hasher)
) -> LoginUser:
    return LoginUser(user_repo=repo, password_hasher=hasher)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repo: IUserRepository = Depends(get_user_repository)
):
    try:
        payload = decode_access_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

    user = await user_repo.get_by_email(email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user