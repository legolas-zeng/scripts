# -*-coding:utf-8 -*-
import os
import requests

check_path = '/data/game/'
maxsize = 100000000  # 最大为10G

def showFile():
    path = os.listdir(check_path)
    for p in path:
        if os.path.isdir(p):
            dir_path = os.path.join(check_path,p)
            linux_path = os.path.join(dir_path,'linux')
            size = getFolderSize(linux_path)
            if size > maxsize:
                req,names = rmFile(linux_path)
                print req,names
                if req == '1':
                    sendMsg(names)

# 获取文件夹大小
def getFolderSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            # print(f)
    return size

# 删除文件
def rmFile(filePath):
    path = os.listdir(filePath)
    for p in path:
        file_path = os.path.join(filePath,p)
        file_size = getfileSize(file_path)
        if file_size > maxsize:
            #os.remove(file_path)
            print u'超大文件已删除'
            return '1',file_path
        else:
            return '0'
# 获取文件大小
def getfileSize(filename):
    size = os.path.getsize(filename)
    return size

def sendMsg(names):
    data = {
        'ip':'ip',
        'msg': '超大文件已经删除',
        'size':'size',
        'name':names
    }
    r = requests.post('http://192.168.2.120:8000', data=data)
    status_code = r.status_code
    print status_code

showFile()