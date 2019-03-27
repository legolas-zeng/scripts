# coding=utf-8
# @author: zenganiu
# @time: 2019/3/27 0:16

import tkinter as tk
from tkinter import *

FONT_1 = ('微软雅黑', 14, 'normal')
FONT_2 = ('Arial', 12, 'normal')

# 主窗体
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.pack()
        self.createimage()
        self.createlabel()
        self.createRadiobutton()
        self.createbutton()
        self.mainloop()

    def createimage(self):
        self.frame1 = tk.Frame()
        self.photo = tk.PhotoImage(file="D:\\2019.gif")
        self.imgLabel = tk.Label(self.frame1, image=self.photo)
        self.imgLabel.pack(side=RIGHT)
        self.frame1.pack(side=TOP, fill=X)

    def createlabel(self):
        self.frame2 = tk.Frame()
        self.frame2.pack(side=TOP, fill=X)
        self.lb = Label(self.frame2, text='请选择你想使用的打印机：', font=FONT_1)
        self.lb.pack(side=LEFT)

    def createRadiobutton(self):
        LANGS = [
            ('西面的公共打印机', 1),
            ('南面的打印机', 2),
            ('东面的财务打印机', 3)]
        self.v = tk.IntVar()
        self.v.set(1)
        for lang, num in LANGS:
            b = Radiobutton(self.master, text=lang, variable=self.v, value=num)
            b.pack(anchor=W)

    def createbutton(self):
        self.frame3 = tk.Frame()
        self.frame3.pack()
        self.btndel = Button(self.frame3,
                    text="清空",
                    command=self.heandle,
                    bg='gray').grid(row=3,
                                    column=3)


    def heandle(self):
        print('-------')


if __name__ == '__main__':
    windows = tk.Tk()
    windows.title('自动安装程序V1.0')
    windows.geometry('1050x700')
    windows.iconbitmap('D:\\print.ico')
    app = Application(master=windows)
