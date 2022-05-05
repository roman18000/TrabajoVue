from marshmallow import Schema , fields


class PointScheme(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    coordinates_latitude = fields.Str(required=True)
    coordinates_longitude = fields.Str(required=True)
    phone = fields.Str(required=True) #lo pide como string, en el modelo esta como int
    email = fields.Str(required=True)
        
class PointPaginationScheme(Schema):
    page = fields.Int()
    total = fields.String() 
    items = fields.Nested(PointScheme, many=True, data_key="zonas")


points_scheme = PointScheme(many = True)
point_scheme = PointScheme()
point_pagination_scheme = PointPaginationScheme()