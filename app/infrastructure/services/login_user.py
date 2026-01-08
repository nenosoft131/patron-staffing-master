# app/utils/login_user.py
from app.interfaces.user_repository import IUserRepository
from app.interfaces.password_hasher import IPasswordHasher
from app.api.schemas.auth import LoginInput, LoginOutput
from app.utils.jwt_handler import create_access_token
from fastapi import HTTPException, status

class LoginUser:
    def __init__(self, user_repo: IUserRepository, password_hasher: IPasswordHasher):
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    async def execute(self, input: LoginInput) -> LoginOutput:
        user = await self.user_repo.get_by_email(input.email)
        if not user or not self.password_hasher.verify(input.password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        token_data = {"sub": user.email, "role": user.role}
        access_token = create_access_token(token_data)
        return LoginOutput(access_token=access_token)
