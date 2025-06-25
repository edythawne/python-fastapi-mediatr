from abc import abstractmethod

from sqlalchemy.orm import Session

class BaseService:

    def __init__(self, session : Session):
        self.session = session

    @abstractmethod
    def execute(self):
        pass