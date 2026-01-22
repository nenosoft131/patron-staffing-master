from app.interfaces.user_repository import IUserRepository
from app.infrastructure.security.password_hasher import IPasswordHasher
from app.database.schemas.user import CreateUserInput, UserOutput


class CreateUser:
    def __init__(self, user_repo: IUserRepository, password_hasher: IPasswordHasher):
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    async def execute(self, input: CreateUserInput) -> UserOutput:
        # 🔍 Check uniqueness
        existing = await self.user_repo.get_by_email(input.email)
        if existing:
            raise ValueError("Email already registered")
        # 🔐 Hash password
        hashed = self.password_hasher.hash(input.password_hash)
        # 🧠 Create domain entity
        domain_user = CreateUserInput(
            email=input.email,
            password_hash=hashed,
            first_name=input.first_name,
            last_name=input.last_name,
            role=input.role,
            is_active=input.is_active
        )

        # 💾 Persist
        saved = await self.user_repo.create(domain_user)

        return UserOutput(
            id=id(saved),  # or map ORM ID
            email=saved.email,
            first_name=saved.first_name,
            last_name= saved.last_name,
            role=saved.role,
            is_active=saved.is_active
        )