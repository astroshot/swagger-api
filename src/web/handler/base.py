# coding=utf-8
from tornado.escape import json_encode
from tornado.web import RequestHandler
from src.define import list_swagger_files


class APIBaseHandler(RequestHandler):

    def render_json(self, data):
        self.set_header('Content-Type', 'application/json')
        self.finish(json_encode(data).encode('utf-8'))

    def get_base_url(self):
        return '{}://{}'.format(self.request.protocol, self.request.host)

    @property
    def schema_names(self):
        return list_swagger_files()
