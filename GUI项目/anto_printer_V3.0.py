# coding=utf-8
# @Time    : 2020/4/17 11:31
# @Author  : zwa
# @Motto   ：❤lqp

import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import platform,os,zipfile,requests,shutil
from subprocess import getstatusoutput as gso

FONT_1 = ('微软雅黑', 14, 'normal')
FONT_2 = ('Arial', 12, 'normal')
PRINTER = {
    '1' : ["客服打印机","192.168.10.237","FX DocuCentre-VI C4471 PCL 6"],
    '2' : ["前台打印机","192.168.23.238","FX ApeosPort-V 3060 PCL 6"],
    '3' : ["财务打印机","192.168.23.237","FX ApeosPort-V 3060 PCL 6"],
    '4' : ["研发打印机","192.168.23.240","FX DocuCentre-VI C4471 PCL 6"],
}
path = os.getcwd()

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.master = master # 主Frame
        self.path = os.getcwd()
        self.pack()
        self.createimage()
        self.createlabel()
        self.createtext()
        self.mainloop()

    def createimage(self):
        self.canvas = tk.Canvas(self.master,height=577,width=1046)   # 定义顶部的image Frame
        self.photo = tk.PhotoImage(file=self.path+"\conf\\20200.png")
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

        r3 = ttk.Radiobutton(self.frame2, text=PRINTER.get('4')[0], variable=self.v, value='4')
        r3.grid(row=5, column=0, sticky=W)
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
    rundll32 printui.dll,PrintUIEntry /dl /n 打印机xxx.xxx.xxx.xxx /q
    '''
    def heandle(self):
        sys_info = self.Jud_sys_version()
        system_version =  sys_info.get('version')+' '+sys_info.get('machine')
        try:
            add_port = "Cscript C:\Windows\System32\Printing_Admin_Scripts\zh-CN\Prnport.vbs -a -r IP_%s -h %s -o raw"
            install_printer = "rundll32 printui.dll,PrintUIEntry /if /b 打印机%s /f \"%s\" /r IP_%s /m \"%s\" /z"
            v = self.v.get()
            r = self.msg(1,"确定安装%s吗？，此操作会将之前安装的打印机覆盖。"%(PRINTER.get(v)[0]))
            # r = messagebox.askokcancel('消息框', "确定安装%s吗？"%(PRINTER.get(v)[0]))
            ip = PRINTER.get(v)[1]
            self.pc_data = self.Jud_sys_version()
            if r :
                retcode, output = gso(add_port % (ip, ip))
                print("添加端口命令：", add_port % (ip, ip))
                if jud_samba():
                    inf_3060 = "\\\\192.168.3.93\\all\打印机\\3060黑白\%s\cswnd\PCL\\amd64\\001\FX6MHAL.inf"
                    inf_4471 = "\\\\192.168.3.93\\all\打印机\\4471彩机\%s\Software\PCL\\amd64\Simplified_Chinese\\001\FX6BEAL.inf"
                else:
                    inf_3060 = path + "\print\%s\PCL\\amd64\\001\FX6MHAL.inf"
                    inf_4471 = path + "\print\%s\KOAYTJ__.INF"
                    self.text.insert(INSERT, "已创建/更新端口%s\n端口添加成功！！\n" % (ip))
                    judge_info = judge()
                    self.text.insert(INSERT, judge_info)
                    downloaDriveInfo = downloaDrive(system_version, v)
                    self.text.insert(INSERT, downloaDriveInfo)
                    unzipFileInfo = unzipFile(path + "\print.zip", path + "\print")
                    self.text.insert(INSERT, unzipFileInfo)
                    self.text.insert(INSERT, "开始执行安装程序.....\n")
                if retcode == 0:
                    # 安装4471
                    if v == '1' or v == '4':
                        inf_path = inf_4471 % (sys_info.get('version') + ' ' + sys_info.get('machine'))
                        print("inf路径：", inf_path)
                        print("打印命令：", install_printer % (ip, inf_path, ip, PRINTER.get(v)[2]))
                        retcode1, output1 = gso(install_printer % (ip, inf_path, ip, PRINTER.get(v)[2]))
                        if retcode1 == 0:
                            self.text.insert(INSERT, "安装程序开始执行，后台服务安装中,请稍后......\n")
                            self.text.insert(INSERT, "安装程序完成\n")
                            self.text.insert(INSERT, "稍等几分钟后，请打开控制面板查看新的打印机")
                            retcode2, output2 = gso("control")
                        else:
                            self.text.insert(INSERT,"安装程序出错，请联系管理员！！！！")
                    # 安装3060
                    if v == '2' or v == '3' :
                        inf_path = inf_3060 % (sys_info.get('version') + ' ' + sys_info.get('machine'))
                        print("inf路径：",inf_path)
                        print("打印命令：", install_printer % (ip, inf_path, ip, PRINTER.get(v)[2]))
                        retcode1, output1 = gso(install_printer % (ip, inf_path, ip, PRINTER.get(v)[2]))
                        if retcode1 == 0:
                            self.text.insert(INSERT, "安装程序开始执行，后台服务安装中,请稍后......\n")
                            self.text.insert(INSERT, "安装程序完成，\n")
                            self.text.insert(INSERT, "稍等几分钟后，请打开控制面板查看新的打印机")
                            retcode2, output2 = gso("control")
                        else:
                            self.text.insert(INSERT, "安装程序出错，请联系管理员！！！！")
                else:
                    self.text.insert(INSERT, "\n端口%s添加失败，请联系管理员！！！！" % (ip))
        except Exception:
            print(Exception)


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
        print(data)
        return data

def jud_samba() -> bool:
    if os.path.exists("\\\\192.168.3.93\\all\打印机\\3060黑白\win10 64\PCL\\amd64\\001\FX6MHAL.inf"):
        print("使用共享文件")
        return True
    else:
        print("使用http")
        return False


def downloaDrive(systemVersion:str,printModel:str) -> str:
    # print(systemVersion,printModel)
    if systemVersion == "win7 64":
        if printModel != "1":
            url = "http://192.168.3.5/download/%E6%89%93%E5%8D%B0%E6%9C%BA/3060%E9%BB%91%E7%99%BD/win7%2064.zip"
        elif printModel == "1":
            url = "http://192.168.3.5/download/%E6%89%93%E5%8D%B0%E6%9C%BA/c640e%E5%BD%A9%E6%9C%BA/win7%2064.zip"
    elif systemVersion == "win10 64":
        if printModel != "1":
            url = "http://192.168.3.5/download/%E6%89%93%E5%8D%B0%E6%9C%BA/3060%E9%BB%91%E7%99%BD/win10%2064.zip"
        elif printModel == "1":
            url = "http://192.168.3.5/download/%E6%89%93%E5%8D%B0%E6%9C%BA/c640e%E5%BD%A9%E6%9C%BA/win10%2064.zip"
    zipPath = path + "\print.zip"
    r = requests.get(url)
    try:
        with open(zipPath, "wb") as code:
            code.write(r.content)
    except Exception:
        return "驱动下载错误。请联系运维！\n"
    return "驱动下载成功！\n"

def judge () -> str:
    try:
        if os.path.exists(path + "\print.zip"):
            os.remove(path + "\print.zip")
        if os.path.exists(path + "\print"):
            shutil.rmtree(path + "\print",True)
    except Exception:
        return "环境清理失败!\n"
    return "环境清理完成!\n"


def unzipFile(zip_src:str, dst_dir:str) -> str:
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
        return "驱动解压完成！\n"
    else:
        print('This is not zip')
        return "驱动解压失败！\n"


if __name__ == '__main__':
    windows = tk.Tk()
    windows.title('自动安装程序V3.0')
    windows.geometry('800x720')
    windows.iconbitmap(path+'\conf\\print.ico')
    Application(master=windows)
