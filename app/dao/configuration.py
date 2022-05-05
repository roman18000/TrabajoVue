from flask import request
from app.models.configuration import Configuration
from app.models.views_sort import View
from app.db import db

class ConfigurationDAO:

    def __init__(self):
        self._config_row = Configuration.query.filter_by(id=1).first()


    @property
    def background(self):
        return self._config_row.background

    @background.setter
    def background(self,value):
        try:
            self._config_row.background = value
            db.session.commit()
        except:
            raise Exception

    @property
    def items_per_page(self):
        return self._config_row.items_per_page

    @items_per_page.setter
    def items_per_page(self, value):
        if value in Configuration.get_valid_paginations():
            self._config_row.items_per_page = value
            db.session.commit()
        else:
            raise Exception

    def order_list(self,array, value):
        array.remove(value)
        # Lo coloco en el indice 0, para en la vista mostrarlo como la opcion actual utilizada
        array.insert(0,value)
        return array

    def values_to_render(self):
        order_items = Configuration.get_valid_paginations()
        self.order_list(order_items, self._config_row.items_per_page)
        order_backgrounds = Configuration.get_valid_colors()
        self.order_list(order_backgrounds, self._config_row.background)
        values = { "items_per_page" : order_items,
                    "background" : order_backgrounds
                    }
        return values


    def set_view_user_values(self, values):
        user_row = View.query.filter_by(id = "user").first()
        user_row.sorted_by_column = values["column"]
        user_row.sort_type = values["type"]
        try:
            db.session.commit()
        except:
            raise Exception

    def set_view_issue_values(self, values):
        issue_row = View.query.filter_by(id = "issue").first()
        issue_row.sorted_by_column = values["column"]
        issue_row.sort_type = values["type"]
        try:
            db.session.commit()
        except:
            raise Exception

    def set_view_point_values(self, values):
        point_row = View.query.filter_by(id = "point").first()
        point_row.sorted_by_column = values["column"]
        point_row.sort_type = values["type"]
        try:
            db.session.commit()
        except:
            raise Exception
