
from marshmallow import Schema , fields


class CoordinateScheme(Schema):
    latitude = fields.Str(required=True)
    longitude = fields.Str(required=True)


class RouteOfEvacuationScheme(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    coordinates = fields.Nested(CoordinateScheme, many=True, data_key="coordinates")
        
class RouteOfEvacuationPaginationScheme(Schema):
    page = fields.Int()
    total = fields.String() 
    items = fields.Nested(RouteOfEvacuationScheme, many=True, data_key="recorridos")







route_of_evacuation_scheme = RouteOfEvacuationScheme(many = True)
route_of_evacuation_scheme = RouteOfEvacuationScheme()
route_of_evacuation_pagination_scheme = RouteOfEvacuationPaginationScheme()
