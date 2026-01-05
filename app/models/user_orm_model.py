# adapters/database/models/user.py
from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from app.models.user import UserRole  # reuse domain enum!

Base = declarative_base()

class UserORM(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)  # ← note: "hashed_password", not "password_hash"
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.candidate)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Optional: helper to convert to DomainUser
    def to_domain(self) -> "DomainUser":
        from app.domain.models.user import DomainUser  # avoid circular import
        return DomainUser(
            email=self.email,
            password_hash=self.hashed_password,  # map DB field → domain field
            first_name=self.first_name,
            last_name=self.last_name,
            role=self.role,
            is_active=self.is_active,
        )