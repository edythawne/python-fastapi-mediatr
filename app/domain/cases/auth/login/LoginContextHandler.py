from mediatr import Mediator, GenericQuery

from app.domain.cases.auth.login.LoginRequest import LoginRequest
from app.domain.util.BaseResponse import BaseResponse
from app.infrastructure.service.auth.login_service import LoginService

class LoginCommand(GenericQuery[LoginRequest]):

    def __init__(self, request: LoginRequest) :
        self.request = request


@Mediator.handler
class LoginCommandHandler:
    service : LoginService = LoginService()

    def handle(self, request : LoginCommand) :
        print("Constructor de LoginCommandHandler")
        self.service.execute()
        return BaseResponse[LoginRequest](message = "Hello", data = request.request)

