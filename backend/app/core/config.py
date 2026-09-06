from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "CineAI Studio"
    API_V1_STR: str = "/api/v1"
    
    # Environment variables
    ENVIRONMENT: str = "development"
    
    # These will be populated in Phase 2
    DATABASE_URL: Optional[str] = None
    
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")

settings = Settings()
