# coding=utf-8
# @Time    : 2019/6/11 16:33
# @Author  : zwa

import cx_Oracle as oracle

# connect oracle database
db = oracle.connect('credit_t1/wyj102030@192.168.3.17:1521/creditx') # 用户名/密码@oracleserver的ip地址/数据库名字

# create cursor
cursor = db.cursor()

# execute sql
cursor.execute('show tables')

# fetch data
data = cursor.fetchone()

print('Database time:%s' % data)

# close cursor and oracle
cursor.close()
db.close()