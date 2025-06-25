from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.application.auth.authentication import authentication_router

class ApiRouter:

    def __init__(self, db : Session):
        self.db = db

    def get_routers(self) -> APIRouter:
        router = APIRouter()
        router.include_router(authentication_router(self.db), prefix="/authentication", tags=["authentication"])
        return router