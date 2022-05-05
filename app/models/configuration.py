from sqlalchemy import Column, Integer,VARCHAR
from sqlalchemy.orm import relationship
from app.db import db

from flask import session


class Configuration(db.Model):
  """Es la tabla la cual define la configuracion del usuario """
  __tablename__ = "configurations"
  id = Column(Integer,primary_key=True)
  background = Column(VARCHAR(50))
  items_per_page = Column(Integer)


  def __init__ (self,background = None , items_per_page = None ):
      self.background = background
      self.items_per_page = items_per_page

  def __repr__(self):
    return (f"{self.background} {self.items_per_page}")


  @staticmethod
  def setItemsPerPage(value):
      items_per_page = value
      db.session.commit()


  @staticmethod
  def get_valid_paginations():
      return [5,10,15,20,25]

  @staticmethod
  def get_valid_colors():
    return ["Gris","Amarillo","Celeste"]

  @staticmethod
  def get_valid_user_columns():
    return ['username','last_name','first_name']

  @staticmethod
  def get_valid_sort_types():
    return ['asc','desc']

  @staticmethod
  def get_valid_issues_column():
    return ["email","created_at"]

  @staticmethod
  def get_valid_point_columns():
    return ["name", "email"]
