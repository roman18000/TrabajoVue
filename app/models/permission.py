from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.configuration import Configuration
import datetime as dt

from app.db import db
from sqlalchemy.orm import relationship

class Role_has_permission():
    table = db.Table(
        "role_has_permission",
        Column("role_id",Integer, ForeignKey("roles.id")),
        Column("permission_id",Integer, ForeignKey("permissions.id")),
        )

    @classmethod
    def get_table_role_has_role(cls):
        return (cls.table)

class Role(db.Model):
        __tablename__ = "roles"
        id = Column(Integer, primary_key=True)
        name = Column(String(255), unique= True)

        permission = relationship(
            "Permission",
            secondary = Role_has_permission.get_table_role_has_role(),
            backref = db.backref("roles",lazy = "dynamic"),
            lazy = "dynamic",
        )
        
        def __init__ (self,name = None ):
            self.name = name;

        def __repr__(self):
            return self.name

class User_has_role():
    table = db.Table(
        "user_has_role",
        Column("user_id",Integer, ForeignKey("users.id")),
        Column("role_id",Integer, ForeignKey("roles.id")),
        )

    @classmethod
    def get_table_user_has_role(cls):
        return (cls.table)



class Permission(db.Model):
        __tablename__ = "permissions"
        id = Column(Integer, primary_key=True)
        name = Column(String(255), unique= True)

        def __init__ (self,name = None ):
            self.name = name;
