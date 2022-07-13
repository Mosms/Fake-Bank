##操作excel必要引入的包
import xlrd
import xlwt
import xlutils
##操作excel必要引入的包

from PyQt6.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)
from PyQt6.QtGui import *
import sys
#import os.path
#import sip


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("./Pic/background.png"))#设置窗口背景图片，平铺到整个窗口，随着窗口的变化而变化

    def center(self):
        """centers the window on the screen"""
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.setFixedSize(700, 450)
        self.center()
        self.setWindowTitle("珐剋ATM")

        self.Get_qbtn()
        self.Get_libtn()
        self.Get_lubtn()
        self.show()


    def Setfont(self, button, size):
        nowFont = button.font()
        nowFont.setFamily('楷书')
        nowFont.setPointSize(size)
        nowFont.setBold(True)
        button.setFont(nowFont)

    def Get_qbtn(self):
        quit_btn = QPushButton('关闭', self)
        quit_btn.setFixedSize(80, 40)
        #quit_btn.setStyleSheet("background: white")
        self.Setfont(quit_btn, 15)
        #quit_btn.setStyleSheet("color: red")
        quit_btn.clicked.connect(QApplication.instance().quit)
        quit_btn.move(600, 386)

    def Get_libtn(self):
        login_btn = QPushButton('登录', self)
        login_btn.setFixedSize(100, 40)
        self.Setfont(login_btn, 16)
        login_btn.clicked.connect(self.Login)
        login_btn.move(300, 180)
    def Get_lubtn(self):
        logup_btn = QPushButton('注册', self)
        logup_btn.setFixedSize(100, 40)
        # login_btn.setStyleSheet("background: white")
        # quit_btn.setStyleSheet("color: red")
        self.Setfont(logup_btn, 16)
        logup_btn.clicked.connect(self.Logup)#此处要传入的是函数指针，而不是函数本身，相当于传入函数名即可
        logup_btn.move(300, 240)


    def Login(self):
        QApplication.instance().quit()

    def Logup(self):
        QApplication.instance().quit()
        #这里主要需要改变页面布局#进行的是对文档的操作

        """okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)"""


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()