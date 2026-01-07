from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str =  'a1bb637a08de62f26d379855dec2f43cab9288105605a7a749ccbb0e244df84aa559b4495569ca3027d4b3965922a635250a7661aaf6de7228df53ce9e6c1322'
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()

def get_settings() -> Settings:
    return Settings()