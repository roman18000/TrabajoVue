from sqlalchemy.orm import relationship
from sqlalchemy import Column,  String,ForeignKey
from sqlalchemy.sql.sqltypes import VARCHAR
from app.db import db


class View(db.Model):
    "Contiene la columna por la que se ordena el listado del as vistas y el tipo de orden (ASC,DESC)"
    __tablename__ = "view"
    id = Column(String,primary_key=True)
    sorted_by_column = Column(VARCHAR(30))
    sort_type = Column(VARCHAR(30))

    def __init__(self,id = None, column = None , type = None):
        self.id = id
        self.sorted_by_column = column
        self.sort_type = type

    def __repr__():
        return (f"{self.sorted_by_column} {self.sort_type}")

    def formatted_values(self):
        return { "column" : self.sorted_by_column,
                 "type" : self.sort_type }
