# coding=utf-8

import xlwt,xlrd
import os
import numpy as np

xls_path = 'C:\Users\Administrator.000\Desktop\\xiaojiejie'


def file_name(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        for file in files:
            # print(os.path.join(root, file).decode('gbk').encode('utf-8'))
            file_list.append(os.path.join(root, file))
    # print(file_list)
    return file_list


def read_xls(file_names):
    data = xlrd.open_workbook(file_names)
    table = data.sheets()[0]  # 通过索引顺序获取工作表
    data_sum = {}
    # table.col_values(i) #获取整列
    # print(table.name)
    # print(table.nrows, table.ncols)
    # print 'Subject code:',table.row_values(3)[:1]   # 获取科目代码
    # print 'Subject code value:',table.row_values(3)[3:] # 获取第三列的值
    # print(table.cell(1,1).value) # 获取B2
    for i in range(2,int(table.nrows)):
        for code in table.row_values(i)[:1]:
            # print code,table.row_values(i)[3:]
            data_sum[code] = table.row_values(i)[3:]
    return data_sum
def handle_data(data):
    for k,v in data.iteritems():
        print k,v
def creat_xls(dic):
    header = [u'科目代码', u'科目名称', u'币别', u'期初借方余额', u'期初贷方余额', u'本期借方发生额', u'本期贷方发生额', u'本年借方累计', u'本年贷方累计', u'期末借方余额', u'期末贷方余额',]
    name = {'1002':u'银行存款','1002.01':u'众财6856','1122':u'应收账款','1221':u'其他应收款','1221.01':u'员工社保','1221.02':u'员工公积金',
            '1221.03':u'深圳市众财商务信息咨询有限公司','2211':u'应付职工薪酬','2221':u'应交税费','2221.02':u'应交增值税（销项税）','2221.03':u'应交个人所得税',
            '2221.04':u'应交所得税','2241':u'其他应付款','2241.01':u'许文斌','2241.02':u'员工','4103':u'本年利润','6001':u'主营业务收入','6403':u'营业税金及附加',
            '6602':u'管理费用','6602.01':u'工资','6602.02':u'社保','6602.03':u'公积金','6602.05':u'工会经费','6603':u'财务费用',}
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet(u'科目余额表',cell_overwrite_ok=True)
    i = 0
    for each_header in header:
        worksheet.write(0, i, each_header)
        i += 1
    j = 1
    for k,v in dic.iteritems():
        worksheet.write(j, 0, k)
        x = 3
        for val in v:
            worksheet.write(j,x,str(val))
            x +=1
        j +=1
    first_col = worksheet.col(3)  # xlwt中是行和列都是从0开始计算的
    first_col.width = 256 * 18
    workbook.save('C:\Users\Administrator.000\Desktop\\xiaojiejie\Excel_test.xls')

def main():
    file_name_list = file_name(xls_path)
    dic = {}
    for file_names in file_name_list:
        dica = read_xls(file_names)
        for key in dica:
            if dic.get(key):
                a = np.array(dica[key])
                b = np.array(dic[key])
                s = a + b
                dic[key] = s.tolist()
            else:
                dic[key] = dica[key]
        for key in dic:
            if dica.get(key):
                pass
            else:
                dic[key] = dic[key]
    print dic
    creat_xls(dic)


if __name__ == '__main__':
    main()
