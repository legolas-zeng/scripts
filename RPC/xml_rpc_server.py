# -*-coding:utf-8 -*-
import os
import socket
import logging
import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ThreadingMixIn

logfile_path = '/data/runlog.log'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(thread)d %(threadName)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=logfile_path,
                    filemode='w')  #记录日志级别为DEBUG

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):pass

class Command(object):
    def __init__(self):
        pass

    def pwd(self):
        return os.getcwd()

    def ls(self,directory=None):
        if directory is None:
            directory = pwd()
        try:
            return os.listdir(directory)
        except OSError as e:
            return e

    def cd(self,directory):
        try:
            os.chdir(directory)
        except OSError as e:
            return e
        return 'change current working direcotry to: %s' % (directory)

    def mkdir(self,directory):
        try:
            os.mkdir(directory)
        except OSError as e:
            return e
        else:
            return 'successfully create directory: %s' % directory

    def cp(self,src, dest):
        with open(src, 'r') as fin:
            with open(dest, 'w') as fout:
                fout.write(fin.read())
        return 'copy %s->%s' % (src, dest)

class Person:
    def show(self):
        return 'test'

if __name__ == "__main__":
    server = ThreadXMLRPCServer(("192.168.28.130", 8005), allow_none=True)
    print "Listening on port 8005"
    run = Command()
    run.reqs = Person()
    server.register_instance(run,allow_dotted_names=True) #注册，指定容许类中的'.' 这样调用
    server.serve_forever()
