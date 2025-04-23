from pydantic_settings import BaseSettings
import os
import logging
from pydantic import PostgresDsn


class Settings(BaseSettings):
    # === App ===
    APP_SECRET_KEY: str
    DEBUG: bool = True
    TOKEN_EXPIRE_HOURS: int = 12

    # === Database ===
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    # DATABASE_URL: str = "sqlite:///./app.db"  # fallback, если PostgreSQL не используется

    @property
    def postgres_url(self) -> PostgresDsn:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"  # type: ignore

    # === Frontend API URL ===
    VITE_API_BASE_URL: str

    # === MinIO / S3 ===
    # S3_ENDPOINT_URL: str = "http://minio:9000"
    # S3_ACCESS_KEY: str
    # S3_SECRET_KEY: str
    # S3_REGION: str = "us-east-1"
    # S3_BUCKET_NAME: str = "files"

    class Config:
        env_file = f".env.{os.getenv('ENV', 'dev')}"
        env_file_encoding = "utf-8"


settings = Settings()

# Логгер
logger = logging.getLogger("config")
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# logger.info(
#     f"[CONFIG] ENV: {os.getenv('ENV', 'dev')} | DEBUG: {settings.DEBUG} | DB: {settings.DATABASE_URL} | TOKEN_EXP: {settings.TOKEN_EXPIRE_HOURS}h"
# )
