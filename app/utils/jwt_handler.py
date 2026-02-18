# infrastructure/security/jwt_handler.py
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.core.config import get_settings

settings = get_settings()

def create_access_token(data: dict, expires_delta: int | None = None):
    
    to_encode = data.copy()
    expire_minutes = expires_delta if expires_delta is not None else settings.ACCESS_TOKEN_EXPIRE_MINUTES
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        J = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
