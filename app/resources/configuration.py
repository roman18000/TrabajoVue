from flask import render_template, request, flash,session
from app.models.configuration import Configuration
from app.helpers.auth import Auth
from app.dao.configuration import ConfigurationDAO
from app.helpers.form_validator import FormConfigValidator

from app.helpers.permission import PermissionDAO

def index():
    PermissionDAO.assert_permission("configuracion_index")

    dao = ConfigurationDAO()
    config_values = dao.values_to_render()
    return render_template("configuration/index.html", values = config_values)


def update():
    PermissionDAO.assert_permission("configuracion_index")

    errors = []
    configDao = ConfigurationDAO()
    frmValidator = FormConfigValidator()
    params = request.form
    if (int(params["items-per-page"])) not in Configuration.get_valid_paginations():
            errors.append("La cantidad de items por pagina que ingreso es invalida")

    else:
            # configDao en su setter, hace el commit en la bd.
            configDao.items_per_page = int(params["items-per-page"])
    if not (frmValidator.color_is_valid(params["color-background-selected"])):
         errors.append("Ingreso un color invalido para el color de fondo")
    else:
            configDao.background = params["color-background-selected"]
    if ( (params["user-col-selected"] not in Configuration.get_valid_user_columns()) or (params["user-type-selected"] not in Configuration.get_valid_sort_types()) ):
         errors.append("El campo seleccionado para ordenar los usuario o su tipo de orden son incorrectos.")
    else:
       configDao.set_view_user_values({
          "column":params["user-col-selected"],
          "type":params["user-type-selected"]
       })

    if frmValidator.validate_issue_values(params["issue-col-selected"], params["issue-type-selected"]):
       configDao.set_view_issue_values({
          "column":params["issue-col-selected"],
          "type":params["issue-type-selected"]
       })
    else:
       errors.append("El campo seleccionado para ordenar las consultas o su tipo de orden son incorrectos.")
    if frmValidator.validate_point_values(params["point-col-selected"], params["point-type-selected"]):
       configDao.set_view_point_values({
          "column":params["point-col-selected"],
          "type":params["point-type-selected"]
       })
    else:
       errors.append("El campo seleccionado para ordenar los puntos de encuentro o su tipo de orden son incorrectos.")


    return render_template("configuration/index.html", values = configDao.values_to_render(), errors = errors)
