from flask import redirect, render_template, request, url_for,flash,session
from app.dao.configuration import ConfigurationDAO
from app.dao.user import UserDAO
from app.helpers.auth import Auth
from datetime import datetime as dt
from app.helpers.permission import PermissionDAO

from app.dao.report import ReportDAO
import json

def get_values_filter_columns():
    return ["En curso","Resuelta","Cerrada","Sin confirmar","Todos"]

def _obtener_valores(status, texto):
    """ Obtengo los valores para mostrar los reportes, ya sea con un filtro o no"""
    if request.args.get('status_id') is None:
        filtro = status
    else:
        filtro = request.args.get('status_id')
    if request.args.get('texto_id') is None:
        texto_a_filtrar = texto
    else:
        texto_a_filtrar = request.args.get('texto_id')
    return (filtro,texto_a_filtrar)

def _analizar_fecha(inicio,fin):
    año_in,mes_in,dia_in = inicio.split("-")
    año_in = int(año_in)
    mes_in = int(mes_in)
    dia_in = int(dia_in)
    fecha_inicio = dt(año_in,mes_in,dia_in).strftime("%b %d %Y %H:%M:%S")
    if fin:
        año_fin,mes_fin,dia_fin = fin.split("-")
        año_fin = int(año_fin)
        mes_fin = int(mes_fin)
        dia_fin = int(dia_fin)
        fecha_fin = dt(año_fin,mes_fin,dia_fin).strftime("%b %d %Y %H:%M:%S")

    else:
        fecha_fin = dt.now().strftime("%b %d %Y %H:%M:%S")
    return (fecha_inicio,fecha_fin)

def index():
    PermissionDAO.assert_permission("denuncia_index")
    dao = ConfigurationDAO()
    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    fecha_in = request.args.get("fecha_inicio")
    if fecha_in and  (len(fecha_in) < 4):
        fecha_inicio,fecha_fin = _analizar_fecha(request.args.get("fecha_inicio"),request.args.get("fecha_fin"))
        filtered_reports = ReportDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar,fecha_inicio,fecha_fin)
    else:
        filtered_reports = ReportDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("report/index.html", reportes=filtered_reports,values=values, filtro = filtro,texto=texto_a_filtrar)

def new():
    PermissionDAO.assert_permission("denuncia_new")
    users = UserDAO.recover_users()
    return render_template("report/new.html",users= users)


def create():
    PermissionDAO.assert_permission("denuncia_new")
    parameter = request.form
    if _validate_empty_fields(parameter["title"],parameter["category"],parameter["descript"],parameter["coordenada_lat"],parameter["coordenda_long"],parameter["first_name"],parameter["last_name"],parameter["phone"],parameter["email"],parameter["user_assing"]):
        if ReportDAO.existe_coordinates(coordinates_latitude = parameter["coordenada_lat"],coordinates_longitude = parameter["coordenda_long"]):
            msj = "Las coordenadas ya existen, se esta trabajando para arreglar el problema"
        else:
            usser_id = int(parameter["user_assing"])
            if usser_id  == -1:
                usser_id = None
            if ReportDAO.create_report(parameter["title"],parameter["category"],parameter["descript"],parameter["coordenada_lat"],parameter["coordenda_long"],parameter["first_name"],parameter["last_name"],parameter["phone"],parameter["email"],usser_id):
                msj = "Se creo la denuncia " + parameter["title"] + " con exito"
            else:
                flash (" hubo uno error al crear la denuncia, intene nuevamente")
                return redirect(url_for('report_new'))
    else:
        msj = "Por favor complete todos los campost para poder continuar"
    flash (msj)
    return redirect(url_for('report_index'))

def _validate_empty_fields(title,category, description, coordinates_latitude, coordinates_longitude,  first_name, last_name, phone, email,user_assing_id ):
        return (bool(title and category and description and coordinates_latitude and coordinates_longitude and  first_name and last_name and phone and email and user_assing_id ))


