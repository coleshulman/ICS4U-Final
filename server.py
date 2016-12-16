import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from socket import *
import urllib
import re

class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.title = 'Title'
        self.left = 100
        self.top = 100
        self.width = 620
        self.height = 550
        self.bar = QLineEdit(self)
        self.text_feild = QTextEdit(self)
        self.text_feild.setEnabled(False)
        self.user = 'server'
        self.palette = QPalette()


        # self.check_box = QCheckBox(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.palette.setColor(QPalette.Background, Qt.darkRed)
        self.setPalette(self.palette)
        self.text_feild.setGeometry(10, 5, self.width-20, 450)
        self.text_feild.setAutoFillBackground(True)
        self.text_bar()
        self.show()

    def text_bar(self):
        self.bar.setGeometry(100, 480, 300, 30)
        button = QPushButton('Send', self)
        button.move(400, 480)
        self.bar.returnPressed.connect(self.clear)
        button.clicked.connect(self.clear)

    def clear(self):
        self.text_feild.insertPlainText(self.user+'-'+self.bar.displayText()+'\n')
        self.bar.setText('')


def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

main()
