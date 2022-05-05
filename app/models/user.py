# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.configuration import Configuration
from datetime import datetime as dt

from app.db import db
from sqlalchemy.orm import relationship

from app.models.permission import Role , User_has_role

class User(db.Model):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        email = Column(String(50), unique=True)
        username = Column (String (50),unique=True)
        password = Column(String(50))
        first_name = Column(String(50))
        last_name = Column(String(50))
        active = Column(Boolean)
        created_at = Column(String(30))

        configuration_id = Column(Integer,ForeignKey("configurations.id"))
        configuration = relationship(Configuration)

        role = db.relationship(
            "Role",
            secondary = User_has_role.get_table_user_has_role(),
            backref= db.backref("roles_user", lazy="dynamic"),
            lazy = "dynamic",
            )   

        def __init__ (self,first_name = None , last_name = None, email = None, user = None, password = None,active = True):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.username = user
            self.password = password
            self.configuration_id = 1
            self.active = active
            self.created_at = dt.now().strftime("%b %d %Y %H:%M:%S")


        def __repr__(self):
            return (f"{self.first_name} {self.last_name} email: {self.email}")
