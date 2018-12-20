# coding=utf-8
import xlrd

excel_path = "C:\\Users\Administrator\Desktop\movie_info.xlsx"

def read_xls(file_names,col):
    data = xlrd.open_workbook(file_names)
    table = data.sheets()[0]  # 通过索引顺序获取工作表
    # data_sum = {}
    # table.col_values(1) #获取整列
    # print(table.name)
    # print(table.nrows, table.ncols)
    # print 'Subject code:',table.row_values(1)  # 获取科目代码
    print('Subject code value:',table.col_values(col)) # 获取第三列的值
    # print(table.cell(1,1).value) # 获取B2
    print(type(table.col_values(col)))
    return table.col_values(col)

# read_xls(excel_path,2)



