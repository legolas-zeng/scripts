# -*-coding:utf-8 -*-
import uiautomator
from uiautomator import device as d
import time,os,re
import subprocess,shutil
from PIL import Image, ImageDraw

#d = uiautomator.Device('F7J4C16119006229')
nowtime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
screenshot_backup_dir = 'screenshot_backups/'

if not os.path.isdir(screenshot_backup_dir):
    os.mkdir(screenshot_backup_dir)

# os.popen('adb shell uiautomator dump /sdcard/ui.xml')
# os.popen("adb pull /sdcard/ui.xml " + screenshot_backup_dir)

# print d.info
def _get_screen_size():
    size_str = os.popen('adb shell wm size').read()
    print size_str
    if not size_str:
        print('请安装ADB及驱动并配置环境变量')
        sys.exit()
    m = re.search('(\d+)x(\d+)', size_str)
    if m:
        width = m.group(1)
        height = m.group(2)
        print "{height}x{width}".format(height=height, width=width)
        return "{height}x{width}".format(height=height, width=width)
def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system("adb pull /sdcard/autojump.png "+ screenshot_backup_dir)
    shutil.move('F:\scripts\screenshot_backups\\autojump.png','F:\scripts\screenshot_backups\%s.png'%nowtime)

def find_like(im):
    w, h = im.size
    like_y = 0
    im_pixel = im.load()
    print w,h
    # 从右开始寻找点赞,点赞颜色为(133, 147, 176, 255)，
    for i in range(like_y, int(h)):
        for j in range(w*4/5, int(w)):
            pixel = im_pixel[j, i]
            print pixel
            if (130 < pixel[0] < 135) and (143 < pixel[1] < 150) and (172 < pixel[2] < 180):
                piece_x_sum += j
                piece_x_c += 1
                piece_y_max = max(i, piece_y_max)
def click_screen(x,y):
    pass
def slide_screen():
    pass
def main():
    im = Image.open('./screenshot_backups/2018-03-23-16-06-22.png')
    find_like(im)

main()



