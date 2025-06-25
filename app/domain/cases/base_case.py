from sqlalchemy.orm import Session

class BaseRequest:

    def __init__(self, db : Session = None):
        self.db = db
