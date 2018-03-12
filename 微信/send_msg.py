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
username = '@543887f9df8b178af7ef8513f29eaafcebfe49bc26a81772858302d331445fa6'
itchat.auto_login(hotReload=True,loginCallback=lc, exitCallback=ec)
friends = itchat.get_friends(update=True)[0:]


# info = itchat.search_friends(name='wxsendmsg')

def get_UserName(NickName):
    info = itchat.search_friends(nickName=NickName)
    fname = info[0]['UserName']
    return fname

def send_msg(fname,msg):
    # a = itchat.send_msg(msg='text message', toUserName=fname)
    # print a
    b = itchat.send('test msg', toUserName=fname)
    print b
    req = b.get('BaseResponse').get('Ret')
    if req == 0 :
        print u'消息发送成功'

name = get_UserName('风居住的街道')
send_msg(name)

# def get_var(var):
#     variable = []
#     for i in friends:
#         value = i[var]
#         print value
# NickName = get_var("NickName")
# Sex = get_var('Sex')
# Province = get_var('Province')
# City = get_var('City')
# Signature = get_var('Signature')





