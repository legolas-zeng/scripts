import xmlrpclib

server = xmlrpclib.ServerProxy("http://192.168.28.130:8005")
b = server.reqs.show()
print b
a = server.ls('/data')
print a