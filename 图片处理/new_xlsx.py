# coding=utf-8
import xlsxwriter
from PIL import Image

def ten_sixteen(rang):
    tar = hex(rang)
    return tar

def Joining(R,G,B):
    R = ten_sixteen(R)[2:4]
    G = ten_sixteen(G)[2:4]
    B = ten_sixteen(B)[2:4]
    req = R+G+B
    return req

def creta_table():
    workbook = xlsxwriter.Workbook('C:\Users\Administrator\Desktop\zm6.xlsx')
    table_name = 'sheet1'
    worksheet = workbook.add_worksheet(table_name)
    format_title=workbook.add_format()    #定义format格式对象

    im = Image.open("C:\Users\Administrator\Desktop\hsq.png")
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    for x in range(width):
        for y in range(height):
            print x, y
            colour = pix[x, y][0:3]
            R = colour[0]
            G = colour[1]
            B = colour[2]
            colour_code = Joining(R,G,B)
            print colour_code

            format_title.set_bg_color(colour_code)
            worksheet.write_row(x,y,' ',format_title) # 如果指定行还可以加 字符型A1之类的。

    workbook.close()

creta_table()
