##操作excel必要引入的包
import xlrd
import xlwt
import xlutils
##操作excel必要引入的包

from PyQt6.QtWidgets import (QWidget, QPushButton,
        QFrame, QApplication)
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


    def initUI(self):

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.resize(100, 100)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Quit button')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()