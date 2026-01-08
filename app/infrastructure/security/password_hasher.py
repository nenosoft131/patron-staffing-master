# adapters/auth/bcrypt_password_hasher.py
import bcrypt
from typing import Final
from app.interfaces.password_hasher import IPasswordHasher

# Security: bcrypt work factor (12 is standard; 10–14 recommended)
BCRYPT_ROUNDS: Final[int] = 12


class BcryptPasswordHasher(IPasswordHasher):
   
    def hash(self, password: str) -> str:
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        if len(password) > 1024:
            raise ValueError("Password too long (>1024 chars)")

        pwd_bytes = password.encode("utf-8")
        
        # Hash with salt
        salt = bcrypt.gensalt(rounds=BCRYPT_ROUNDS)
        hashed = bcrypt.hashpw(pwd_bytes, salt)
        
        return hashed.decode("utf-8")

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
            return False

        try:
            plain_bytes = plain_password.encode("utf-8")
            hash_bytes = hashed_password.encode("utf-8")
            
            return bcrypt.checkpw(plain_bytes, hash_bytes)
        except (ValueError, TypeError):
            return False