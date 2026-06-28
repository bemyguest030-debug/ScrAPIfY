"""
Configuration globale de ScrAPIfY
"""
import os
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Paramètres de configuration principal de l'application"""

    # ===== Application =====
    APP_NAME: str = "ScrAPIfY"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # ===== API =====
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    API_KEY: Optional[str] = os.getenv("API_KEY")

    # ===== Database =====
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./scrapify.db"
    )
    DB_ECHO: bool = False

    # ===== Redis =====
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # ===== Security =====
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24

    # ===== Scraping =====
    MAX_WORKERS: int = int(os.getenv("MAX_WORKERS", "5"))
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "10"))
    USER_AGENT: str = os.getenv(
        "USER_AGENT",
        "ScrAPIfY/1.0 (Product Positioning & Market Research Tool)"
    )
    RESPECT_ROBOTS_TXT: bool = os.getenv("RESPECT_ROBOTS_TXT", "true").lower() == "true"

    # ===== NLP =====
    SENTIMENT_MODEL: str = "textblob"
    LANGUAGE: str = "en"

    # ===== Logging =====
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = "logs/scrapify.log"

    # ===== Proxy =====
    USE_PROXY: bool = os.getenv("USE_PROXY", "false").lower() == "true"
    PROXY_LIST: list = os.getenv("PROXY_LIST", "").split(",") if os.getenv("PROXY_LIST") else []

    # ===== Browser Automation =====
    SELENIUM_DRIVER: str = "chrome"
    HEADLESS_BROWSER: bool = os.getenv("HEADLESS_BROWSER", "true").lower() == "true"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Récupère les paramètres de configuration (cachés)"""
    return Settings()


# Instance globale
settings = get_settings()