from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from app.models.configuration import Configuration
from app.db import db


class Coordinate(db.Model):
        __tablename__ = "coordinates"
        id = Column(Integer, primary_key=True)
        latitude = Column(Float)
        longitude = Column(Float)

        def __init__ (self,latitude = None, longitude = None ):
            self.latitude = latitude
            self.longitude = longitude


class Route_of_evacuation_has_coordinate():
    table = db.Table(
        "route_of_evacuation_has_coordinate",
        Column("route_of_evacuation_id",Integer, ForeignKey("route_of_evacuation.id", ondelete="CASCADE")),
        Column("coordinate_id",Integer, ForeignKey("coordinates.id", ondelete="CASCADE")),
    )

    @classmethod
    def get_table_route_of_evacuation_has_coordinate(cls):
        return (cls.table)


class FloodZone_has_coordinate():
    table = db.Table(
        "floodZone_has_coordinate",
        Column("floodZone_id",Integer, ForeignKey("flood_zones.id", ondelete="CASCADE")),
        Column("coordinate_id",Integer, ForeignKey("coordinates.id", ondelete="CASCADE")),
        )

    @classmethod
    def get_table_floodZone_has_coordinate(cls):
        return (cls.table)

    # def __init__(self, flood_zone_id = None, coordinate_id = None):
    #     self.floodZone_id = flood_zone_id
    #     self.coordinate_id = coordinate_id

    @classmethod
    def get_points_sorted(cls):
       return cls.query.order_by(cls.coordinates_id).all()
    

    