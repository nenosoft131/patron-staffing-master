from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_async_db
from app.api.repos.user_repository import UserSQLAlchemyRepository
from app.api.utils.create_user import CreateUser
from app.api.interfaces.user_repository import IUserRepository

def get_user_repository(
    session: AsyncSession = Depends(get_async_db)
) -> IUserRepository:
    return UserSQLAlchemyRepository(session)

def get_create_user_use_case(
    repo: IUserRepository = Depends(get_user_repository),
    # hasher: IPasswordHasher = Depends(get_password_hasher),
) -> CreateUser:
    # return CreateUser(user_repo=repo, password_hasher=hasher)
    return CreateUser(user_repo=repo)