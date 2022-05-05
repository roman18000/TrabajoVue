from flask import request
from app.models.point import Point
from app.db import db
from app.models.views_sort import View




class PointDAO():
    def points_paginated(items_per_page):
        page = request.args.get('page', 1, type=int)
        # points = Point.query.order_by(Point.email.desc())
        view_dict = View.query.filter_by(id = "point").first().formatted_values()
        points = eval("Point.query.order_by(Point.{}.{}())".format(view_dict["column"], view_dict["type"]))
        points = points.paginate(page=page, per_page=items_per_page)
        return points

    @staticmethod
    def filter_by_key(status,items_per_page, key=""):
        key_filtered = "%" + key + "%"
        page = request.args.get('page', 1, type=int)
        if status == "Todos":
            points =  Point.query.filter(Point.name.like(key_filtered)).paginate(page=page, per_page=items_per_page)
        else:
            points =  Point.query.filter(Point.name.like(key_filtered)).filter_by(status = status).paginate(page=page, per_page=items_per_page)
        return points


    @staticmethod
    def recover_points():
         return Point.query.all()

    @staticmethod
    def exist_name(name):
        return bool((Point.query.filter_by(name=name).first()))

    @staticmethod
    def exist_adress(address):
        return bool((Point.query.filter_by(address=address).first()))


    @staticmethod
    def create_user(name, address, coordinates_lat,coordinates_long, phone, email, status):
        new_point = Point(name,address,coordinates_lat,coordinates_long,phone,email,status)
        db.session.add(new_point)
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def search_by_id(point_id):
        return Point.query.filter_by(id=point_id).first()

    @staticmethod
    def update(point_update,name, address, coordinates_lat,coordinates_long, phone, email, status):
        if name:
            point_update.name = name
        if address:
            point_update.address = address
        if coordinates_lat:
            point_update.coodinates_latitude = coordinates_lat
        if coordinates_long:
            point_update.coodinates_longitude = coordinates_long
        if status:
            point_update.status = status
        if phone:
            point_update.phone = phone
        if email:
            point_update.email = email
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def delete(point_delete):
        db.session.delete(point_delete)
        try:
            db.session.commit()
            return True
        except:
            return False


    @staticmethod
    def recover_points_paginated(page,per_page):
        return Point.query.paginate(page = page, per_page = per_page)
