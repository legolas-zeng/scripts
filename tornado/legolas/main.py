# coding:utf-8
import tornado
from tornado import web,websocket,httpserver,ioloop,options
from tornado.web import url, RequestHandler,Application

options.define("port", default=8081, type=int, help="run server on the given port.")  # 定义服务器监听端口选项
options.define("itcast", default=[], type=str, multiple=True, help="itcast subjects.") # 无意义，演示多值情况

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    '''
    新的WebSocket连接打开时被调用。
    '''
    def open(self):
        pass

    '''
    连接收到新消息时被调用。
    '''
    def on_message(self, message):
        self.write_message(u"Your message was: " + message)
        print(message)
        self.write_message(u"hahhahahah")
    '''
    在客户端关闭时被调用。
    '''
    def on_close(self):
        pass


class IndexPageHandler(RequestHandler):
    def get(self):
        self.render("indexs.html")


class ItcastHandler(RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)


class Application(Application):
    def __init__(self):
        handlers = [
            (r'/', IndexPageHandler),
            (r'/ws', WebSocketHandler),
            (r"/cpp", ItcastHandler, {"subject": "c++"}),
            url(r"/python", ItcastHandler, {"subject": "python"}, name="python_url"),
        ]

        settings = {
            'template_path': 'templates',
            'static_path': 'static',
            'static_url_prefix': '/static/',
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    ws_app = Application()
    http_server = tornado.httpserver.HTTPServer(ws_app)
    # server.listen(8081)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()