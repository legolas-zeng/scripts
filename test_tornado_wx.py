# -*-coding:utf-8 -*-
import requests
import urllib
import json

def send():
    data = {
        'core':'1',
        'path': '/data/game/game_1001/linux',
        'size': '138M',
        'msg': u'超大文件已经删除',
        'ip':'192.168.28.130'
    }

    r = requests.post('http://192.168.2.120:8000', data=data)
    status_code = r.status_code
    print status_code
    url = 'http://192.168.2.120:8000'

send()