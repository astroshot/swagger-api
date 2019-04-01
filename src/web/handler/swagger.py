# coding=utf-8

from src.web.handler.base import APIBaseHandler
from src.define import SWAGGER_PATH
import yaml


class SwaggerHandler(APIBaseHandler):

    def get(self, spec_name):
        spec_file_path = "{}/{}.yaml".format(SWAGGER_PATH, spec_name)
        yaml_content = open(spec_file_path, 'r')
        content = yaml.full_load(yaml_content)
        self.render_json(content)
