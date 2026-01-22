from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.interfaces.user_repository import IUserRepository
from app.database.models.user_orm_model import UserORM  # SQLAlchemy model
from app.database.schemas.user import CreateUserInput
from app.database.models.user_orm_model import UserORM

class UserSQLAlchemyRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_by_email(self, email: str) -> CreateUserInput | None:
        stmt = select(UserORM).where(UserORM.email == email)
        result = await self.session.execute(stmt)
        orm_user = result.scalar_one_or_none()  # returns single UserORM or None
        return orm_user if orm_user else None
    

    async def create(self, user: CreateUserInput):
        orm_user = UserORM(
            email=user.email,
            hashed_password=user.password_hash,
            first_name=user.first_name,
            last_name=user.last_name,
            role=user.role,
            is_active=user.is_active,
        )
        self.session.add(orm_user)
        await self.session.commit()
        await self.session.refresh(orm_user)
        return orm_user
        # return self._to_domain(orm_user)

    # def _to_domain(self, orm: UserORM) -> DomainUser:
    #     return DomainUser(
    #         email=orm.email,
    #         password_hash=orm.hashed_password,
    #         first_name=orm.first_name,
    #         last_name=orm.last_name,
    #         role=orm.role,
    #         is_active=orm.is_active,
    #     )
