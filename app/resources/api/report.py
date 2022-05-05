from app.dao.report import ReportDAO
from flask import jsonify, Blueprint, request
from app.scheme.report import  reports_scheme,report_scheme,report_pagination_scheme, ReportScheme
from app.dao.configuration import ConfigurationDAO
from flask import abort;
report_api = Blueprint("reportes",__name__, url_prefix = "/report")


@report_api.get("/all")
def index():
    """Recupera todos las denuncias de la base de dato, habria que ver si hay campos que no hay que mostrar"""
    recover_reports_row = ReportDAO.recover_reports()
    reports = reports_scheme.dump(recover_reports_row)
    return jsonify(reports)

@report_api.get("/")
def index_page():
    """Recupera  las denuncias paginadas  de la base de dato, habria que ver si hay campos que no hay que mostrar"""
    dao = ConfigurationDAO()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", dao.items_per_page))
    recover_reports_row = ReportDAO.recover_reports_paginated(page, per_page)

    reports = report_pagination_scheme.dump(recover_reports_row)
    return jsonify(reports)

@report_api.post("/")
def create():
    user_data = request.get_json()
    schema = ReportScheme()
    try:
        schema.load(user_data)
    except:
        return abort(400)
    return jsonify("Created"),201


#     endpoints = Blueprint('api', __name__)
# api = Api(endpoints)
# CORS(endpoints, resources='/login', allow_headers='*',
#      origins='*', methods='*', expose_headers='Authorization')
# api.add_resource(Login, '/login')
