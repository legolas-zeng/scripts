# coding=utf-8
# @author: zenganiu
# @time: 2019/3/30 15:10

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.displayimage()
        self.displaylabel()

    def initUI(self):
        
        self.setGeometry(300, 300, 1046, 700)
        self.setWindowTitle('自动安装程序')
        self.setWindowIcon(QIcon('C:\\Users\Administrator\Desktop\printer\print.ico'))
        
    def displayimage(self):
        self.lbl1 = QLabel(self)
        self.pix = QPixmap('C:\\Users\Administrator\Desktop\printer\\2019.gif')
        self.lbl1.setPixmap(self.pix)
        self.lbl1.move(0, 0)
        
    def displaylabel(self):
        self.lbl2 = QLabel('请选择你要使用的打印机：', self)
        self.lbl2.move(10, 590)
        
    def displaybutton(self):
        pass
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())