# coding=utf-8
import os
from os import *
from slave import *

fd = open("C:\Users\Administrator.000\Desktop\open.txt",os.O_RDWR|os.O_CREAT)
line = "654321"
b = str.encode(line) # 重新编码
os.write(fd, b) # 写入

os.close( fd)  # 关闭句柄
print ("successfully!!")