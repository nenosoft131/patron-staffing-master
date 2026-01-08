
from pydantic import BaseModel, EmailStr
from typing import Optional
from app.domain.models.user import UserRole

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
