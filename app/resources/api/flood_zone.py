from flask import jsonify, Blueprint, request
from app.dao.flood_zone import FloodZoneDao
from app.models.flood_zone import FloodZone
from app.scheme.flood_zone import flood_zone_scheme, flood_zone_pagination_scheme
from app.dao.configuration import ConfigurationDAO
from app.helpers.permission import PermissionDAO


flood_zones_api = Blueprint("flood_zones", __name__, url_prefix="/flood_zones")


@flood_zones_api.get("/")
def index():
    dao = ConfigurationDAO()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", dao.items_per_page))
    flood_zones_page = FloodZoneDao.recover_flood_zones_paginated(page, per_page)

    flood_zones = flood_zone_pagination_scheme.dump(flood_zones_page)

    return jsonify(flood_zones)

@flood_zones_api.get("/all")
def all_zones():
    recover_flood_zones_row = FloodZoneDao.recover_flood_zones()
    flood_zones = flood_zone_scheme.dump(recover_flood_zones_row, many=True)
    for zone in flood_zones:
        zone['coordinates'] = FloodZoneDao.recover_coordinates_by_id(zone['id'])

    return jsonify(zonas=flood_zones)

@flood_zones_api.get("/show/<int:id>")
def show(id):
    flood_zone_instance = FloodZoneDao.recover_flood_zone(id)
    flood_zone = flood_zone_scheme.dump(flood_zone_instance)
    if (not flood_zone == {}):
        flood_zone['coordinates'] = FloodZoneDao.recover_coordinates_by_id(flood_zone['id'])

    return jsonify(attributes=flood_zone)
