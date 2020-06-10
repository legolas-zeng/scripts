# coding=utf-8
# @author: zwa❤lqp
# @time: 2020/6/1 20:49

import xlrd, os, shutil, time,json,time,re,ssl,json
from multiprocessing import Pool
import requests
import pymysql
import urllib.request as urllib2

xls_path = "C:\\Users\Administrator.000\Desktop\\JiuLianShanLibrary.xlsx"
headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

class Rrjc_DB(object):

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.passwd = 'qq1005521'
        self.user = 'root'
        self.db = 'movie'
        self.cursor = self.conn()

    def conn(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.db,
                                    charset="utf8", cursorclass=pymysql.cursors.DictCursor)
        self.cor = self.conn.cursor()
        return self.cor


    def insert_one(self, sql):
        result = self.cursor.execute(sql)
        self.conn.commit()
        return result
    def close(self):
        self.cursor.close()
        self.conn.close()

def read_xls(xls_path):
    data = xlrd.open_workbook(xls_path)
    table = data.sheets()[0]  # 通过索引顺序获取工作表
    for i in range(4811,5170):
        print('图书的ISBN号码：', table.row_values(i)[:1][0])
        getinfo(table.row_values(i)[:1][0],i)
        time.sleep(1)

def getinfo(isbn,i):
    try:
        host = 'https://jisuisbn.market.alicloudapi.com'
        path = '/isbn/query'
        method = 'ANY'
        appcode = '050687e2a6b84ac1a7fd280c8aafa4ba'
        #appCode = '853da7ee8c334ac0b293bbd812473b42','b8ba9d0f2f294329850e3956048c1e32','627300f68c00416bab6ffbefdf02da3c'

        querys = 'isbn='+isbn
        bodys = {}
        url = host + path + '?' + querys

        bodys[''] = ""
        post_data = bodys['']
        request = urllib2.Request(url)
        request.add_header('Authorization', 'APPCODE ' + appcode)
        # 根据API的要求，定义相对应的Content-Type
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        response = urllib2.urlopen(request, context=ctx)
        content = response.read()
        if (content):
            handle_data(content, i, isbn)
    except Exception as e:
        print(e)
        storage_data(i, '没有返回数据', isbn)


def handle_data(bookinfo,i,isbn):
    strs = bookinfo.decode()
    jsons = json.loads(strs)
    str = jsons.get('result').get('pubdate')
    result = re.findall('\d\d\d\d', str)
    if result == []:
        print('没有查询到出版日期')
        storage_data(i,'没有查询到出版日期',isbn)
    else:
        print("第{0}本书的出版日期：{1}".format(i,result[0]))
        storage_data(i,result[0],isbn)

def storage_data(i,info,isbn):
    querys = Rrjc_DB()
    sql = "INSERT INTO jiulianshan2 (`book`,`riqi`,`isbn`)VALUES('%s','%s','%s');" % (i, info,isbn)
    print(sql)
    data = querys.insert_one(sql)
    print(data)
    querys.close()

if __name__ == "__main__":
    read_xls(xls_path)
    # getinfo("9787514319729", 1234)
