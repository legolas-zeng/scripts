# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver  # 新引入httpserver模块
import tornado.options # 新导入的options模块
from tornado.web import url, RequestHandler
import config

tornado.options.define("port", default=8081, type=int, help="run server on the given port.")  # 定义服务器监听端口选项
tornado.options.define("itcast", default=[], type=str, multiple=True, help="itcast subjects.") # 无意义，演示多值情况

class IndexHandler(RequestHandler):
    def get(self):
        self.write("Hello Itcast!")


class ItcastHandler(RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)


if __name__ == "__main__":
    # tornado.options.parse_config_file("./config")  # 导入配置的路径
    tornado.options.parse_command_line()

    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/cpp", ItcastHandler, {"subject": "c++"}),
        url(r"/python", ItcastHandler, {"subject": "python"}, name="python_url"),
    ], debug=True)

    tornado.options.parse_command_line()
    print(tornado.options.options.itcast)  # 输出多值选项

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    # http_server.bind(8081)
    # http_server.start(2)   # os.fork  不要在windows系统上用,不然会报错
    tornado.ioloop.IOLoop.current().start()