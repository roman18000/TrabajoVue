from flask import redirect, render_template, request, url_for,flash,session
from app.dao.configuration import ConfigurationDAO
from app.dao.user import UserDAO
from app.helpers.auth import Auth
from app.dao.role import RoleDAO
from app.helpers.permission import PermissionDAO


# Protected resources


def get_values_filter_columns():
    return ["Activo","Bloqueado","Todos"]


def _obtener_valores(status, texto):
    """ Obtengo los valores para mostrar los usuarios, ya sea con un filtro o no"""
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
    PermissionDAO.assert_permission("usuario_index")

    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    filtered_users = UserDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("user/index.html", users=filtered_users,values=values, filtro = filtro,texto=texto_a_filtrar)


def new():
    PermissionDAO.assert_permission("usuario_new")
    return render_template("user/new.html")



def create():
    PermissionDAO.assert_permission("usuario_new")

    parameter = request.form
    errors = []

    validos = _validate_empty_fields(parameter["first_name"], parameter["last_name"], parameter["email"],parameter["user"],parameter["password"])
    if validos:
        if UserDAO.exist_email(parameter["email"]):
            errors.append("El email " + parameter["email"] +" ya existe, ingrese otro")
        elif UserDAO.exist_username(parameter["user"]):
            errors.append("El usuario " + parameter["user"] + " ya existe, ingrese otro")
        else:
            if (UserDAO.create_user(parameter["first_name"],parameter["last_name"],parameter["email"],parameter["user"],parameter["password"])):
                msj = "Se creo el usuario " + parameter["user"] + " exitosamente"
                flash(msj)
                return redirect(url_for("user_index"))
    else:
        errors.append("Por favor complete todos los campos")
    return render_template("user/new.html", errors = errors)


def _validate_empty_fields(first_name,last_name,email,user,password):
    if  email  and password and user  and first_name and last_name:
        return True
    else:
        return False



def _recuperar_values_roles(modification_user):
    list = ["operador","administrador","sin asignar"]
    roles_name = RoleDAO.recover_roles_of(modification_user)
    if len(roles_name) == 0:
        print ("NO tiene nada")
        list_values_roles = ["sin asignar"]
    else:
        list_values_roles = roles_name
    for value in list:
        if not (value in list_values_roles):
            list_values_roles.append(value)
    print (list_values_roles)
    return list_values_roles

def edit(user_id):
    PermissionDAO.assert_permission("usuario_update")
    modification_user = UserDAO.search_by_id(user_id)
    if modification_user:
        values = _recuperar_values_roles(modification_user)
        msj = "Los campos que desea dejar igual dejenlo sin rellenar"
        return render_template("user/edit.html", user = modification_user, msj = msj,value = values)
    return redirect(url_for("user_index"))

def modify(user_id):
    PermissionDAO.assert_permission("usuario_update")

    parameter = request.form
    user_update = UserDAO.search_by_id(user_id)
    emailBoolean = UserDAO.exist_email(parameter["email"])
    if emailBoolean:
        msj = "El email " + parameter["email"] +" ya existe, ingrese otro"
    elif UserDAO.exist_username(parameter["user"]):
        msj = "El usuario " + parameter["user"] + " ya existe, ingrese otro"

    else:
        obj = UserDAO.update(user_update,parameter["user"],parameter["email"],parameter["password"],parameter["first_name"], parameter["last_name"],parameter["role"])
        if obj:
            msj = "Se modifico el usuario " + parameter["user"] + " exitosamente"
        else:
            msj = "Se produjo un error al modificar, intente nuevamente "
        flash (msj)
        return redirect(url_for("user_index"))
    values = _recuperar_values_roles(user_update)
    flash(msj)
    return render_template("user/edit.html" , user = user_update, msj = msj, value = values)

def delete(user_id):
    PermissionDAO.assert_permission("usuario_destroy")
    if UserDAO.delete_by_id(user_id):
        msj = "El usuario  ha sido eliminado con exito"
    else:
        msj = "Error al quere borrar el usuario  de la tabla"
    flash (msj,"info")
    return redirect(url_for("user_index"))

def activate_desactivate(user_id):
    Auth.verify_authentification()
    UserDAO.activate_desactivate(user_id)
    return redirect(url_for("user_index"))
