from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.database_context import db_connection


class LoginService:
    db_context: Session

    def __init__(self, context: Session = Depends(db_connection)):
        print("Constructor de LoginService")
        self.db_context = context

    def execute(self):
        print(self.db_context.execute("SELECT 1"))
        print("LoginService : execute")