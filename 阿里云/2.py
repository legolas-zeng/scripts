# -*- coding: utf8 -*-
import json,re,time,uuid,random,hashlib
import MySQLdb
from MySQLdb import*

# 配置数据库信息
DB_INFO = {'user':'jumpserver',
           'host':'192.168.1.202',
           'pwd':'z1P98EDggNE19bcl0I23rGhR',
           'dbname':'jumpserver',
           'port':3306,}

# 测试数据
data_test = ('实例ID', 'test-soa-node-1', '内网ip', '公网ip', 'cn-beijing', 'vpcid', '项目1')

# 节点配置
NODE_INFO = {'root':'[0]',
             'doupai':'[0]:[0]',
             'dp-cn-beijing':'[0]:[0]:[0]',
             'dp-cn-hongkong':'[0]:[0]:[1]',
             'qutui':'[0]:[1]',
             'qt-cn-beijing':'[0]:[1]:[0]',
             'qt-cn-hongkong':'[0]:[1]:[1]',
             'huozu':'[0]:[2]',
             'qt-cn-beijing':'[0]:[2]:[0]',
             'qt-cn-hongkong':'[0]:[2]:[1]',
             }

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

class GmDB(object):
    def __init__(self):
        self.host = DB_INFO.get('host')
        self.user = DB_INFO.get('user')
        self.pwd = DB_INFO.get('pwd')
        self.dbname = DB_INFO.get('dbname')
        self.port = DB_INFO.get('port')
        self._conn = self.db_conn()
    def db_conn(self):
        conn = CDataBase(self.host, self.user, self.pwd,
                         self.dbname, self.port)
        return conn
    def get_node(self,node):
        sql = "select `key` from assets_node WHERE VALUE = '%s'" %node
        print sql
        ret = self._conn.select_sql(sql, ())
        return ret
    def get_key(self,count):
        sql = "select `key` from assets_node where LENGTH(`key`)<%s and LENGTH(`key`)>%s;"%(5*int(count)+5,5*int(count))
        print sql
        ret = self._conn.select_sql(sql, ())
        return ret

# TODO 先判断assets_node是否存在node，没有就新建，有就更新assets_asset_nodes和assets_node

# TODO 从第一节点开始判断
def judge_node(node_1,node_2,node_3,node_4):
    a = GmDB()
    b = update_info()
    if a.get_node(node_2) == ():
        b.second_node(node_1,node_2)
    if a.get_node(node_3) == ():
        b.third_node(node_2,node_3)
    if a.get_node(node_4) == ():
        b.fourth_node(node_3,node_4)
    else:
        print u"所有节点已存在"

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

class update_info(object):
    # def __init__(self):
    #     time,id = self.re_info()
    # 生成id 和时间
    def re_info(self,node):
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        m = hashlib.md5()
        m.update(node)
        id = m.hexdigest()
        #id = ''.join(str(uuid.uuid1()).split('-'))
        return nowtime,id

    # 生成key
    def create_key(self,count):
        str2 = random.randint(0, 10)
        if count == 1:
            key2 = "[{}]:[{}]".format('0', str2)
            return key2

    def judge_key(self,count):
        a = GmDB()
        key = self.create_key(count)
        for info in a.get_key(count):
            print info.get('key')
            if info.get('key') == key:
                return '1'
        return '0',key

    def fist_node(self,node):
        while True:
            ret = self.judge_key(1)
            print ret
            if ret == '1':
                continue
            elif ret[0] == '0':
                print 'create key success!'
                break
        key = ret[1]
        print key,node,self.id,self.time
        db = GmDB()
        ret = db.update_node(key,node,self.id,self.time)
        print ret

    def second_node(self,node_1,node_2):
        print node_1, node_2
        db = RUN_DB()
        ab = GmDB()
        time, id = self.re_info(node_2)
        pre_key = ab.get_node(node_1)
        prefix_key = pre_key[0].get('key')

        db.create_node(node_2, key, id, time)

    def third_node(self,node_2,node_3):
        print node_3, node_2
        db = RUN_DB()
        ab = GmDB()
        time,id = self.re_info(node_3)

        pre_key = ab.get_node(node_2)
        print pre_key
        db.create_node(node_2, key, id, time)
    def fourth_node(self,node_3,node_4):
        print node_4,node_2
        db = RUN_DB()
        time, id = self.re_info()
        db.create_node(node_2, key, id, time)

    def fist_judge_node(self):
        for key in NODE_INFO:
            db = RUN_DB()
            ab = GmDB()
            if ab.get_node(key) == ():
                time,id = self.re_info()
                ret = db.create_node(key,NODE_INFO[key],id,time)
        print 'create node sueecss!'

if __name__=="__main__":
    a = update_info()
    #a.fist_judge_node()

    node_1 = data_test[6]  # 第一个节点，项目
    node_2 = data_test[4]  # 第二个节点，地区
    node_3 = data_test[5]  # 第三个节点，vpc
    #node_4 = data_test[2]
    str = data_test[2].split(r'.')
    node_4 = str[0]+'.'+str[1]+'.'+'0'+'.'+'0' # 第四个节点，交换机
    judge_node(node_1,node_2,node_3,node_4)


