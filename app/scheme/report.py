from app.dao.report import ReportDAO
from marshmallow import Schema , fields, post_load, validate, ValidationError
from flask import abort;

def validate_coordinates(coordinates):
    if ReportDAO.existe_coordinates(coordinates):
        try:
            raise ValidationError(" La coordenada ingresada ya existe")
        except Exception as e:
            abort(400)
def validate_category(category):
    if category in [1,2,3]:
        return True
    else:
        try:
            raise ValidationError(" La coordenada categoria ya")
        except Exception as e:
            abort(400)

class ReportScheme(Schema):
        title = fields.Str(required=True)
        category = fields.Str(required=True) # FALTA VALIDAR
        description = fields.Str(required=True)
        coordinates = fields.Str(required=True,validate = validate_coordinates)
        coordinates_longitude = fields.Str()
        coordinates_latitude = fields.Str()
        first_name = fields.Str(required=True)
        last_name = fields.Str(required=True)
        phone = fields.Int(required=True)
        email = fields.Email(required=True)

        @post_load
        def make_report(self, data, **kwargs):
            return self.inicializar_report(data)

        def inicializar_report(self,data):
            return ReportDAO.create_report_dict(data)

class Report_show_id(Schema):
    id = fields.Int(required = True)

    @post_load
    def make_report(self, data, **kwargs):
        return ReportDAO.show(data)


class Report_pagination_scheme(Schema):
    page = fields.Int()
    total = fields.String()
    items = fields.Nested(ReportScheme, many=True, data_key="report")


reports_scheme = ReportScheme(many = True)
report_scheme = ReportScheme()
report_pagination_scheme = Report_pagination_scheme()
