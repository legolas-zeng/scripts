# coding=utf-8

import xlwt,xlrd
import os

xls_path = 'C:\\Users\Administrator\Desktop\\xiaojiejie'


def file_name(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        for file in files:
            # filename = file.decode('gbk').encode('utf-8')
            # print filename
            print(os.path.join(root, file).decode('gbk').encode('utf-8'))
            file_list.append(os.path.join(root, file))
    print(file_list)
    return file_list


def read_xls():
    data = xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\xiaojiejie\\\xc9\xcf\xc8\xc4\xd2\xbb\xb5\xea\xbf\xc6\xc4\xbf\xd3\xe0\xb6\xee\xb1\xed.xls')
    table = data.sheets()[0]  # 通过索引顺序获取工作表
    # table.row_values(i) #获取整行
    # table.col_values(i) #获取整列
    print(table.name)
    print(table.nrows, table.ncols)
    print table.row_values(3)[3:] # 获取第三列的值
    print(table.cell(1,1).value) # 获取B2

def creat_xls():
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(1, 0, label='this is test')
    workbook.save('Excel_test.xls')

# file_name(xls_path)
read_xls()