from flask import request
from app.models.flood_zone import FloodZone
from app.db import db
from app.scheme.flood_zone import FloodZoneScheme

class FloodZoneDao():


    @staticmethod
    def search_object_by_id(id):
        return  FloodZone.query.filter_by(id=id).first()

    @staticmethod
    def filter_by_key(status,items_per_page, key=""):
        key_filtered = "%" + key + "%"
        page = request.args.get('page', 1, type=int)
        if status == "Todos":
            zones =  FloodZone.query.filter(FloodZone.name.like(key_filtered)).paginate(page=page, per_page=items_per_page)
        else:
            if status == "Publicado":
                zones =  FloodZone.query.filter(FloodZone.name.like(key_filtered)).filter_by(state = True).paginate(page=page, per_page=items_per_page)
            else:
                zones =  FloodZone.query.filter(FloodZone.name.like(key_filtered)).filter_by(state = False).paginate(page=page, per_page=items_per_page)
        return zones

    @staticmethod
    def recover_flood_zones():
         return FloodZone.query.all()

    @staticmethod
    def recover_flood_zones_paginated(page,per_page):
        return FloodZone.query.paginate(page = page, per_page = per_page)

    @staticmethod
    def recover_flood_zone(id):
        return FloodZone.query.filter_by(id=id).first()

    @staticmethod
    def name_exists(floodzone_name):
        return bool(FloodZone.query.filter_by(name=floodzone_name).first())

    @staticmethod
    def delete(flood_zone_delete):
        db.session.delete(flood_zone_delete)
        try:
            db.session.commit()
            return True
        except:
            return False
    
    @staticmethod
    def recover_coordinates_by_id(id):
        return FloodZone.query.filter_by(id=id).first().get_as_json()

    @staticmethod
    def recover_coordinates_by_id(id):
        return FloodZone.query.filter_by(id=id).first().get_as_json()

    @classmethod
    def publicate_despublicate(cls,flood_zone_id):
        flood_zone = cls.search_object_by_id(flood_zone_id)
        flood_zone.state = not (flood_zone.state)
        try:
            db.session.commit()
            return True
        except:
            return False


