from fastapi import FastAPI
from api.routers import router as api_router
from infrastructure.database.session import engine
from domain.models.base import Base
from contextlib import asynccontextmanager
from config.settings import config
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Data Table is Create")
    yield 
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print("Data Table is drop")


app = FastAPI(
    lifespan=lifespan
)
app.include_router(api_router, prefix="/api")

if __name__=="__main__":
    uvicorn.run(
        app="main:app",
        host=config.run.host,
        port=config.run.port,
        reload=config.run.auto_reload
    )