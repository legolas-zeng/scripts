# -*-coding:utf-8 -*-
import xmlrpclib

class super_api(object):
    __slots__ = ['user', 'password', 'ip', 'port'] # 固定集合分配空间，减少内存使用
    def __init__(self,user,password,ip,port):
        self.user = user
        self.password = password
        self.ip = ip
        self.port = port
        #url = 'http://' + user + ':' + password + '@' + ip + ':' + port + '/RPC2'
        # url = 'http://' + self.user + ':' + self.password + '@' + self.ip + ':' + self.port + '/RPC2'
        # print url
        # self.url = url
    def ser_conn(self):
        url = 'http://' + self.user + ':' + self.password + '@' + self.ip + ':' + self.port + '/RPC2'
        conn = xmlrpclib.Server(url)
        return conn

    def conf_reload(self):
        pass

    def start_process(self,process):
        status = self.ser_conn().supervisor.startProcess(process)
        return status
    def start_process_all(self):
        pass

    def stop_process(self,process):
        status = self.ser_conn().supervisor.stopProcess(process)
        return status

    def stop_process_all(self):
        pass

    def get_info(self,process):
        info = self.ser_conn().supervisor.getProcessInfo(process)
        return info
    def get_info_all(self):
        info = self.ser_conn().supervisor.getAllProcessInfo()
        return info



a = super_api('user','123','192.168.28.130','9001')
#b = a.get_info('redis')
#c = a.start_process('nginx')
#d = a.stop_process('nginx')
e = a.get_info_all()
print e

