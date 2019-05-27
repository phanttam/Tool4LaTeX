# coding=utf-8
# tool4latex.py
#
import re, os, sys, csv, codecs, time
# sys.path.insert(0, 'D:/Tool4LaTeX/source')
from datetime import datetime, timedelta
from urllib.request import urlopen
import math, argparse, subprocess, signal, shutil, errno, unicodedata, webbrowser
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from fractions import Fraction
from decimal import Decimal
from def_id import *
from def_bbt import *
from def_convert import *
from def_information import *
from def_ban_quyen import *
from def_calculation import *
from def_matrix import *
from def_bank import *
from def_utilities import *
import src_information
from src_full_graph import *
from src_bbt import *
from src_do_thi import *
from src_id_combo import *
from src_tool_id import *
from src_convert import *
from src_reg import *
from src_matrix import *
from src_bank import *
from src_mix import *
from src_provip import *
from src_apply_id import *
from src_options import *
REG_INF = Registry_Inf_get()

class Test(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group1 = QGroupBox('ID1')
        self.group2 = QGroupBox('ID2')
        self.layout().addWidget(self.group1)
        self.layout().addWidget(self.group2)


class Ui_Form(object):

    def setupUi(self, Form):
        Form.resize(314, 66)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


class Widget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        for i in range(20):
            letter = chr(ord('a') + i)
            checkBox = QCheckBox(('{}').format(i + 1), self)
            self.layout().addWidget(checkBox, i, 0)
            btna = QPushButton(('{}1').format(letter), self)
            btnb = QPushButton(('{}2').format(letter), self)
            self.layout().addWidget(btna, i, 1)
            self.layout().addWidget(btnb, i, 2)


class Tab1(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group1 = QGroupBox('ID1')
        self.group2 = QGroupBox('ID2')
        self.layout().addWidget(self.group1)
        self.layout().addWidget(self.group2)


class Creat_file_tex(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group1 = QGroupBox('ID1')
        self.group2 = QGroupBox('ID2')
        self.layout().addWidget(self.group1)
        self.layout().addWidget(self.group2)


class Draw_Tikz(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group1 = QGroupBox('ID1')
        self.layout().addWidget(self.group1)


class Casio_Tool(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group1 = QGroupBox('ID1')
        self.layout().addWidget(self.group1)


class Word_Tool(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group1 = QGroupBox('ID1')
        self.layout().addWidget(self.group1)


class Page1(QTabWidget):

    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)
        self.title = 'Tool4LaTeX'
        self.left = 50
        self.top = 50
        self.width = 1100
        self.height = 700
        self.setMinimumSize(1100, 700)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setWindowIcon(QIcon('logo.ico'))
        for directory in ('Temp', 'BBT', 'DOTHI', 'Tool_ID', 'CONVERT', 'KHAOSAT',
                          'Bank', 'Matran', 'Setting', 'Mixed Test', 'ProVip'):
            try:
                os.makedirs(directory)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if os.path.exists('Setting//header-footer.tex'):
            codecs.open('Setting//header-footer.tex', 'r+', 'utf-8')
        else:
            with codecs.open('Setting//header-footer.tex', 'w+', 'utf-8') as (f):
                f.write('\\usepackage{fancyhdr}\n\\pagestyle{fancy}\n\\renewcommand{\\headrulewidth}{1pt}\n\\renewcommand{\\footrulewidth}{1pt}\n\\lhead{Trường THPT Trần Hưng Đạo}\n\\chead{}\n\\rhead{Thầy Phan Thanh Tâm}\n\\lfoot{Số điện thoại: 0907991160}\n\\cfoot{}\n\\rfoot{Trang \\thepage}\n')
                f.close()
        self.tab0 = Registry_Inf()
        self.tab1 = Tool_ID()
        self.tab5 = Draw_BBT()
        self.tab6 = Draw_Graph()
        self.tab2 = Convert()
        self.tab7 = Full_Graph()
        self.tab8 = Matrix_Test()
        self.tab9 = Bank()
        self.tab10 = Mix_Test()
        self.tab11 = ProVip()
        self.tab12 = ApplyID()
        self.tab20 = Option()
        if REG_INF == 2:
            self.addTab(self.tab12, 'Gán ID')
            self.addTab(self.tab10, 'Trộn đề')
            self.addTab(self.tab1, 'Công cụ ID')
            self.addTab(self.tab5, 'Bảng biến thiên')
            self.addTab(self.tab6, 'Đồ thị hàm số')
            self.addTab(self.tab7, 'Khảo sát')
            self.addTab(self.tab20, 'Tuỳ chỉnh')
            self.addTab(self.tab0, 'Thông tin')
        else:
            if REG_INF == 3:
                self.addTab(self.tab12, 'Gán ID')
                self.addTab(self.tab10, 'Trộn đề')
                self.addTab(self.tab9, 'Ngân hàng câu hỏi')
                self.addTab(self.tab8, 'Ma trận đề')
                self.addTab(self.tab5, 'Bảng biến thiên')
                self.addTab(self.tab6, 'Đồ thị hàm số')
                self.addTab(self.tab7, 'Khảo sát')
                self.addTab(self.tab1, 'Công cụ ID')
                self.addTab(self.tab2, 'Chuyển đổi')
                self.addTab(self.tab11, 'ProVip')
                self.addTab(self.tab20, 'Tuỳ chỉnh')
                self.addTab(self.tab0, 'Thông tin')
            else:
                if REG_INF == 4:
                    self.addTab(self.tab12, 'Gán ID')
                    self.addTab(self.tab10, 'Trộn đề')
                    self.addTab(self.tab9, 'Ngân hàng câu hỏi')
                    self.addTab(self.tab8, 'Ma trận đề')
                    self.addTab(self.tab5, 'Bảng biến thiên')
                    self.addTab(self.tab6, 'Đồ thị hàm số')
                    self.addTab(self.tab7, 'Khảo sát')
                    self.addTab(self.tab1, 'Công cụ ID')
                    self.addTab(self.tab2, 'Chuyển đổi')
                    self.addTab(self.tab11, 'ProVip')
                    self.addTab(self.tab20, 'Tuỳ chỉnh')
                    self.addTab(self.tab0, 'Thông tin')
                else:
                    if REG_INF == 5:
                        self.addTab(self.tab12, 'Gán ID')
                        self.addTab(self.tab1, 'Công cụ ID')
                        self.addTab(self.tab11, 'ProVip')
                        self.addTab(self.tab10, 'Trộn đề')
                        self.addTab(self.tab8, 'Ma trận đề')
                        self.addTab(self.tab9, 'Ngân hàng câu hỏi')
                        self.addTab(self.tab20, 'Tuỳ chỉnh')
                    else:
                        self.addTab(self.tab0, 'Thông tin')
                        self.addTab(self.tab12, 'Gán ID')
                        self.addTab(self.tab10, 'Trộn đề')
                        self.addTab(self.tab1, 'Công cụ ID')
                        self.addTab(self.tab5, 'Bảng biến thiên')
                        self.addTab(self.tab6, 'Đồ thị hàm số')
                        self.addTab(self.tab7, 'Khảo sát')
                        self.addTab(self.tab20, 'Tuỳ chỉnh')
        self.tab13 = Casio_Tool()
        self.tab14 = Word_Tool()
        if self.currentIndex() == 0:
            self.setGeometry(self.left, self.top, self.width, self.height)
        else:
            self.setGeometry(self.left, self.top, self.width, self.height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    font = app.font()
    font.setPointSize(10)
    app.setFont(font)
    app.setWindowIcon(QIcon('logo.ico'))
    mainwindow = QMainWindow()
    mainwindow.setWindowIcon(QIcon('logo.ico'))
    clock = Page1()
    clock.show()
    sys.exit(app.exec_())
