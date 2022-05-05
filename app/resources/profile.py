from flask import redirect, render_template, request, url_for, session, abort,flash
from app.models.user import User
from app.models.configuration import Configuration
from app.helpers.auth import Auth
from app.db import db


def index_profile(id):
    try:
        user_retorned = User.query.filter_by(id = id).first()
    except:
        flash("Ingreso el url de un usuario invalido")
        return redirect(url_for("home"))
    return render_template("profile.html", user=user_retorned)
