# coding=utf-8
# @author: zwa❤lqp
# @time: 2020/6/1 20:49

import xlrd, os, shutil, time,json,time,re
from multiprocessing import Pool
import requests


xls_path = "C:\\Users\Administrator\Desktop\\JiuLianShanLibrary.xlsx"
headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

def read_xls(xls_path):
    data = xlrd.open_workbook(xls_path)
    table = data.sheets()[0]  # 通过索引顺序获取工作表
    for i in range(table.nrows):
        print('图书的ISBN号码：', table.row_values(i)[:1][0])
        getinfo(table.row_values(i)[:1][0],i)
        time.sleep(1)

def getinfo(isbn,i):
    try:
        isbn = str(isbn)
        url = 'http://book.feelyou.top/isbn/'
        url = url+isbn
        print('Getting information from', url, '……')
        result = requests.get(url)
        handle_data(result.json(),i)
    except Exception as e:
        print(e)


def handle_data(bookinfo,i):
    str = bookinfo.get('abstract')
    result = re.findall('\d\d\d\d-\d*', str)
    print(result)
    if result == []:
        print('没有查询到出版日期')
    else:
        print("第{0}本书的出版日期：{1}".format(i,result[0]))

def creat_xls():
    header = ['出版日期']
    code_data = loadJson()
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('出版信息', cell_overwrite_ok=True)
    i = 0
    for each_header in header:
        worksheet.write(0, i, each_header)  # 写入表头
        i += 1
    j = 1
    for k, v in dic.items():  # python3
        # for k, v in data.iteritems(): # python2
        worksheet.write(j, 0, k)  # 写入行头
        l = code_data.get(k)
        worksheet.write(j, 1, l)  # 写入科目名称
        print(l)
        x = 3
        for val in v:
            worksheet.write(j, x, str(val))  # 写入内容
            x += 1
        j += 1
    first_col = worksheet.col(3)  # xlwt中是行和列都是从0开始计算的
    first_col.width = 256 * 18
    workbook.save('C:\\Users\Administrator.000\Desktop\\xiaojiejie\BaseData\Excel_test.xls')



if __name__ == "__main__":
    info = read_xls(xls_path)
    print(info)
