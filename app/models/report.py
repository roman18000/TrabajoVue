from app.db import db

from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime as dt
import json
from app.models.user import User


class Report_has_monitoring():
    table = db.Table(
        "report_has_monitoring",
        Column("report_id",Integer, ForeignKey("report.id")),
        Column("monitoring_id",Integer, ForeignKey("monitoring.id")),
        )
    @classmethod
    def get_table_report_has_monitoring(cls):
        return (cls.table)


class Report(db.Model):
    """ Crea el modelo de las denuncias con toda la informacion relacionada y el id de el usuario asignado """
    __tablename__ = "report"
    id = Column(Integer,primary_key=True)
    title = Column(String(50))
    status = Column(String(50))
    category = Column(String(50))
    creation_date = Column(String(30))
    closing_date = Column(String(30))
    description = Column(String(255))
    coordinates_latitude = Column(String(50),unique=True)  #Unico y si ya se elijo pedir otra
    coordinates_longitude = Column(String(50),unique=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    phone = Column(Integer)
    email = Column(String(30))

    user_assing_id = Column(Integer,ForeignKey("users.id"))
    user_assing = relationship(User)

    monitoring = relationship(
        "Monitoring",
        secondary = Report_has_monitoring.get_table_report_has_monitoring(),
        backref = db.backref("report",lazy = "dynamic"),
        lazy = "dynamic",
    )



    def __init__ (self,title,category, description, coordinates_latitude, coordinates_longitude,  first_name, last_name, phone, email,user_assing_id = None):
        self.title = title
        self.category = category
        self.creation_date = dt.now().strftime("%b %d %Y %H:%M:%S")
        self.closing_date = ""
        self.description = description
        self.coordinates_latitude = coordinates_latitude
        self.coordinates_longitude = coordinates_longitude
        self.user_assing_id = user_assing_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        if user_assing_id:
            self.status = "En Curso"
        else:
            self.status = "Sin confirmar"



    def get_values_json(self):
        return json.dumps([{
        "id":self.id,
        "title": self.title,
        "category": self.category,
        "creation_date": self.creation_date,
        "closing_date" : self.closing_date ,
        "description": self.description ,
        "coordinates_latitude": self.coordinates_latitude,
        "coordinates_longitude": self.coordinates_longitude ,
        "user_assing_name": self.user_assing.first_name ,
        "first_name": self.first_name,
        "last_name": self.last_name ,
        "phone": self.phone ,
        "email": self.email ,
        "status": self.status }])

    def get_lis_monitoring(self):
        lis_monitoring = []
        for monitoring in self.monitoring:
            lis_monitoring.append(monitoring)
        return lis_monitoring

class Monitoring(db.Model):
        __tablename__ = "monitoring"
        id = Column(Integer, primary_key=True)
        description = Column(String(255))
        creation_date = Column(String(30))
        author_id = Column(Integer,ForeignKey("users.id"))
        author = relationship(User)


        def __init__ (self,description = None, author_id = None ):
            self.description = description
            self.author_id = author_id
            self.creation_date = dt.now().strftime("%b %d %Y %H:%M:%S")
