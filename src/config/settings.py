from pydantic_settings import BaseSettings
from pydantic import BaseModel


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


config = Settings()