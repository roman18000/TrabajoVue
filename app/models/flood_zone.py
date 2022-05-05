from sqlalchemy import Column, Integer, String, Boolean
from app.db import db
from app.models.coordinate import Coordinate , FloodZone_has_coordinate
import random
import json

class FloodZone(db.Model):
  """Define el modelo de la tabla zonas_inundables"""
  __tablename__ = "flood_zones"
  id = Column(Integer,primary_key=True)
  cod_zone = Column (String(50))
  name = Column(String(50), unique=True)
  state = Column(Boolean)
  colour = Column(String(50))

  coordinates = db.relationship(
            "Coordinate",
            secondary = FloodZone_has_coordinate.get_table_floodZone_has_coordinate(),
            backref= db.backref("coordinates_floodZone", lazy="dynamic"),
            lazy = "dynamic",
        )

  # por defectos se cargan con estos valores por el tema de que en el csv solo viene nombre y coordenadas
  def __init__ (self, name = None, cod_zone = "Codigo default", state = True, color = "Rojo"):
      self.name = name
      self.cod_zone = cod_zone
      self.state = state
      self.colour = color

  def get_ordered_coords(self):
      coords = self.coordinates.all()
      coords_sort = coords.sort(key=lambda obj: obj.id)
      print(coords_sort)


  def get_as_json(self):
      coords = self.coordinates.all()
      coords.sort(key=lambda x: x.id)
      arr = []
      for coor in coords:
          arr.append([coor.latitude, coor.longitude])
      return arr

  def get_color_traduced(self):
       dic = { "Rojo" : "red",
                "Violeta" : "violet",
                "Amarillo": "yellow",
                "Azul": "blue",
                "Verde": "green"
                }
       return dic[self.colour]

  
  
