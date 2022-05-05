from app.db import db
from app.models.category import Category
from app.models.status import Status
from datetime import datetime as dt

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Issue(db.Model):
    __tablename__ = "issues"
    id = Column(Integer,primary_key=True)
    email = Column(String(50), unique=True)
    description = Column(String(30),unique=True)
    #category_id = Column(String(30),unique =True)
    created_at = Column(String(50))

    category_id = Column(Integer,ForeignKey("categories.id"))
    category = relationship(Category)

    status_id = Column(Integer,ForeignKey("statuses.id"))
    status = relationship(Status)

    def __init__ (self,email = None, description = None, category_id = None, status_id = None):
        self.email = email
        self.description = description
        self.category_id = category_id
        self.status_id = status_id
        self.created_at = dt.now().strftime("%b %d %Y %H:%M:%S")
