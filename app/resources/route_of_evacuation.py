from flask import redirect, render_template, request, url_for,flash,session
from app.dao.configuration import ConfigurationDAO
from app.dao.route_of_evacuation import Route_of_evacuationDAO
from app.helpers.auth import Auth

from app.helpers.permission import PermissionDAO


# Protected resources


def get_values_filter_columns():
    return ["Publicado","Despublicado","Todos"]


def _obtener_valores(status, texto):
    """ Obtengo los valores para mostrar las rutas de evacuacion, ya sea con un filtro o no"""
    if request.args.get('status_id') is None:
        filtro = status
    else:
        filtro = request.args.get('status_id')
    if request.args.get('texto_id') is None:
        texto_a_filtrar = texto
    else:
        texto_a_filtrar = request.args.get('texto_id')
    return (filtro,texto_a_filtrar)

def index():
    PermissionDAO.assert_permission("route_of_evacuation_index")
    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    filtered_route = Route_of_evacuationDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("route_of_evacuation/index.html", routes=filtered_route,values=values, filtro = filtro,texto=texto_a_filtrar)

def new():
    PermissionDAO.assert_permission("route_of_evacuation_new")
    return render_template("route_of_evacuation/new.html")

def create():
    PermissionDAO.assert_permission("route_of_evacuation_new")
    parameter = request.form
    if (_validate_empty_fields(parameter["name"],parameter["publicado"],parameter["coordinates"],parameter["description"])):
            if Route_of_evacuationDAO.create_route(parameter["name"],bool(parameter.get('publicado')),parameter["coordinates"],parameter["description"]):
                msj = "Se creo el recorrido de evacuacion " + parameter["name"] + " con exito"
                flash (msj)
                return redirect(url_for("route_index"))
            else:
                msj = "Se produjo un error al momento de crealo, intentelo nuevamente"

    else:
        msj = "Complete todos los campos para que puedas continuar"
    flash (msj)
    return render_template("route_of_evacuation/new.html")

def _validate_empty_fields(name,publicado,coordinates,description):
    return bool((name and publicado and coordinates and description))


def delete(route_id):
    PermissionDAO.assert_permission("route_of_evacuation_destroy")
    route_delete = Route_of_evacuationDAO.search_by_id(route_id)
    if Route_of_evacuationDAO.delete(route_delete):
        msj = "El recorrido de evacuacion " + route_delete.name + " se elimino con exito"
    else:
        msj = "El recorrido de evacuacion "+ route_delete.name + " no se pudo eliminar, intente nuevamente"

    flash (msj)
    return redirect(url_for("route_index"))

def _parse_coordinate_string(coordinates_obj):
    list_coordinates_string = []
    for obj in coordinates_obj:
        list_new = []
        list_new.append(obj.latitude)
        list_new.append(obj.longitude)
        list_coordinates_string.append(list_new)
        #print (f"-----------La lista creada {obj.latitude}  {obj.longitude}")
    return list_coordinates_string

def edit(route_id):
    PermissionDAO.assert_permission("route_of_evacuation_update")
    modification_route = Route_of_evacuationDAO.search_by_id(route_id)
    list_coordinates_string = _parse_coordinate_string(modification_route.coordinates.order_by().all())
    #list_coordinates_string = list(reversed(list_coordinates_string))
    if modification_route:
        return render_template("route_of_evacuation/edit.html",route = modification_route,list_string = list_coordinates_string)
    return redirect(url_for('route_index'))



def modify(route_id):
    PermissionDAO.assert_permission("route_of_evacuation_update")
    parameter = request.form
    route_modification = Route_of_evacuationDAO.search_by_id(route_id)
    if route_modification:
        if (Route_of_evacuationDAO.update(route_modification,parameter["name"],int(parameter["publicado"]),parameter["coordinates"],parameter["description"])):
            msj = "Se actualizo con exito el recorrido seleccionado "
        else:
            msj = "Ocurrio un error al quere modificar el recorrido seleccionado"
    flash (msj)
    return redirect(url_for("route_index"))

def publicate_despublicate(route_id):
    #ver temas permisos
    Auth.verify_authentification()
    Route_of_evacuationDAO.publicate_despublicate(route_id)
    return redirect(url_for("route_index"))
