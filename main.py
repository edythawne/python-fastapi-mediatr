from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.application.api_router import ApiRouter
from app.infrastructure.database_context import db_connection, SessionLocal
from typing import AsyncIterator


async def configure_service(app: FastAPI) -> AsyncIterator[None]:
    db_connection()
    yield


def create_app(api_prefix = "/api/v1") -> FastAPI :
    app = FastAPI(title="SEMOV Backend", version="1.0.0", lifespan = configure_service)

    db = SessionLocal()
    api_router = ApiRouter(db = db)

    # Routers
    app.include_router(api_router.get_routers(), prefix = api_prefix)

    # Agregar estaticos
    app.mount("/public", StaticFiles(directory="public"), name="public")

    return app


app = create_app()

