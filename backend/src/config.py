"""Global Settings module for the application."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEV_DATABASE_URL: str
    TEST_DATABASE_URL: str
    SECRET_KEY: str
    app_name: str = "QRafty API"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
