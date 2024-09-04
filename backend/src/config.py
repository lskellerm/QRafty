"""Global Settings module for the application."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi_users.jwt import SecretType
from typing import Optional


class Settings(BaseSettings):
    DEV_DATABASE_URL: Optional[str] = None
    TEST_DATABASE_URL: str
    SECRET_KEY: SecretType
    ENVIRONMENT: str
    SHOW_DOCS_ENVIRONMENTS: tuple[str, str, str] = ("development", "staging", "testing")
    APP_NAME: str = "QRafty API"
    ALLOWED_ORIGINS: Optional[str] = None
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
