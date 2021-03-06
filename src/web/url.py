# coding=utf-8

from src.web.handler import HomeHandler
from src.web.handler import SwaggerHandler
from src.web.handler import SwaggerAPIPageHandler


handlers = [
    (r'/', HomeHandler),
    (r'/api/([\w.-]+)', SwaggerHandler),
    (r'/doc/([\w.-]+)', SwaggerAPIPageHandler),
]
