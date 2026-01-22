from abc import ABC, abstractmethod
from app.database.schemas.user import CreateUserInput

class IUserRepository(ABC):
    @abstractmethod
    async def get_by_email(self, email: str) -> CreateUserInput | None:
        pass
    @abstractmethod
    async def create(self, user: CreateUserInput):
        pass