# -*-coding:utf-8 -*-
import os,re
import requests

check_path = '/data/game/'
maxsize = 100000000  # 最大为10G

def showFile():
    path = os.listdir(check_path)
    for p in path:
        if os.path.isdir(p):
            m = re.search(r".*\d",p,re.I)
            n = re.search(r"local_hub",p,re.I)
            if m!=None or n!=None:
                print p
                dir_path = os.path.join(check_path,p)
                linux_path = os.path.join(dir_path,'linux')
                size = getFolderSize(linux_path)
                if size > maxsize:
                    info = rmFile(linux_path)
                    print info
                    if info.get('core') == '1':
                        sendMsg(info)

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
        print p
        o = re.search(r"hub_log_\d+\.log",p,re.I)
        if o!=None:
            file_path = os.path.join(filePath,p)
            file_size = getfileSize(file_path)
            if file_size > maxsize:
                size = file_convert(file_size)
                #os.remove(file_path)
                print u'超大文件已删除'
                info = {
                    'core' : '1',
                    'path' : file_path,
                    'size' : size,
                    'msg' : u'超大文件已经删除',
                }
        else:
            info = {
                'core' : '0'
            }
    return info
# 获取文件大小
def getfileSize(filename):
    size = os.path.getsize(filename)
    return size
# 文件大小单位转换
def file_convert(size):
    SUFFIXES = {1000:['Bit','Kb','Mb','Gb','Tb'],1024:['Bit','Kib','Mib','Gib','Tib']}
    multiple = 1000
    if size < 0 :
        return u'文件大小必须是非负的!'
    if size > 0 and size < multiple:
        suffix = SUFFIXES[multiple][0]
        size = (format(float(size) / float(1), '.0f'))
        return size + suffix
    if size > multiple and size < pow(multiple, 2):
        suffix = SUFFIXES[multiple][1]
        size = (format(float(size) / float(multiple), '.2f'))
        return size + suffix
        # print '{0:.1f} {1}'.format(size,suffix)
    if size > pow(multiple, 2) and size < (pow(multiple, 3)):
        suffix = SUFFIXES[multiple][2]
        size = (format(float(size) / float(pow(multiple, 2)), '.2f'))
        return size + suffix
    else:
        return u'文件已经突破天际，无法显示大小！！！'

def sendMsg(data):
    r = requests.post('http://192.168.2.120:8000', data=data)
    status_code = r.status_code
    print status_code

showFile()