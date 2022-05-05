from flask import jsonify, Blueprint, request
from app.dao.route_of_evacuation import Route_of_evacuationDAO
from app.scheme.route_of_evacuation import route_of_evacuation_pagination_scheme
from app.dao.configuration import ConfigurationDAO
from app.helpers.permission import PermissionDAO


route_of_evacuation_api = Blueprint("route_of_evacuation", __name__, url_prefix="/route_of_evacuation")

@route_of_evacuation_api.get("/")
def index():
    #necesito evaluar los permisos?
    dao = ConfigurationDAO()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", dao.items_per_page))
    route_of_evacuation_page = Route_of_evacuationDAO.recover_route_of_evacuation_paginated(page, per_page)

    route_of_evacuation = route_of_evacuation_pagination_scheme.dump(route_of_evacuation_page)

    return jsonify(route_of_evacuation)