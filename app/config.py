from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    MAX_CONCURRENT_JOBS: int = Field(default=4, ge=1)
    LLM_MAX_CALLS: int = Field(default=10, ge=1)
    LLM_TIMEOUT: int = Field(default=60, ge=1)
    STORAGE_PATH: Path = Path("storage")
    CACHE_DIR: Path = Path(".cache")
    EXTRACTOR_VERSION: str = "v1"
