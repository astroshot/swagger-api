# coding=utf-8
from __future__ import absolute_import

from os.path import dirname, abspath
import tornado
import tornado.ioloop
import tornado.wsgi
from tornado.options import options, define

from src.web.url import handlers
from src.define import (
    STATIC_PATH, TEMPLATES_PATH
)

ROOT_PATH = abspath(dirname(dirname(__file__)))
define('port', default=8005, help='listening port', type=int)


def parse_cmd_params():
    try:
        tornado.options.parse_command_line()
    except Exception as e:
        print(e)


def get_tornado_application():
    application = tornado.web.Application(
        handlers,
        debug=True,
        template_path=TEMPLATES_PATH,
        static_path=STATIC_PATH,
    )
    return application


def get_wsgi_application():
    app = get_tornado_application()
    return tornado.wsgi.WSGIAdapter(app)


def main():
    parse_cmd_params()
    app = get_tornado_application()
    app.listen(options.port)
    print('listening port: {}'.format(options.port))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
