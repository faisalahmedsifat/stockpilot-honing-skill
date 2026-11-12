from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "StockPilot"
    app_env: Literal["development", "testing", "production"] = "development"

    debug: bool = False

    api_v1_prefix: str = "/api/v1"

    database_url: str = (
        "postgresql+asyncpg://stockpilot:stockpilot@localhost:5444/stockpilot"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
