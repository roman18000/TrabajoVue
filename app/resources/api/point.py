from flask import jsonify, Blueprint, request
from app.dao.point import PointDAO
from app.scheme.point import point_pagination_scheme, points_scheme
from app.dao.configuration import ConfigurationDAO
from app.helpers.permission import PermissionDAO


point_api = Blueprint("points", __name__, url_prefix="/points")


@point_api.get("/")
def index():
    #PermissionDAO.assert_permission("puntos_encuentro_index") #deberia pedir permisos?
    dao = ConfigurationDAO()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", dao.items_per_page))
    points_page = PointDAO.recover_points()

    points = point_pagination_scheme.dump(points_page)

    return jsonify(points)


@point_api.get("/all")
def all_points():
    "Recupera todos los puntos de encuentro"
    recover_points_row = PointDAO.recover_points()
    points = points_scheme.dump(recover_points_row)
    return jsonify(points)