def delete(report_id):
    PermissionDAO.assert_permission("denuncia_destroy")
    report_delete = ReportDAO.search_by_id(report_id)
    if ReportDAO.delete_by_id(report_id):
        msj = "El reporte " + report_delete.title + " a sido eliminado con exito"
    else:
        msj = "Error al quere borrar el reporte  " + report_delete.title + " de la tabla"
    flash (msj,"info")
    return redirect(url_for("report_index"))


def edit(report_id):
    PermissionDAO.assert_permission("denuncia_update")
    modification_report = ReportDAO.search_by_id(report_id)
    if modification_report:
        users_assign = UserDAO.recover_users()
        msj = "Los campos que desea dejar igual dejenlo sin rellenar"
        user_asignado = modification_report.user_assing
        try:
            users_assign.remove(user_asignado)
        except:
            user_asignado = ""
        return render_template("report/edit.html", report = modification_report, msj = msj, users = users_assign,user_assing = user_asignado)
    return redirect(url_for("report_index"))

def modify(report_id):
    PermissionDAO.assert_permission("denuncia_update")
    parameter = request.form
    user_id = int(parameter["user_assing"])
    if (bool(UserDAO.search_by_id(user_id)) or (user_id == -1)):
        report_update = ReportDAO.search_by_id(report_id)
        if ReportDAO.existe_coordinates(coordinates_latitude = parameter["coordenada_lat"],coordinates_longitude = parameter["coordenda_long"]):
            msj = "Las coordenadas ya existen, se esta trabajando para arreglar el problema"
        else:
            if ReportDAO.update_report(report_update,parameter["title"],parameter["category"],parameter["description"],parameter["coordenada_lat"],parameter["coordenda_long"],
                parameter["first_name"],parameter["last_name"],parameter["phone"],parameter["email"],user_id):
                msj = "se modifico con exito el reporte " + parameter["title"]
            else:
                msj = "Se produjo un error al modificar, intente nuevamente "
                flash(msj)
                return redirect(url_for("report_edit",report_id = report_id))
    else:
        msj = "Ingrese un usuario valido "

    flash (msj)
    return redirect(url_for("report_index"))


def show(report_id):
    PermissionDAO.assert_permission("denuncia_show")
    report = ReportDAO.search_by_id(report_id)
    if report.status in ["Cerrada","Resuelta"]:
        cerrada = True
    else:
        cerrada = False
    return render_template("/report/detail.html",report = report,cerrada = cerrada)

def add_monitoring(report_id):
    PermissionDAO.assert_permission("denuncia_add_monitoring")
    if request.form["description"] != " ":
        description_create = ReportDAO.create_monitoring(request.form["description"],session["id"])
        ReportDAO.add_monitoring(report_id, description_create)
        flash ("Se agrego el seguimiento correctamente")
    else:
        flash("Ingrese una descripcion ")
    return redirect(url_for("report_show",report_id = report_id))

def close(report_id):
    PermissionDAO.assert_permission("denuncia_close")
    if ReportDAO.satisfy_three_monitoring(report_id):
        if ReportDAO.closing(report_id,request.form["description"],session["id"]):
            flash ("Se cerro la denuncia con exito")
        else:
            flash ("La denuncia ya estaba cerrada")
    else:
        flash ("Usted tien que generar 3 descripciones para cerrar el seguimiento")
    return redirect(url_for("report_show",report_id = report_id))

def resolved(report_id):
    PermissionDAO.assert_permission("denuncia_resolved")
    if request.form["description"] != " ":
        if ReportDAO.resolved(report_id,request.form["description"],session["id"]):
            flash ("Se cerro la denuncia con exito")
        else:
            flash ("La denuncia ya estaba cerrada")
    else:
        flash("Ingrese una descripcion ")
    return redirect(url_for("report_show",report_id = report_id))

def open(report_id):
    PermissionDAO.assert_permission("denuncia_open")
    report = ReportDAO.search_by_id(report_id)
    if  report.status in ["Cerrada","Resuelta"]:
        ReportDAO.open(report_id)
        flash("Se abrio nuevamente la denuncia")
    else:
        flash ("La denuncia ya estaba abierta")
    return redirect(url_for("report_show",report_id = report_id))
