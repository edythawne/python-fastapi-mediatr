from mediatr import Mediator
from fastapi import Depends

def init_mediator():
    return Mediator()

def init_controller(mediator : Mediator = Depends(init_mediator)):
    return BaseController(mediator)

class BaseController:

    def __init__(self, mediator : Mediator):
        self.mediator = mediator

    async def execute(self, handler):
        return await self.mediator.send_async(handler)

