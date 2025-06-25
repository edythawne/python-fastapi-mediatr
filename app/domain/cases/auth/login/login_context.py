from mediatr import Mediator
from sqlalchemy.orm import Session
from app.domain.cases.auth.login.login_request import LoginRequest
from app.domain.cases.base_case import BaseRequest
from app.domain.util.base_response import BaseResponse
from app.infrastructure.service.auth.login_service import LoginService

class LoginCommand(BaseRequest):

    def __init__(self, request: LoginRequest, db : Session) :
        super().__init__(db)
        self.request = request


@Mediator.handler
class LoginCommandHandler:
    service : LoginService

    def handle(self, request : LoginCommand) :
        self.service = LoginService(request.db)
        data = self.service.execute()
        print(data)
        return BaseResponse[LoginRequest](message = "Hello", data = request.request)

