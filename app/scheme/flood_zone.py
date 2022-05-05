from marshmallow import Schema , fields


class CoordinateScheme(Schema):
    latitude = fields.Str(required=True)
    longitude = fields.Str(required=True)


class FloodZoneScheme(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    colour = fields.Str(required=True)
    #coordinates = fields.Nested(CoordinateScheme, many=True, data_key="coordinates")



class FloodZonePaginationScheme(Schema):
    page = fields.Int()
    total = fields.String()
    items = fields.Nested(FloodZoneScheme, many=True, data_key="zonas")







flood_zones_scheme = FloodZoneScheme(many = True)
flood_zone_scheme = FloodZoneScheme()
flood_zone_pagination_scheme = FloodZonePaginationScheme()
