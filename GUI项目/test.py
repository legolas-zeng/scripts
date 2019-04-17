# coding = utf-8
import platform,easygui,os
from subprocess import getstatusoutput as gso
from PIL import Image,ImageTk
import tkinter as tk

# 简单插入显示
# def show_jpg():
#     root = tk.Tk()
#     im=Image.open("D:\printer\conf\ye.png")
#     img=ImageTk.PhotoImage(im)
#     imLabel=tk.Label(root,image=img).pack()
#     root.mainloop()
#
# if __name__ == '__main__':
#     show_jpg()

path = os.getcwd()
print(path)

retcode2,output2 = gso("control")
