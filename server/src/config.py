from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    base_url: str = "http://localhost:9000/"
    dsn: str = "sqlite:///./shorty.db"
    short_id_length: int = 5
    secret_length: int = 8

    class Config:
        env_file = "../.env"


@lru_cache
def config() -> Settings:
    return Settings()
