# -*-coding:utf-8 -*-import tornado.httpserverimport tornado.ioloopimport tornado.optionsimport tornado.webfrom tornado.options import define, options# TODO 全局配置define("port", default=8001, help="run on the given port", type=int)# TODO 定义RequestHandler请求处理器，并添加了一个处理get请求方式的方法class IndexHandler(tornado.web.RequestHandler):	def get(self):		greeting = self.get_argument('one', 'Hello')		self.write(greeting + ', tornado!') #向响应中，写入数据，响应信息		print greeting		class Sendinfo():    def get(self):        self.post()    def post(self):        if not self.check_sinature():            self.write(json.dumps({'ret': -1, 'result': 'error'}))        one = self.get_argument('one', '')        if not one or one == '':            print one        returnif __name__ == "__main__":	tornado.options.parse_command_line()	app = tornado.web.Application(handlers=[(r"/", IndexHandler)],debug=True) #创建一个应用对象	http_server = tornado.httpserver.HTTPServer(app) #httpserver监听端口	http_server.listen(options.port)  #绑定一个监听端口		tornado.ioloop.IOLoop.instance().start() #启动web程序，开始监听端口的连接