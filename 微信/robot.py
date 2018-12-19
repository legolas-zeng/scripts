# -*-coding:utf-8 -*-
from wxpy import *
import requests
import itchat
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

KEY = '89b8d50316174244a7a489ce1b381d0d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT) # 如果别人发送的是text信息
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=['——BY机器人']

    print u'收到来自的%s信息:%s'%(msg['FromUserName'],msg['Text'])
    print msg
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply

itchat.auto_login(enableCmdQR = False)
myUserName = itchat.get_friends(update=True)[0]["UserName"]
print myUserName
itchat.run()
