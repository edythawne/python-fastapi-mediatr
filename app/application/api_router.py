from fastapi import APIRouter
from app.application.auth.authentication import authentication_router

class ApiRouter:

    def __init__(self, db):
        self.db = db

    def get_routers(self) -> APIRouter:
        router = APIRouter()
        router.include_router(authentication_router(), prefix="/authentication", tags=["authentication"])
        return router