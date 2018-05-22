# coding=utf-8
from PIL import Image

# 打开要处理的图像
img_src = Image.open('C:\Users\Administrator\Desktop\hsq.jpg')

# 转换图片的模式为RGBA
img_src = img_src.convert('RGBA')

# 获得文字图片的每个像素点
src_strlist = img_src.load()

# 100,100 是像素点的坐标
data = src_strlist[100, 100]

print data
