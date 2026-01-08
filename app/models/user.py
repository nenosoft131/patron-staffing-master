# app/domain/models/user.py
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    admin = "admin"
    client = "client"      # e.g., hiring company
    candidate = "candidate"  # job seeker
    staff = "staff"        # internal agent

@dataclass(frozen=True)  # immutable: safe for domain logic
class User:
    email: str
    password_hash: Optional[str] = str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: UserRole = UserRole.candidate
    is_active: bool = True