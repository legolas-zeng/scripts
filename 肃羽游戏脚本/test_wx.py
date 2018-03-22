# -*-coding:utf-8 -*-
import itchat
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

def get_UserName(NickName):
    nick = NickName.encode('unicode-escape')
    print nick
get_UserName('风居住的街道')