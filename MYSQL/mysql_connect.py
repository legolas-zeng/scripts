# coding=utf-8

import pymysql
from scrapy_web import settings


class Rrjc_DB(object):

    def __init__(self, db='default'):
        self.host = "192.168.3.5"
        self.port = "3306"
        self.passwd = "qq1005521"
        self.user = "zwa"
        self.db = "test2"
        self.cursor = self.conn()

    def conn(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.db,
                                    charset="utf8", cursorclass=pymysql.cursors.DictCursor)
        self.cor = self.conn.cursor()
        return self.cor

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert_one(self, sql):
        result = self.cursor.execute(sql)
        self.conn.commit()
        return result

    def insert_long_one(self, sql, params):
        result = self.cursor.execute(sql, params)
        self.conn.commit()
        return result

    # 插入多条数据
    def insert_many(self, sql, datas):
        result = self.cursor.executemany(sql, datas)
        self.conn.commit()
        return result

    # 更新数据
    def update(self, sql):
        result = self.cursor.execute(sql)
        self.conn.commit()
        return result

    # 关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()

    def one_query(self, sql):
        self.cursor.execute(sql)
        return self.cursor

def main():
    sql1 = """INSERT INTO `anvilgroup` (`id`, `url`, `url_object_id`, `title`) VALUES ('{0}','{1}','{2}','{3}') """.format('3','etcd','8da8s8',"\\\\")
    print(sql1)
    sql2 = """ SELECT * FROM `anvilgroup`"""
    conn = Rrjc_DB()
    # result = conn.insert_one(sql1)
    result = conn.query(sql2)
    print(result)
    conn.close()

if __name__ == '__main__':
    main()
