from pydantic_settings import BaseSettings
import os
import logging

class Settings(BaseSettings):
    JWT_SECRET: str
    DATABASE_URL: str = "sqlite:///./app.db"
    DEBUG: bool = True
    TOKEN_EXPIRE_HOURS: int = 12
    
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    VITE_API_URL: str
    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    S3_ENDPOINT: str = "http://minio:9000"
    S3_REGION: str = "us-east-1"
    
    class Config:
        env_file = f".env.{os.getenv('ENV', 'dev')}"
        env_file_encoding = "utf-8"

settings = Settings()

# Логгер
logger = logging.getLogger("config")
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

logger.info(
    f"[CONFIG] ENV: {os.getenv('ENV', 'dev')} | DEBUG: {settings.DEBUG} | DB: {settings.DATABASE_URL} | TOKEN_EXP: {settings.TOKEN_EXPIRE_HOURS}h"
)
