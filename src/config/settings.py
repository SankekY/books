from pydantic_settings import BaseSettings
from pydantic import BaseModel


class JWTConfig(BaseModel):
    algorithm: str = "HS256"
    secret_key: str = "gV64m9aIzFG4qpgVphvQbPQrtAO0nM-7YwwOvu0XPt5KJOjAy4AfgLkqJXYEt"
    expire_day: int = 30

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    auto_reload: bool = True


class DBConfig(BaseModel):
    url: str = "sqlite+aiosqlite:///database.db"
    echo: bool = True
    max_overflow: int = 10

class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    run: RunConfig = RunConfig()
    jwt: JWTConfig = JWTConfig()


config = Settings()