# -*-coding:utf-8 -*-
import itchat
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

def lc():
    print("登陆成功！")
def ec():
    print("exit")

itchat.auto_login(hotReload=True,loginCallback=lc, exitCallback=ec)
friends = itchat.get_friends(update=True)[0:]
admin = ['风居住的街道','Willie']

# info = itchat.search_friends(name='wxsendmsg')

def get_UserName(NickName):
    info = itchat.search_friends(nickName=NickName)
    fname = info[0]['UserName']
    return fname

def get_group(groupname):
    group = itchat.search_chatrooms(name=groupname)
    if group is not None:
        group_name = group[0]['UserName']
        return group_name

def send_msg(fname):
    # a = itchat.send_msg(msg='text message', toUserName=fname)
    # print a
    b = itchat.send(u'这是一条测试信息...', toUserName=fname)
    req = b.get('BaseResponse').get('Ret')
    if req == 0 :
        print u'消息发送成功'

for names in admin:
    print names
    name = get_UserName(names)
    send_msg(name)






