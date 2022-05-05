from sqlalchemy import Column, Integer, String
from app.db import db

class Category(db.Model):
  """define una entidad de tipo category que se corresponde con la tabla categories"""
  __tablename__ = "categories"
  id = Column(Integer,primary_key=True)
  name = Column (String(30),unique=True)

  def __init__ (self, name = None):
    self.name = name
