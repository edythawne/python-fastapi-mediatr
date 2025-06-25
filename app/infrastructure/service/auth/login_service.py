from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.infrastructure.database_context import db_connection
from app.infrastructure.service.base_service import BaseService


class LoginService(BaseService):

    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self):
        data = self.session.execute(text("SELECT * FROM client.user"))
        return data.fetchall()