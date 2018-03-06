# -*-coding:utf-8 -*-
import tornado
from tornado import ioloop
from tornado import web
from tornado.options import define, options
define("port", default=8000, type=int)

class IndexHandler(web.RequestHandler):
    def get(self):
        self.write('hello ,world')
    def post(self):
        msg = self.get_argument('msg')
        names = self.get_argument('name')
        size = self.get_argument('size')
        print msg,names,size

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()