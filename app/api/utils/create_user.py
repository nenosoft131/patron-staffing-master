from app.models.user import User, UserRole
from app.api.interfaces.user_repository import IUserRepository
from app.api.interfaces.password_hasher import IPasswordHasher
from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateUserInput(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: UserRole = UserRole.candidate

class CreateUserOutput(BaseModel):
    id: int
    email: str
    role: UserRole

class CreateUser:
    def __init__(
        self,
        user_repo: IUserRepository,
        password_hasher: IPasswordHasher
    ):
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    async def execute(self, input: CreateUserInput) -> CreateUserOutput:
        # 🔍 Check uniqueness
        existing = await self.user_repo.get_by_email(input.email)
        if existing:
            raise ValueError("Email already registered")

        # 🔐 Hash password
        hashed = self.password_hasher.hash(input.password)
        # 🧠 Create domain entity
        domain_user = User(
            email=input.email,
            password_hash=hashed,
            first_name=input.first_name,
            last_name=input.last_name,
            role=input.role,
        )

        # 💾 Persist
        saved = await self.user_repo.create(domain_user)

        return CreateUserOutput(
            id=id(saved),  # or map ORM ID
            email=saved.email,
            role=saved.role
        )