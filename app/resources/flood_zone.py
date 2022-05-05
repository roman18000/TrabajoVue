import re

from werkzeug.utils import redirect, secure_filename
from app.helpers.auth import Auth
from flask import render_template, request, url_for, flash, session
from app.dao.configuration import ConfigurationDAO
from app.dao.flood_zone import FloodZoneDao
from app.models.coordinate import Coordinate
from app.models.flood_zone import FloodZone
from app.models.coordinate import FloodZone_has_coordinate
from app.helpers.permission import PermissionDAO
import csv
import os
from app.db import db
import json
import io

# def flood_zones_index():
#     Auth.is_authenticated()
#     # Permisos de ver index: Operador/Administrador

#     return render_template("flood_zone/index.html")

def get_values_filter_columns():
    return ["Publicado","Despublicado","Todos"]

def _obtener_valores(status, texto):
    """ Obtengo los valores para mostrar las zonas, ya sea con un filtro o no"""
    if request.args.get('status_id') is None:
        filtro = status
    else:
        filtro = request.args.get('status_id')
    if request.args.get('texto_id') is None:
        texto_a_filtrar = texto
    else:
        texto_a_filtrar = request.args.get('texto_id')
    return (filtro,texto_a_filtrar)

def flood_zones_index():
    PermissionDAO.assert_permission("zonas_inundables_index")

    # Permisos de ver index: Operador/Administrador

    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    filtered_zones = FloodZoneDao.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("flood_zone/index.html", zones=filtered_zones,values=values, filtro = filtro,texto=texto_a_filtrar)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'csv', 'xls', 'xlsx'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def update_csv():
    PermissionDAO.assert_permission("zonas_inundables_update")
    file = request.files.get('file')
    if file and allowed_file(file.filename):
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        reader = csv.reader(stream)
        for row in reader:
            if row[1] == 'name' or row[1] == 'area' or FloodZoneDao.name_exists(row[0]):
                pass
            else:
                flood_zone = FloodZone(name=row[0])
                db.session.add(flood_zone)
                coords = json.loads(row[1])
                for coor in coords:

                    coordinate = Coordinate(latitude=float(coor[0]), longitude=float(coor[1]))
                    db.session.add(coordinate)
                    flood_zone.coordinates.append(coordinate)
                db.session.commit()



    else:
        flash("No ha subido ningun archivo.")
        return redirect(url_for("flood_zone_index"))
    return redirect(url_for("flood_zone_index"))

def profile(id):
    PermissionDAO.assert_permission("zonas_inundables_index")

    flood_zone = FloodZoneDao.search_object_by_id(id)

    return render_template("flood_zone/profile.html", flood_zone=flood_zone)


def delete(flood_zone_id):
    #colocar permiso de borrado
    PermissionDAO.assert_permission("zona_inundable_destroy")
    flood_zone_delete = FloodZoneDao.search_object_by_id(flood_zone_id)
    if FloodZoneDao.delete(flood_zone_delete):
         msj = "La zona inundable " + flood_zone_delete.name + " ha sido eliminado con exito"
    else:
        msj = "Error al querer borrar la zona inundable " + flood_zone_delete.name + " de la tabla, intente nuevamente"

    flash (msj,"info")
    return redirect(url_for("flood_zone_index"))

def publicate_despublicate(flood_zone_id):
    #ver temas permisos
    Auth.verify_authentification()
    FloodZoneDao.publicate_despublicate(flood_zone_id)
    return redirect(url_for("flood_zone_index"))
