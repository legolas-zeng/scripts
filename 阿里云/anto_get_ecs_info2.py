# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
import json,uuid
import MySQLdb
from MySQLdb import*


# 配置地域和可用区
Region_ID = ['cn-beijing','cn-hongkong']

# 配置数据库信息
DB_INFO = {'user':'jumpserver',
           'host':'192.168.1.202',
           'pwd':'z1P98EDggNE19bcl0I23rGhR',
           'dbname':'jumpserver',
           'port':3306,}

# 配置access
Prod_ID = {'doupai':{'access_key_id':'LTAICn8RWNvohrYS',
                     'access_key_secret':'Yct1hP7CyTcFp4YSVhSzYNCjkaZMG9'},
           'qutui':{'access_key_id':'',
                     'access_key_secret':''},}


# 数据库类
class CDataBase(object):
    def __init__(self, host, user, passwd, database, port=3306):
        self._host = host
        self._user = user
        self._pwd = passwd
        self._database = database
        self._port = port
        self._connect_db()


    def _connect_db(self):
        try:
            self._conn = Connection(self._host, self._user, self._pwd, self._database, self._port,
                                    cursorclass=cursors.DictCursor)
        except MySQLdb.Error, e:
            print '[connect_db]failed.error:%s' % str(e)
            self._conn = None
            return
        self._cursor = self._conn.cursor()
        #self._cursor.execute('set autocommit=1')
        #self._cursor.execute('SET NAMES utf8')
        self._cursor.execute('SET NAMES latin1')
        #self._cursor.execute('set character_set_results = latin1')


    def __del__(self):
        if self._conn:
            self._cursor.close()
            self._conn.close()

    def update_sql(self, sql, param):
        '''执行insert、update、delete语句'''
        ret = self._cursor.execute(sql, param)
        return ret

    def exec_many_sql(self, sql, param):
        self._cursor.executemany(sql, param)
        return self._cursor.fetchall()

    def select_sql(self, sql, param):
        '''执行select语句'''
        self._cursor.execute(sql, param)
        if self._cursor.rowcount == 0:
            return ()

        return self._cursor.fetchall()
        #return self._convert_to_name()

    def _convert_to_name(self):
        records = self._cursor.fetchall()
        fields = self._get_fields()

        results = []
        for record in records:
            rec = {}
            for i in xrange(len(fields)):
                rec[fields[i]]=record[i]

            results.append(rec)

        return tuple(results)

    def _get_fields(self):
        """map indices to fieldnames"""
        if not self._cursor.description:
            return {}

        results = {}
        column = 0

        for des in self._cursor.description:
            fieldname = des[0]
            results[column] = fieldname
            column = column + 1

        return results

    def ping(self):
        try:
            _ret = self._conn.ping()
        except Exception, e:
            _ret = e

        if _ret is None:
            return True

        ## reconnect
        self.close()
        return self._connect_db()

    def close(self):
        if self._conn != None:
            self._conn.close()

        self._conn = None
        self._cursor = None

# 数据库操作
class GmDB(object):
    def __init__(self):
        self.host = DB_INFO.get(host)
        self.user = DB_INFO.get(user)
        self.pwd = DB_INFO.get(pwd)
        self.dbname = DB_INFO.get(dbname)
        self.port = DB_INFO.get(port)
    def db_conn(self):
        conn = CDataBase(self.host, self.user, self.pwd,
                         self.dbname, self.port)
        return conn

class RUN_DB(object):
    def __init__(self):
        self.host = DB_INFO.get('host')
        self.user = DB_INFO.get('user')
        self.pwd = DB_INFO.get('pwd')
        self.dbname = DB_INFO.get('dbname')
        self.port = DB_INFO.get('port')
        self._conn = self.db_conn()
    def db_conn(self):
        conn = MySQLdb.connect(self.host, self.user, self.pwd,
                         self.dbname, self.port)
        return conn
    def create_node(self,key,value,id,date_create):
        cursor = self._conn.cursor()
        sql = """insert into assets_node(`value`,`key`,`id`,date_create,child_mark) values ('%s','%s','%s','%s','%s')""" %(key,value,id,date_create,'0')
        cursor.execute(sql)
        self._conn.commit()
        cursor.close()
        data = cursor.fetchone()
        print data
        return data
    def save_host(self,id,ip,hostname,os):
        cursor = self._conn.cursor()
        sql = """insert into assets_asset(`id`,ip,hostname,port,os) values ('%s','%s','%s','%s','%s')""" % (
            id, ip, hostname,22, os)
        cursor.execute(sql)
        self._conn.commit()
        cursor.close()
        data = cursor.fetchone()

def get_data(key):
    # 创建AcsClient实例
    client = AcsClient(
       "LTAICn8RWNvohrYS",
       "Yct1hP7CyTcFp4YSVhSzYNCjkaZMG9",
       key
    );
    # 创建request，并设置参数
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_PageSize(10)
    # 发起API请求并显示返回值
    # response = client.do_action_with_exception(request)

    request.set_accept_format('json')
    # 发起请求，获取数据
    #result = json.loads(client.do_action_with_exception(request)).get('Instances').get('Instance')
    result = json.loads(client.do_action_with_exception(request)).get('Instances').get('Instance')
    return result

def handle_data(key):
    data = get_data(key)
    result = []

    for line in data:
        data = (
            line.get('InstanceId'), # 实例ID
            line.get('InstanceName'), # 名称
            # line.get('PublicIpAddress').get('IpAddress')[0],
            # line.get('InnerIpAddress').get('IpAddress')[0],
            line.get('NetworkInterfaces').get('NetworkInterface')[0].get('PrimaryIpAddress'), # 私有ip
            line.get('EipAddress').get('IpAddress'), # 弹性公网ip
            line.get('OSType'), # 操作系统
            'doupai',
        )
        result.append(data)
    print (result)
    return result

if __name__ == '__main__':
    for Region in Region_ID:
        data = handle_data(Region)
        for info in data:
            id = ''.join(str(uuid.uuid1()).split('-'))
            ip = info[2]
            hostname = info[1]
            os = info[4]
            db = RUN_DB()
            print id,ip,hostname,os
            db.save_host(id,ip,hostname,os)
