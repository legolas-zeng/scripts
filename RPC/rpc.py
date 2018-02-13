# coding: utf-8

import calendar, SimpleXMLRPCServer, time, string, os

#创建 Server 对象
class Calendar:
    def getMonth(self, year, month):
        if(type(year) is type("")):
            if(year.isdigit()):
                year=string.atoi(year)
            else:
                return "error,the argv must be number"
        if(type(month) is type("")):
            if(month.isdigit()):
                 month=string.atoi(month)
            else:
                return "error,the argv must be number"
        return calendar.month(year,month)

    def getYear(self, year):
        if(type(year) is type("")):
            if(year.isdigit()):
                year=string.atoi(year)
            else:
                return "error,the argv must be number"
        return calendar.calendar(year)

    def getDict(self):
        dict={'1':'1','2':'2','3':'3'}
        return dict

#创建实例
calendar_object = Calendar()
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("192.168.28.130", 8005))
server.register_instance(calendar_object)

#输出信息，等待链接
print "Listening on port 8005"
server.serve_forever()