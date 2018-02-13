# -*-coding:utf-8 -*-
import os
import socket
import SimpleXMLRPCServer

# 获取当前路径
def pwd():
    return os.getcwd()

# 列出指定目录中的内容
def ls(directory=None):
    if directory is None:
        directory = pwd()
    try:
        return os.listdir(directory)
    except OSError as e:
        return e

# 改变工作路径
def cd(directory):
    try:
        os.chdir(directory)
    except OSError as e:
        return e
    return 'change current working direcotry to: %s' % (directory)

# 创建目录
def mkdir(directory):
    try:
        os.mkdir(directory)
    except OSError as e:
        return e
    else:
        return 'successfully create directory: %s' % directory

# 文件拷贝
def cp(src, dest):
    with open(src, 'r') as fin:
        with open(dest, 'w') as fout:
            fout.write(fin.read())
    return 'copy %s->%s' % (src, dest)

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def show(self):
        return str(self)

    def __str__(self):
        return 'Person(name=%s,age=%s' % (self._name, self._age)


if __name__ == "__main__":
    # name = socket.getfqdn(socket.gethostname(  ))
    # ip = socket.gethostbyname(name)
    # print ip
    s = SimpleXMLRPCServer.SimpleXMLRPCServer(("192.168.28.130", 8005))
    print "Listening on port 8005"
    s.register_function(pwd)  # 注册函数
    s.register_function(ls)
    s.register_function(cd)
    s.register_function(mkdir)
    s.register_function(cp)
    p = Person('python', 28)
    s.register_instance(p)  # 注册对象实例
    s.serve_forever()