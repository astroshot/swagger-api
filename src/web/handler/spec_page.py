# coding=utf-8
from src.web.handler.base import APIBaseHandler


class SwaggerAPIPageHandler(APIBaseHandler):

    def get(self, spec_name):

        self.render(
            'page.html',
            base_url=self.get_base_url(),
            spec_name=spec_name,
            schema_names=self.schema_names,
        )
