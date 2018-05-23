# coding=utf-8
import xlwt

book = xlwt.Workbook()

xlwt.add_palette_colour("custom_colour", 0x21)
book.set_colour_RGB(0x21, 251, 228, 228)

sheet1 = book.add_sheet('Sheet 1')
style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
sheet1.write(0,0,'',style)
sheet1.write(0,1,'',style) # 第一个是纵坐标，第二个是横坐标

#book.save('test.xls')