"""Global Settings module for the application."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from Typing import Optional


class Settings(BaseSettings):
    DEV_DATABASE_URL: Optional[str] = None
    TEST_DATABASE_URL: str
    SECRET_KEY: Optional[str] = None
    ENVIRONMENT: str
    SHOW_DOCS_ENVIRONMENTS: tuple[str, str, str] = ("development", "staging", "testing")
    app_name: str = "QRafty API"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
