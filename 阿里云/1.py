import hashlib,time,uuid,random
import db_test

def test_1():
    pwd = '10.7.0.0'
    id = uuid.uuid4()
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print nowtime,id
test_1()

DB_INFO = {'user':'jumpserver',
           'host':'192.168.1.202',
           'pwd':'z1P98EDggNE19bcl0I23rGhR',
           'dbname':'jumpserver',
           'port':3306,}

class GmDB(object):
    def __init__(self):
        self.host = DB_INFO.get('host')
        self.user = DB_INFO.get('user')
        self.pwd = DB_INFO.get('pwd')
        self.dbname = DB_INFO.get('dbname')
        self.port = DB_INFO.get('port')
        self._conn = self.db_conn()
    def db_conn(self):
        conn = db_test.CDataBase(self.host, self.user, self.pwd,
                         self.dbname, self.port)
        return conn
    def get_test(self,count):
        #sql = "select `key` from assets_node WHERE `value` = 'hk-test';"
        #sql = "select `key` from assets_node group by `key`;"
        sql = "select `key` from assets_node where LENGTH(`key`)<%s and LENGTH(`key`)>%s;"%(10*int(count),5*int(count))
        print sql
        ret = self._conn.select_sql(sql, ())
        return ret
def create_key(count):
    str2 = random.randint(0, 10)
    key2 = "[{}]:[{}]".format('0', str2)
    print key2
    return key2
def judge_key(count):
    a = GmDB()
    key = create_key(count)
    for info in a.get_test(count):
        print info.get('key')
        if info.get('key') == key:
            return '1'
    return '0',key
if __name__ == '__main__':
    while True:
        ret = judge_key(1)
        print ret
        if ret == '1':
            print 'error'
            continue
        elif ret[0] == '0':
            print 'success'
            break








