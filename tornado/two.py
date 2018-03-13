# -*-coding:utf-8 -*-
import tornado,json,time
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

# 这里添加管理员的微信昵称
admin = ['风居住的街道','Willie']
# 这里添加群组名
rooms = []
def lc():
    print("登陆成功！")

def ec():
    print("退出登陆")


def get_UserName(NickName):
    info = itchat.search_friends(nickName=NickName)
    fname = info[0]['UserName']
    return fname

def get_Group(groupname):
    group = itchat.search_chatrooms(name=groupname)
    if group is not None:
        group_name = group[0]['UserName']
        return group_name

def send_msg(fname,msg):
    b = itchat.send(msg, toUserName=fname)
    req = b.get('BaseResponse').get('Ret')
    if req == 0 :
        print u'消息发送成功'

def msg_info(msg):
    if msg.get('core')[0] == '1':
        event = msg.get('msg')[0]
        Time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        size = msg.get('size')[0]
        path = msg.get('path')[0]
        ip = msg.get('ip')[0]
        warn = '【'+event+'】'+"\n"+\
               u'故障机器:'+ip+"\n"+\
               u'故障路径:'+path+"\n"+\
               u'文件大小:'+size+"\n"+\
               u'报警时间:'+Time
        print warn
        return warn

class IndexHandler(web.RequestHandler):
    def get(self):
        self.write('hello ,world')
    def post(self):
        # core = self.get_argument('core')
        # info = self.get_argument('msg')
        # names = self.get_argument('path')
        # size = self.get_argument('size')
        args = self.request.arguments
        msg = msg_info(args)
        for admins in admin:
            name = get_UserName(admins)
            send_msg(name,msg)


if __name__ == "__main__":
    itchat.auto_login(hotReload=True,enableCmdQR=2, loginCallback=lc, exitCallback=ec)
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()