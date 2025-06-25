from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.application.application import BaseController, init_controller
from app.domain.cases.auth.login.login_context import LoginCommand
from app.domain.cases.auth.login.login_request import LoginRequest

def authentication_router(db : Session) -> APIRouter:
    router = APIRouter()

    @router.post("/login")
    async def login(request: LoginRequest, controller: BaseController = Depends(init_controller)):
        return await controller.execute(LoginCommand(request, db))

    return router


