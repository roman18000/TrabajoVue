from flask import redirect, render_template, request, url_for, flash
from app.dao.issue import IssueDAO
from app.helpers.auth import Auth
from app.dao.configuration import ConfigurationDAO


# Public resources
def index():
    #Auth.verify_authentification()
    # Ver proximamente en usar un staticmethod para retornar items per page, asi no se instancia siempre el objeto
    issue = IssueDAO.all_paginated_issues()
    return render_template("issue/index.html", issues=issue)


def new():
    return render_template("issue/new.html")


def create():
    #conn = connection()
    #Issue.create(conn, request.form)

    # validar ()       -faltaria metodo validar
    if IssueDAO.create_issue(request.form):
        flash("se creo flama")
    else:
        flash("No se cre")
    return redirect(url_for("issue_index"))
