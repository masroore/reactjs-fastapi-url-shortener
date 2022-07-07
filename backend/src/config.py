from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    base_url: str
    dsn: str
    short_id_length: int
    secret_length: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def config() -> Settings:
    return Settings()
