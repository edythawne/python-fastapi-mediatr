from fastapi import APIRouter, Depends
from app.application.application import BaseController, init_controller
from app.domain.cases.auth.login.LoginContextHandler import LoginCommand
from app.domain.cases.auth.login.LoginRequest import LoginRequest

def authentication_router() -> APIRouter:
    router = APIRouter()

    @router.post("/login")
    async def login(request: LoginRequest, controller: BaseController = Depends(init_controller)):
        print("Constructor de login")
        return await controller.execute(LoginCommand(request))

    return router


