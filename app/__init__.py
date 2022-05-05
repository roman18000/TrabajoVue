from os import path, environ,urandom
from flask import Flask, render_template, g, Blueprint,session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import config
from app import db
from app.resources import issue,user,point,configuration,auth,report,route_of_evacuation,profile
from app.resources.api.issue import issue_api
from app.resources.api.flood_zone import flood_zones_api
from app.resources.api.point import point_api
from app.resources.api.route_of_evacuation import route_of_evacuation_api
from app.helpers import handler
from app.helpers.auth import Auth
import logging
from app.helpers.routes import RoutesConfig
from app.helpers.configurations import format_background
from app.helpers.permission import PermissionDAO
from flask_cors import CORS

from app.resources.api.report import report_api

#diego
from oauthlib.oauth2 import WebApplicationClient
from flask_login import (LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    )

# Configuration google
GOOGLE_CLIENT_ID = "262521299225-7vupjcju1t6rhe23vu54dmev3vtl1eud.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

#Activo los loggins en la terminal de las query generadas
logging.basicConfig()
logging.getLogger("sqlalchmy.engine").setLevel(logging.INFO)

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'


    #Diego
    app.secret_key = environ.get("SECRET_KEY") or urandom(24)

    # OAuth 2 client setup
    client = WebApplicationClient(GOOGLE_CLIENT_ID)

    login_manager = LoginManager()
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    app.config["SECRET_KEY"] = "NeedConfigureAn"

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    app.config['UPLOAD_FOLDER'] =  'static'

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SESSION_PERMANENT"] = False

    #No imprime.
    #logging.info(environment)

    #if environment=="development":
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/proyecto'
    #else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://grupo3:YWMyMDEzYzE4OTY5@localhost:3306/grupo3'



    Session(app)

    # Configure db
    db.init_app(app)


    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=Auth.is_authenticated)
    app.jinja_env.globals.update(format_background=format_background)

    app.jinja_env.globals.update(has_permission=PermissionDAO.has_permission)
    app.jinja_env.globals.update(has_rol = PermissionDAO.has_rol)
    app.jinja_env.globals.update(assert_permission = PermissionDAO.assert_permission)

    # Autenticación
    app.add_url_rule(
        "/login/callback", "auth_callback", auth.callback, methods=["GET"]
    )
    app.add_url_rule("/Iniciar_sesion_google", "auth_login_google", auth.login_google)
    app.add_url_rule("/iniciar_sesion/", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]  )


    # Rutas de Consultas
    app.add_url_rule("/consultas", "issue_index", issue.index, methods = ["GET"])
    app.add_url_rule("/consultas/create", "issue_create", issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

    #ruta Perfil
    app.add_url_rule("/perfil/<id>", "profile_index", profile.index_profile)

    # Rutas de Usuarios

    app.add_url_rule("/usuarios", "user_index", user.index, methods = ["GET"])
    app.add_url_rule("/usuario/delete/<user_id>", "user_delete", user.delete)
    app.add_url_rule("/usuarios/create", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/edit/<user_id>", "user_edit", user.edit)
    app.add_url_rule("/usuarios/modification/<user_id>", "user_modification", user.modify,methods=["POST"])
    app.add_url_rule("/usuarios/desactivate_activate/<user_id>", "user_activate_desactivate", user.activate_desactivate,methods=["POST", "GET"])


    # Rutas de Puntos de encuentro
    app.add_url_rule("/puntos", "point_index", point.index, methods = ["GET"])
    app.add_url_rule("/puntos/delete/<point_id>", "point_delete", point.delete)
    app.add_url_rule("/puntos/create", "point_create", point.create, methods=["POST"])
    app.add_url_rule("/puntos/nuevo", "point_new", point.new)
    app.add_url_rule("/puntos/edit/<point_id>", "point_edit", point.edit)
    app.add_url_rule("/puntos/modification/<point_id>", "point_modification", point.modify,methods=["POST"])

    #Rutas de los Reportes
    app.add_url_rule("/report", "report_index", report.index, methods = ["GET"])
    app.add_url_rule("/report/delete/<report_id>", "report_delete", report.delete )
    app.add_url_rule("/reports/create", "report_create", report.create, methods=["POST"])
    app.add_url_rule("/reports/nuevo", "report_new", report.new)
    app.add_url_rule("/reports/edit/<report_id>", "report_edit", report.edit)
    app.add_url_rule("/reports/modification/<report_id>", "report_modification", report.modify,methods=["POST"])
    app.add_url_rule("/reports/show/<report_id>", "report_show", report.show)
    app.add_url_rule("/reports/add_monitoring/<report_id>", "report_add_monitoring", report.add_monitoring,methods=["POST"])
    app.add_url_rule("/reports/close/<report_id>", "report_close", report.close,methods=["POST"])
    app.add_url_rule("/reports/open/<report_id>", "report_open", report.open,methods=["POST"])
    app.add_url_rule("/reports/resolved/<report_id>", "report_resolved", report.resolved,methods=["POST"])


    #Rutas de recorridos de evacuacion
    app.add_url_rule("/route_of_evacuation", "route_index", route_of_evacuation.index, methods = ["GET"])
    app.add_url_rule("/route_of_evacuation/create", "route_create", route_of_evacuation.create, methods=["POST"])
    app.add_url_rule("/route_of_evacuation/nuevo", "route_new", route_of_evacuation.new)
    app.add_url_rule("/route_of_evacuation/edit/<route_id>", "route_edit", route_of_evacuation.edit)
    app.add_url_rule("/route_of_evacuation/modification/<route_id>", "route_modification", route_of_evacuation.modify, methods=["POST"])
    app.add_url_rule("/route_of_evacuation/delete/<route_id>", "route_delete", route_of_evacuation.delete )
    app.add_url_rule("/route_of_evacuation/publicate_despublicate/<route_id>", "route_publicate_despublicate", route_of_evacuation.publicate_despublicate )

# Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")





    app.add_url_rule("/configuraciones","config_index",configuration.index)
    app.add_url_rule("/configuraciones/update","config_update",configuration.update, methods=["POST"])

    # Instancio la clase para configurar las rutas

    RoutesConfig(app)

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)
    api.register_blueprint(flood_zones_api)
    api.register_blueprint(report_api)
    api.register_blueprint(point_api)
    api.register_blueprint(route_of_evacuation_api)

    app.register_blueprint(api)


    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(403, handler.Forbidden_error)
    app.register_error_handler(400, handler.Bad_request)
    app.register_error_handler(500, handler.Internal_Server_Error)
    # Implementar lo mismo para el error 500

    # Retornar la instancia de app configurada
    return app
