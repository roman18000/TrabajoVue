from app.models.user import User
from app.db import db
from app.models.report import Report,Monitoring
from flask import request,session
from datetime import datetime as dt
from sqlalchemy import or_, and_
import logging
class ReportDAO():
    """Genera las consultas necesarios para consultar la informacion del denuncias en la base de datos en el resource"""

    @staticmethod
    def create_report(title,category, description, coordinates_latitude, coordinates_longitude,  first_name, last_name, phone, email,user_assing_id = None):
        new_report = Report(title,category, description, coordinates_latitude, coordinates_longitude, first_name, last_name, phone, email,user_assing_id)

        db.session.add(new_report)
    # try:
        
        db.session.commit()
        print("---"*50)
        # return True
    # except:
    #     return False


    @staticmethod
    def recover_reports_paginated(page,per_page):
        return Report.query.paginate(page = page, per_page = per_page)

    @classmethod
    def create_report_dict(cls,report_dic):
        lis = report_dic["coordinates"].split(",")
        coordinates_latitude = lis[0]
        coordinates_longitude = lis[1]
        return  cls.create_report(report_dic["title"],report_dic["category"], report_dic["description"], coordinates_latitude, coordinates_longitude,  report_dic["first_name"], report_dic["last_name"], report_dic["phone"], report_dic["email"])


    @staticmethod
    def existe_coordinates(coordinates = None , coordinates_latitude = None , coordinates_longitude = None):
        if coordinates:
            lis = coordinates.split(",")
            coordinates_latitude = lis[0]
            coordinates_longitude = lis[1]
        if (db.session.query(Report).filter(or_(Report.coordinates_latitude == coordinates_latitude, Report.coordinates_longitude == coordinates_longitude)).first()):
                return True
        return False



    @staticmethod
    def search_by_id(report_id):
        return  Report.query.filter_by(id=report_id).first()


    @classmethod
    def delete_by_id(cls,report_id):
        report_delete = cls.search_by_id(report_id)
        try:
            db.session.delete(report_delete) #Puedo consultar si esto se rompe es porque no existe el usuario
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def update_report(cls,update_report,title,category, description, coordinates_latitude, coordinates_longitude,  first_name, last_name, phone, email,usser_id):
        report_update_parameter = cls._update_report(update_report,title,category, description, coordinates_latitude, coordinates_longitude,  first_name, last_name, phone, email,usser_id)
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def _update_report(update_report,title,category, description, coordinates_latitude, coordinates_longitude,  first_name, last_name, phone, email,usser_id):
        if title:
            update_report.title = title
        if category:
            update_report.category = category
        if description:
            update_report.description = description
        if coordinates_latitude:
            update_report.coordinates_latitude= coordinates_latitude
        if coordinates_longitude:
            update_report.coordinates_longitude =  coordinates_longitude
        if first_name:
            update_report.first_name = first_name
        if last_name:
            update_report.last_name = last_name
        if phone:
            update_report.phone = phone
        if email:
            update_report.email = email
        if usser_id == -1:
            update_report.user_assing_id = None
            update_report.status = "Sin confirmar"
        else:
            update_report.user_assing_id = usser_id
            update_report.status = "En Curso"
        return update_report

    @staticmethod
    def recover_reports():
         return Report.query.all()



    @staticmethod
    def filter_by_key(status,items_per_page, key="",fecha_inicio = None, fecha_fin = None):
        key_filtered = "%" + key + "%"
        page = request.args.get('page', 1, type=int)
        if status == "Todos":
            reports = Report.query.filter(Report.title.like(key_filtered))
        else:
            reports =  Report.query.filter(Report.title.like(key_filtered)).filter_by(status = status)

        if fecha_inicio and fecha_fin:
            reports = reports.filter(Report.creation_date >= fecha_inicio, Report.creation_date <= fecha_fin )
            print (f"-----------------------------{reports.all()}----------------------------------")


        return reports.paginate(page=page, per_page=items_per_page)

    @classmethod
    def delete_by_id(cls,report_id):
        report_delete = cls.search_by_id(report_id)
        db.session.delete(report_delete)
        try:
            db.session.commit()
            return True
        except:
            return False


    @staticmethod
    def create_monitoring(description,author_id):
        monitoring_created = Monitoring(description,author_id)
        db.session.add(monitoring_created)
        try:
            db.session.commit()
            return monitoring_created
        except:
            return False

    @classmethod
    def add_monitoring(cls,report_id ,description):
        report = cls.search_by_id(report_id)
        report.monitoring.append(description)
        try:
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def _finish(cls,report_id,status):
        report = cls.search_by_id(report_id)
        if report.status in ["Cerrada","Resuelta"]:
            return False
        report.status = status
        report.closing_date = dt.now().strftime("%b %d %Y %H:%M:%S")
        try:
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def _add_monitoring(cls,report_id,description,author_id):
        description_create = cls.create_monitoring(description,author_id)
        return cls.add_monitoring(report_id, description_create)

    @classmethod
    def resolved(cls,report_id,description,author_id):
        if  cls._finish(report_id,"Resuelta"):
            return cls._add_monitoring(report_id,description,author_id)


    @classmethod
    def closing(cls,report_id,description,author_id):
        if cls._finish(report_id,"Cerrada"):
            return cls._add_monitoring(report_id,description,author_id)

    @classmethod
    def satisfy_three_monitoring(cls,report_id):
        report = cls.search_by_id(report_id)
        if len(report.get_lis_monitoring()) >= 3:
            return True
        else:
            return False

    @classmethod
    def open(cls,report_id):
        report = cls.search_by_id(report_id)
        report.status = "En curso"
        report.closing_date = ""
        cls._add_monitoring(report_id,"El seguimiento fue abierto ", session["id"])
        try:
            db.session.commit()
            return True
        except:
            return False
