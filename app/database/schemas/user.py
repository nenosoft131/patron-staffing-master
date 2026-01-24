from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from pydantic import ConfigDict


class UserRole(str, Enum):
    admin = "admin"
    client = "client"      # e.g., hiring company HR
    candidate = "candidate"  # job seeker
    staff = "staff"        # internal staffing agent

class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: UserRole = UserRole.candidate
    is_active: bool


class CreateUserInput(UserBase):
    password_hash: str


class UserOutput(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
