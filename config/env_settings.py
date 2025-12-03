# config/env_settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"  
    )

    # Django settings
    SECRET_KEY: str  
    DEBUG: bool = False
    ALLOWED_HOSTS: list[str] = ["127.0.0.1", "localhost"]
    
    # Database
    DATABASE_URL: str  
    
    # Minio (optional)
    MINIO_ROOT_USER: str | None = None
    MINIO_ROOT_PASSWORD: str | None = None
    MINIO_ENDPOINT: str | None = None
    MINIO_BUCKET: str | None = None
    
    API_HOST_PORT: int = 8000

settings = Settings()