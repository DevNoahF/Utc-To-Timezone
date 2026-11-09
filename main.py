from contextlib import asynccontextmanager

from fastapi import FastAPI

from controller.user_controller import router
from infrastructure.database.base import Base
from infrastructure.database.config import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        yield
    finally:
        await engine.dispose()


app = FastAPI(title="UTC to Timezone", lifespan=lifespan)
app.include_router(router)
