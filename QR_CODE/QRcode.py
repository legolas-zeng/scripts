# coding=utf-8
from MyQR import myqr
import os
version, level, qr_name =  myqr.run(
    words='https://u.wechat.com/EDhQ6U8TDW2UYREvz1c3KI8',         #在命令后输入链接或者句子作为参数，然后在程序的当前目录中产生相应的二维码图片文件，默认命名为” qrcode.png“
    version=1,                   #设置容错率为最高默认边长是取决于你输入的信息的长度和使用的纠错等级；而默认纠错等级是最高级的H
    level='H',                   #控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture='F:\下载\\maozhua.gif',         #用来将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片
    colorized=True,              #可以使产生的图片由黑白(False)变为彩色(True)的
    contrast=1.0,                #用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
    brightness=1.0,              #用来调节图片的亮度，其余用法和取值与 -con 相同
    save_name='qiuping7.gif',        #控制文件名，格式可以是 .jpg， .png ，.bmp ，.gif ；
    save_dir=os.getcwd()         #控制位置。
)

print(version,level,qr_name)

print('1111111')