# coding=utf-8

from src.web.handler.base import APIBaseHandler
from src.define import PROJECT_ROOT, list_swagger_files


class HomeHandler(APIBaseHandler):

    def get(self):
        schema_names = list_swagger_files()
        self.render(
            'page.html',
            base_url=self.get_base_url(),
            spec_name=schema_names[0],
            schema_names=schema_names,
        )
