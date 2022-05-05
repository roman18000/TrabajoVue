from flask import request
from app.models.issue import Issue
from app.db import db
from app.dao.configuration import ConfigurationDAO
from app.models.views_sort import View


class IssueDAO():
    @staticmethod
    def all_paginated_issues():
        configDao = ConfigurationDAO()
        page = request.args.get('page', 1, type=int)
        view_dict = View.query.filter_by(id = "issue").first().formatted_values()
        # column = getattr(Issue,view_dict["column"])
        # order = getattr(column,view_dict["type"])
        # issues = Issue.query.order_by(order)
        issues = eval("Issue.query.order_by(Issue.{}.{}())".format(view_dict["column"], view_dict["type"]))
        issues = issues.paginate(page=page, per_page=configDao.items_per_page)
        return issues

    @staticmethod
    def create_issue(parameter):
        new_issue = Issue(parameter["email"],parameter["description"],parameter["category_id"],parameter["status_id"])
        db.session.add(new_issue)
        try:
            db.session.commit()
            return True
        except:
            return False
