##操作excel必要引入的包
import xlrd
import xlwt
import xlutils
import xlwings as xw
##操作excel必要引入的包

from PyQt6 import sip
from PyQt6.QtWidgets import (QWidget, QPushButton, QLayout, QGridLayout, QApplication, QLineEdit, QInputDialog)
from PyQt6.QtGui import *
import sys


#import os.path

class FakeBank(QWidget):
    def __init__(self):
        super().__init__()
        self.dataCore = xlrd.open_workbook('DataCore.xls').sheet_by_name('core')
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
        self.GetID()
        self.Getpassword()
        self.show()


    def Setfont(self, button, size):
        nowFont = button.font()
        nowFont.setFamily('楷书')
        nowFont.setPointSize(size)
        nowFont.setBold(True)
        button.setFont(nowFont)

    def Get_qbtn(self):
        self.quit_btn = QPushButton('关闭', self)
        self.quit_btn.setFixedSize(80, 40)
        #quit_btn.setStyleSheet("background: white")
        self.Setfont(self.quit_btn, 15)
        self.quit_btn.clicked.connect(QApplication.instance().quit)
        self.quit_btn.move(600, 386)

    def Get_libtn(self):
        self.login_btn = QPushButton('登录', self)
        self.login_btn.setFixedSize(100, 40)
        self.Setfont(self.login_btn, 16)
        self.login_btn.clicked.connect(self.Login)
        self.login_btn.move(240, 280)
    def Get_lubtn(self):
        self.logup_btn = QPushButton('注册', self)
        self.logup_btn.setFixedSize(100, 40)
        self.Setfont(self.logup_btn, 16)
        self.logup_btn.clicked.connect(self.Logup)#此处要传入的是函数指针，而不是函数本身，相当于传入函数名即可
        self.logup_btn.move(360, 280)
    def GetID(self):
        self.IDnumber = QPushButton('IDnumber', self)
        self.IDnumber.move(200, 160)
        self.IDnumber.resize(80, 30)
        self.IDnumber.clicked.connect(self.nullDo)
        self.IDinput = QLineEdit(self)
        self.IDinput.move(320, 160)
        self.IDinput.resize(180, 30)
    def Getpassword(self):
        self.password = QPushButton('Password', self)
        self.password.move(200, 210)
        self.password.resize(80, 30)
        self.password.clicked.connect(self.nullDo)
        self.Inpassword = QLineEdit(self)
        self.Inpassword.move(320, 210)
        self.Inpassword.resize(180, 30)

    def nullDo(self):
        self.show()


    def Login(self):
        nowID = self.IDinput.text()
        nowPassword = self.Inpassword.text()
        Rem = -1
        for cor in range(int(self.dataCore.cell_value(0, 0))):
            if nowID == self.dataCore.cell_value(cor + 1, 2):#从第二行开始的记录要注意这点
                if Rem < 0:
                    Rem = cor
                else:
                    print("Error")
                    QApplication.instance().quit
        if Rem < 0:
            text, ok = QInputDialog.getText(self, 'Finding no this ID', 'Enter your ID again:')
            if ok:
                self.IDinput.setText(str(text))
            return
        else:
            if nowPassword == self.dataCore.cell_value(Rem + 1, 3):  # 从第二行开始的记录要注意这点
                if self.dataCore.cell_value(Rem + 1, 3) == "Admin":
                    print(1)
                else:#此处工作为将其代替为相应的函数#I am here
                    print(2)
            else:
                text, ok = QInputDialog.getText(self, 'Password error!', 'Enter your password again:')
                if ok:
                    self.Inpassword.setText(str(text))
                return

    def Logup(self):#所有更改适用xw
        app = xw.App(visible=False, add_book=False)
        wb = app.books.add()
        wb = app.books.open('DataCore.xls')
        wb.sheets['core'][0, 0].value = str(int(self.dataCore.cell_value(0, 0)) + 1)
        print(wb.sheets['core'][0, 0].value)
        wb.save()
        wb.close()#save 然后关闭 之后的更改均可如此
        app.quit()
        print(1)

def main():

    app = QApplication(sys.argv)
    bank = FakeBank()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()