from flask import request
from app.models.route_of_evacuation import Route_of_evacuation as Route
from app.db import db
from sqlalchemy import or_
from app.models.coordinate import Coordinate

class Route_of_evacuationDAO ():

    @staticmethod
    def recover_route_of_evacuation():
         return Route.query.all()

    @staticmethod
    def filter_by_key(status,items_per_page, key=""):
        key_filtered = "%" + key + "%"
        page = request.args.get('page', 1, type=int)
        if status == "Todos":
            routes =  Route.query.filter(Route.name.like(key_filtered)).paginate(page=page, per_page=items_per_page)
        else:
            if status == "Publicado":
                routes =  Route.query.filter(Route.name.like(key_filtered)).filter_by(publicado = True).paginate(page=page, per_page=items_per_page)
            else:
                routes =  Route.query.filter(Route.name.like(key_filtered)).filter_by(publicado = False).paginate(page=page, per_page=items_per_page)
        return routes


    @staticmethod
    def _parse_coordinates(coordinates):
        parse_coordinate = coordinates.split(",")
        print (parse_coordinate)
        ambas_coordinate = False
        list_lat_long = []
        for c in parse_coordinate:
            if ambas_coordinate:
                print (lat,c)
                list_lat_long.append(Coordinate(lat,c))
                ambas_coordinate = False
            else:
                ambas_coordinate = True
                lat = c
        return list_lat_long



    @classmethod
    def create_route(cls,name,publicado,coordinate,description):
        list_general_lat_long = cls._parse_coordinates(coordinate)
        new_route = Route(name,publicado,list_general_lat_long,description)
        db.session.add(new_route)
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def search_by_id(route_id):
        return  Route.query.filter_by(id = route_id).first()

    @staticmethod
    def delete(route_delete):
        db.session.delete(route_delete)
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def update(route,name,publicado,coordinates,description):
        #Como agregarle una nueva coordenada... limpiando la otra relationship
        if name:
            route.name = name
        if publicado:
            route.publicado = True
        else:
            route.publicado = False
        if description:
            route.description = description

        try:
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def publicate_despublicate(cls,route_id):
        route = cls.search_by_id(route_id)
        route.publicado = not (route.publicado)
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def recover_route_of_evacuation_paginated(page,per_page):
        return Route.query.paginate(page = page, per_page = per_page)
