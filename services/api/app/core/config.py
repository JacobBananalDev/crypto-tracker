"""
config.py

Centralized application configuration.

We use environment variables instead of hardcoding values.

This makes the application:
- Secure
- Portable
- Docker-friendly
- Production-ready
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings class automatically reads environment variables.

    If a variable is not found, it will use the default value.
    """

    # App metadata
    APP_NAME: str = "Crypto Tracker API"
    APP_VERSION: str = "1.0.0"

    # Environment
    ENVIRONMENT: str = "development"

    # Database (we will use this later)
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/crypto_db"

    class Config:
        # This allows us to use a .env file later
        env_file = ".env"


# Create a single settings instance to import everywhere
settings = Settings()