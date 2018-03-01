# -*-coding:utf-8 -*-
import requests

def send():
    data = {
        'msg':'1'
    }
    r = requests.post('http://192.168.28.130:8000/func', data=data)
    status_code = r.status_code
    print status_code

send()