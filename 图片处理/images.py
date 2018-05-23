# coding=utf-8
from PIL import Image
import xlwt

book = xlwt.Workbook()
xlwt.add_palette_colour("custom_colour", 0x21)

im = Image.open("C:\Users\Administrator\Desktop\hsq.png")
sheet1 = book.add_sheet('Sheet 1')
pix = im.load()
width = im.size[0]
height = im.size[1]

for x in range(width):
    for y in range(height):
        print x,y
        colour = pix[x,y][0:3]
        R = colour[0]
        G = colour[1]
        B = colour[2]
        book.set_colour_RGB(0x21, R, G, B)
        style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
        sheet1.write(x, y, '', style)

book.save('test.xls')
