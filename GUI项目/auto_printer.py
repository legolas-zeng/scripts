# coding=utf-8
# @author: zenganiu
# @time: 2019/3/27 0:16

import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import platform,time,easygui
from subprocess import getstatusoutput as gso

FONT_1 = ('微软雅黑', 14, 'normal')
FONT_2 = ('Arial', 12, 'normal')
PRINTER = {
    '1' : ["西面的公共打印机","192.168.23.238","FX DocuCentre-VI C4471 PCL 6"],
    '2' : ["南面的打印机","192.168.23.239","FX DocuCentre-VI C4471 PCL 6"],
    '3' : ["东面的财务打印机","192.168.23.237","FX ApeosPort-V 3060 PCL 6"],
}

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.master = master # 主Frame
        self.pack()
        self.createimage()
        self.createlabel()
        self.createtext()
        self.mainloop()

    def createimage(self):
        self.canvas = tk.Canvas(self.master,height=577,width=1046)   # 定义顶部的image Frame
        self.photo = tk.PhotoImage(file="D:\printer\conf\\2019.gif")
        # self.imgLabel = tk.Label(self.frame1, image=self.photo)
        # self.imgLabel.pack(side=TOP)
        self.canvas.create_image(0,0,anchor='nw',image=self.photo)
        self.canvas.pack(side=TOP)

    def createlabel(self):
        self.v = tk.StringVar()
        self.v.set(1) # 默认选择第一个
        self.frame2 = tk.Frame(self.master)   # 定义底下的Frame
        self.lb = Label(self.frame2, text='请选择你想使用的打印机：', font=FONT_1).grid(row=0, sticky=W)
        # self.lb.pack(side=LEFT)
        self.btndel = ttk.Button(self.frame2, text="开始安装", command=self.heandle).grid(row=4, column=1)
        r1 = ttk.Radiobutton(self.frame2, text=PRINTER.get('1')[0], variable=self.v, value='1')
        r1.grid(row=2, column=0,sticky=W)

        r2 = ttk.Radiobutton(self.frame2, text=PRINTER.get('2')[0], variable=self.v, value='2')
        r2.grid(row=3, column=0,sticky=W)

        r3 = ttk.Radiobutton(self.frame2, text=PRINTER.get('3')[0], variable=self.v, value='3')
        r3.grid(row=4, column=0,sticky=W)

        # self.text = Text(self.frame2,width=60,height=10)
        #
        # self.text.grid(row=1,rowspan=4, column=4,ipadx=10)

        self.frame2.pack(side=LEFT)
    def createtext(self):
        self.frame3 = tk.Frame(self.master)
        self.text = Text(self.frame3, width=60, height=7)
        self.text.grid()
        self.frame3.pack()

    '''
    rundll32 printui.dll,PrintUIEntry /dl /n 打印机192.168.23.238 /q
    '''
    def heandle(self):
        add_port = "Cscript C:\Windows\System32\Printing_Admin_Scripts\zh-CN\Prnport.vbs -a -r IP_%s -h %s -o raw"
        install_printer = "rundll32 printui.dll,PrintUIEntry /if /b 打印机%s /f \"%s\" /r IP_%s /m \"%s\" /z"
        inf_4471 = "\\\\192.168.3.93\\all\打印机\\4471彩机\%s\Software\PCL\\amd64\Simplified_Chinese\\001\FX6BEAL.inf"
        # inf_3060_10 = "\\\\192.168.3.93\\all\打印机\\3060黑白\win10 64\PCL\\amd64\\001\FX6MHAL.inf"
        inf_3060  = "\\\\192.168.3.93\\all\打印机\\3060黑白\%s\cswnd\PCL\\amd64\\001\FX6MHAL.inf"
        sys_info = self.Jud_sys_version()
        v = self.v.get()
        r = self.msg(1,"确定安装%s吗？，此操作会将之前安装的打印机覆盖。"%(PRINTER.get(v)[0]))
        # r = messagebox.askokcancel('消息框', "确定安装%s吗？"%(PRINTER.get(v)[0]))
        ip = PRINTER.get(v)[1]
        self.pc_data = self.Jud_sys_version()
        if r :
            retcode, output = gso(add_port % (ip, ip))
            print(add_port % (ip, ip))
            self.text.insert(INSERT, "已创建/更新端口%s\n端口添加成功！！\n" % (ip))
            self.text.insert(INSERT, "开始执行安装程序.....\n")
            if retcode == 0:
                if v == '1' or v == '2':
                    inf_path = inf_4471%(sys_info.get('version')+' '+sys_info.get('machine'))
                    # time.sleep(2)
                    retcode1,output1 = gso(install_printer%(ip,inf_path,ip,PRINTER.get(v)[2]))
                    # print(install_printer%(ip,inf_path,ip,PRINTER.get(v)[2]))
                    if retcode1 == 0:
                        self.text.insert(INSERT, "安装程序开始执行，后台服务安装中,请稍后......\n")
                        # time.sleep(5)
                        self.text.insert(INSERT, "安装程序完成\n")
                        # easygui.msgbox('安装完成', image ='D:\printer\conf\ye.png')
                    else:
                        self.text.insert(INSERT,"安装程序出错，请联系管理员！！！！")
                if v == '3':
                    inf_path = inf_3060 % (sys_info.get('version') + ' ' + sys_info.get('machine'))
                    retcode1, output1 = gso(install_printer % (ip, inf_path, ip, PRINTER.get(v)[2]))
                    if retcode1 == 0:
                        self.text.insert(INSERT, "安装程序开始执行，后台服务安装中,请稍后......\n")
                        self.text.insert(INSERT, "安装程序完成\n")

                    else:
                        self.text.insert(INSERT, "安装程序出错，请联系管理员！！！！")
            else:
                self.text.insert(INSERT, "\n端口%s添加失败，请联系管理员！！！！" % (ip))


    def msg(self,*args):
        value,txt = args
        if value == 1:
            r = messagebox.askokcancel('消息框', txt)
        else:
            r = messagebox.showerror('消息框', '安装程序出错，请联系管理员！！！！')
        return r

    def Jud_sys_version(self):
        version = ''
        if 'Windows-10' in platform.platform():
            version = 'win10'
        elif 'Windows-7' in platform.platform():
            version = 'win7'
        machine = platform.architecture()[0][:2]
        data = {
            'version' : version,
            'machine' : machine,
        }
        return data

if __name__ == '__main__':
    windows = tk.Tk()
    windows.title('自动安装程序V1.0')
    # windows.geometry('1050x700')
    windows.iconbitmap('D:\printer\conf\\print.ico')
    Application(master=windows)
