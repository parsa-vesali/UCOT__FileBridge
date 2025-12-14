# config/env_settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from typing import Union

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"  
    )

    # Django settings
    SECRET_KEY: str
    DEBUG: bool = False
    ALLOWED_HOSTS: Union[list[str], str] = "127.0.0.1,localhost"
    
    # Database
    DATABASE_URL: str = "sqlite:///db.sqlite3"
    
    # Minio (optional)
    MINIO_ROOT_USER: str | None = None
    MINIO_ROOT_PASSWORD: str | None = None
    MINIO_ENDPOINT: str | None = None
    MINIO_BUCKET: str | None = None
    
    API_HOST_PORT: int = 8000

    @field_validator("SECRET_KEY")
    @classmethod
    def validate_secret_key(cls, value):
        if not value or not value.strip():
            raise ValueError(
                "SECRET_KEY is required and cannot be empty."
            )
        return value

    @field_validator("ALLOWED_HOSTS", mode="before")
    @classmethod
    def parse_allowed_hosts(cls, value):
        if isinstance(value, str):
            return [host.strip() for host in value.split(",") if host.strip()]
        return value

settings = Settings()

#  ALLOWED_HOSTS 
if isinstance(settings.ALLOWED_HOSTS, str):
    settings.ALLOWED_HOSTS = [
        host.strip() 
        for host in settings.ALLOWED_HOSTS.split(",") 
        if host.strip()
    ]