from flask import redirect, render_template, request, url_for, session, abort,flash
from app.dao.point import PointDAO
from app.dao.configuration import ConfigurationDAO
from app.models.configuration import Configuration
from app.helpers.auth import Auth

from app.helpers.permission import PermissionDAO


from app.db import db
from app.models.point import Point

# Protected resources

def get_values_filter_columns():
    return ["Publicado","Despublicado","Todos"]

def _obtener_valores(status,texto):
    """ Obtengo los valores para mostrar los puntos de encuentro, ya sea con un filtro o no"""
    if request.args.get('status_id') is None:
        filtro = status
    else:
        filtro = request.args.get("status_id")
    if request.args.get('texto_id') is None:
        texto_a_filtrar = texto
    else:
        texto_a_filtrar = request.args.get("texto_id")
    return (filtro,texto_a_filtrar)

def index():
    PermissionDAO.assert_permission("puntos_encuentro_index")

    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    filtered_points = PointDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("point/index.html", points=filtered_points,values=values, filtro = filtro,texto=texto_a_filtrar)

def new():
    PermissionDAO.assert_permission("puntos_encuentro_new")
    return render_template("point/new.html")


def create():
    PermissionDAO.assert_permission("puntos_encuentro_new")

    parameter = request.form
    validos = _validate_empty_fields(parameter["name"], parameter["address"], parameter["coordinates_lat"],parameter["coordinates_long"],parameter["phone"],parameter["email"],parameter["status"])
    if validos:
        if PointDAO.exist_name(parameter["name"]):
            msj = "el Nombre "+ parameter["name"] + " ya existe, ingrese otro"
        elif PointDAO.exist_adress(parameter["address"]):
            msj = "La direccion " + parameter["address"] + " ya existe , ingrese otro "
        else:

            if PointDAO.create_user(parameter["name"], parameter["address"], parameter["coordinates_lat"],parameter["coordinates_long"],parameter["phone"],parameter["email"],parameter["status"]):
                msj = "Se creo el punto de encuentro " + parameter["name"] + " exitosamente"
            else:
                msj = "Ocurrio un error al crear el punto de encuentro, intente nuevamente"
            flash (msj)
            return redirect(url_for("point_index"))
    else:
        msj = "Por favor complete todos los campos"
    flash(msj,"error")
    return redirect(url_for("point_new"))



def _validate_empty_fields(name, adress, coordinates_lat,coordinates_long,phone,email,status):
    if  name  and adress and coordinates_lat and coordinates_long and phone and email and status:
        return True
    else:
        return False

def edit(point_id):
    PermissionDAO.assert_permission("puntos_encuentro_update")

    modification_point = PointDAO.search_by_id(point_id)
    if modification_point:
        msj = "Los campos que desea dejar igual dejenlo sin rellenar"
        return render_template("point/edit.html", point = modification_point, msj= msj)
    return redirect(url_for("point_index"))

    
def modify(point_id):
    PermissionDAO.assert_permission("puntos_encuentro_update")

    parameter = request.form
    point_update = PointDAO.search_by_id(point_id)
    a = parameter["address"]
    if PointDAO.exist_name(parameter["name"]):
        msj = "el Nombre "+ parameter["name"] + " ya existe, ingrese otro"
    elif PointDAO.exist_adress(parameter["address"]):
        msj = "La direccion " + parameter["address"] + " ya existe , ingrese otro "

    else:
        if PointDAO.update(point_update,parameter["name"], parameter["address"], parameter["coordinates_lat"],parameter["coordinates_long"],parameter["phone"],parameter["email"],parameter["status"]) :
            msj = "Se modifico el punto de encuentro "+ point_update.name + " exitosamente"
        else:
            msj = "Se produjo un error al modificar, intente nuevamente "
        flash (msj)
        return redirect(url_for("point_index"))

    flash(msj,"warning")
    return render_template("point/edit.html" , point = point_update)


def delete(point_id):
    PermissionDAO.assert_permission("puntos_encuentro_destroy")


    point_delete = PointDAO.search_by_id(point_id)
    if PointDAO.delete(point_delete):
         msj = "El punto de encuentro " + point_delete.name + " a sido eliminado con exito"
    else:
        msj = "Error al querer borrar el punto de encuentro " + point_delete.name + " de la tabla, intene nuevamente"

    flash (msj,"info")
    return redirect(url_for("point_index"))
