from flask import request,session
from app.models.configuration import Configuration
from app.db import db

def configSessionAttributes(user):
    #Hacer una consulta a la clase configuracion, y traerme los atributos de la clase
    session["id"] = user.id
    session["user"] = user.username
    session["first_and_last_name"] = user.first_name + ' ' + user.last_name
    session["first_name"] = user.first_name
    session["last_name"] = user.last_name
    session["email"] = user.email
