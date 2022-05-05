# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.configuration import Configuration
from app.models.coordinate import Route_of_evacuation_has_coordinate

from app.db import db
from sqlalchemy.orm import relationship


class Route_of_evacuation(db.Model):
    __tablename__ = "route_of_evacuation"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(50))
    publicado = Column(Boolean)

    coordinates = db.relationship(
            "Coordinate",
            secondary = Route_of_evacuation_has_coordinate.get_table_route_of_evacuation_has_coordinate(),
            backref= db.backref("coordinates_route_of_evacuation", lazy="dynamic"),
            lazy = "dynamic",
        )

    def __init__(self, nombre=None, estado=None,coordinates=None, descripcion=None):
        self.name = nombre
        self.description = descripcion
        self.publicado = estado
        self._agregar_coordinates(coordinates)

    def _agregar_coordinates(self,coordinates):
        for coordinate_lat_long in coordinates:
            #print (f"coordenadas         {coordinate_lat_long.id} {coordinate_lat_long.latitude}           {coordinate_lat_long.longitude}")
            self.coordinates.append(coordinate_lat_long)



    def __repr__(self):
        return (self.name)
