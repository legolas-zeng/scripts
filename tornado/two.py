# -*-coding:utf-8 -*-
import tornado
from tornado import ioloop
from tornado import web
from tornado.options import define, options
import itchat
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

define("port", default=8000, type=int)


def lc():
    print("登陆成功！")

def ec():
    print("退出登陆")


def get_UserName(NickName):
    info = itchat.search_friends(nickName=NickName)
    fname = info[0]['UserName']
    return fname

def send_msg(fname):
    b = itchat.send('test msg', toUserName=fname)
    print b
    req = b.get('BaseResponse').get('Ret')
    if req == 0 :
        print u'消息发送成功'

class IndexHandler(web.RequestHandler):
    def get(self):
        self.write('hello ,world')
    def post(self):
        msg = self.get_argument('msg')
        names = self.get_argument('path')
        size = self.get_argument('size')
        print msg,names,size
        name = get_UserName('风居住的街道')
        send_msg(name)
        # info = itchat.search_friends(nickName='风居住的街道')
        # print info
        # fname = info[0]['UserName']
        # b = itchat.send('test msg', toUserName=fname)
        # print b
        # req = b.get('BaseResponse').get('Ret')
        # if req == 0:
        #     print u'消息发送成功'


if __name__ == "__main__":
    itchat.auto_login(hotReload=True,enableCmdQR=2, loginCallback=lc, exitCallback=ec)
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()