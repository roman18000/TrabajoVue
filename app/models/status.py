from sqlalchemy import Column, Integer, String
from app.db import db

class Status(db.Model):
    """Define la entidad de tipo status que se corresponde con la tabla statuses"""

    __tablename__ = "statuses"
    id = Column(Integer,primary_key=True)
    name = Column (String(30),unique=True)

    def __init__ (self, name = None):
        self.name = name
