from flask import render_template,jsonify,request


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que quiere acceder no existe",
    }
    return make_report(kwargs,404)


def unauthorized_error(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No está autorizado para acceder a la url",
    }
    return make_report(kwargs,401)


def Forbidden_error(e):
    kwargs = {
        "error_name": "403 Forbidden Error",
        "error_description": "No cuenta con los permisos para acceder ",
    }
    return make_report(kwargs,403)


def Bad_request(e):
    kwargs = {
        "Bad_request": "400 Bad_request",
        "error_description": "Los parametros enviados son incorrectos ",
    }
    return make_report(kwargs,400)

def Internal_Server_Error(e):
    kwargs = {
        "Internal Server Erro": "500 Internal Server Error",
        "error_description": "Error en el servidor  ",
    }
    return make_report(kwargs,500)



def make_report(data,status):
    if request.path.startswith("/api/"):
        return jsonify (data),status
    else:
        return render_template("error.html",**data),status
