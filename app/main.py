from fastapi import FastAPI
from app.db import session_manager
from app.settings import DB_CONFIG
from contextlib import asynccontextmanager


def create_app(init_db: bool = True):
    if init_db:
        session_manager.init(DB_CONFIG)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            if session_manager._engine is None:
                await session_manager.close()

    app = FastAPI(lifespan=lifespan)

    return app


app = create_app()
