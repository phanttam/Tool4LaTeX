# coding=utf-8
# src_id_combo.py
import re, os, sys, csv, codecs, time
from datetime import datetime, timedelta
from urllib.request import urlopen
import math, argparse, subprocess, signal, shutil, errno, unicodedata, webbrowser
from fractions import Fraction
from decimal import Decimal
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from def_calculation import *
from src_reg import *
from def_bbt import *
from def_id import *
from def_convert import *
from def_ban_quyen import *

class ID_EditMode(QMainWindow):

    def __init__(self, parent):
        super(ID_EditMode, self).__init__()
        self.group0 = QGroupBox('Câu hỏi')
        self.group0.vbox = QVBoxLayout()
        self.group0.line = QTextEdit('')
        self.group0.hbox1 = QHBoxLayout()
        self.group0.hbox1.addWidget(self.group0.line)
        self.group0.hbox2 = QHBoxLayout()
        self.group0.button1 = QPushButton('Save')
        self.group0.button1.clicked.connect(self.SaveEdit)
        self.group0.button1.clicked.connect(parent.Show_table)
        self.group0.button2 = QPushButton('Cancel')
        self.group0.button2.clicked.connect(self.Cancel)
        self.group0.hbox2.addWidget(self.group0.button1)
        self.group0.hbox2.addWidget(self.group0.button2)
        self.group0.vbox.addItem(self.group0.hbox1)
        self.group0.vbox.addItem(self.group0.hbox2)
        self.group0.setLayout(self.group0.vbox)
        self.group0.setMaximumHeight(300)
        self.layout().addWidget(self.group0)
        self.setWindowTitle('Sửa nội dung câu hỏi')
        self.setGeometry(685, 30, 680, 400)
        with codecs.open('Temp//One.tex', 'r', 'utf-8') as (f):
            cau = f.read()
            f.close()
        self.group0.line.setText(cau)

    def Cancel(self):
        self.close()

    def SaveEdit(self):
        self.close()


class ID_Combo_full(QMainWindow):

    def __init__(self, parent):
        super(ID_Combo_full, self).__init__()
        self.group0 = QGroupBox('Danh sách ID5 và ID6 (Update version 5.3)')
        self.group0.vbox = QVBoxLayout()
        self.label1 = QLabel(self)
        self.label1.setText('Lớp  ')
        self.label1.setMinimumWidth(30)
        self.combo1 = QComboBox(self)
        self.combo1.setObjectName('chooseDataComboBox')
        self.combo1.addItem('')
        self.combo1.addItem('[2] Lớp 12')
        self.combo1.addItem('[1] Lớp 11')
        self.combo1.addItem('[0] Lớp 10')
        self.combo1.setMinimumWidth(580)
        self.combo1.currentIndexChanged.connect(self.ID1_change)
        self.label2 = QLabel(self)
        self.label2.setText('Môn  ')
        self.combo2 = QComboBox(self)
        self.combo2.setMinimumWidth(580)
        self.combo2.currentIndexChanged.connect(self.ID2_change)
        self.label3 = QLabel(self)
        self.label3.setText('Chương')
        self.label3.move(10, 70)
        self.combo3 = QComboBox(self)
        self.combo3.move(50, 70)
        self.combo3.setMinimumWidth(580)
        self.combo3.currentIndexChanged.connect(self.ID3_change)
        self.label4 = QLabel(self)
        self.label4.setText('Mức độ')
        self.label4.move(10, 100)
        self.combo4 = QComboBox(self)
        self.combo4.move(50, 100)
        self.combo4.addItem('[Y] Nhận biết')
        self.combo4.addItem('[B] Thông hiểu ')
        self.combo4.addItem('[K] Vận dụng thấp')
        self.combo4.addItem('[G] Vận dụng cao')
        self.combo4.addItem('[T] Bài toán thực tế')
        self.combo4.currentIndexChanged.connect(self.ID4_change)
        self.combo4.setMinimumWidth(580)
        self.label5 = QLabel(self)
        self.label5.setText('Bài')
        self.label5.move(10, 130)
        self.combo5 = QComboBox(self)
        self.combo5.move(50, 130)
        self.combo5.setMinimumWidth(580)
        self.combo5.currentIndexChanged.connect(self.ID5_change)
        self.label6 = QLabel(self)
        self.label6.setText('Dạng')
        self.label6.move(10, 160)
        self.combo6 = QComboBox(self)
        self.combo6.move(50, 160)
        self.combo6.setMinimumWidth(580)
        self.combo6.currentIndexChanged.connect(self.ID6_full)
        self.label = QLabel(self)
        self.label.setText('ID6 được gán: ')
        self.label.move(20, 190)
        self.line = QLabel(self)
        self.line.setMinimumWidth(580)
        self.group0.hbox1 = QHBoxLayout()
        self.group0.hbox1.addWidget(self.label1)
        self.group0.hbox1.addWidget(self.combo1)
        self.group0.hbox2 = QHBoxLayout()
        self.group0.hbox2.addWidget(self.label2)
        self.group0.hbox2.addWidget(self.combo2)
        self.group0.hbox3 = QHBoxLayout()
        self.group0.hbox3.addWidget(self.label3)
        self.group0.hbox3.addWidget(self.combo3)
        self.group0.hbox4 = QHBoxLayout()
        self.group0.hbox4.addWidget(self.label4)
        self.group0.hbox4.addWidget(self.combo4)
        self.group0.hbox5 = QHBoxLayout()
        self.group0.hbox5.addWidget(self.label5)
        self.group0.hbox5.addWidget(self.combo5)
        self.group0.hbox6 = QHBoxLayout()
        self.group0.hbox6.addWidget(self.label6)
        self.group0.hbox6.addWidget(self.combo6)
        self.group0.hbox7 = QHBoxLayout()
        self.filename_window1 = QLabel()
        self.group0.button1 = QPushButton('OK')
        self.group0.button1.clicked.connect(self.ApplyID)
        self.group0.button1.clicked.connect(parent.Show_table)
        self.group0.button2 = QPushButton('Cancel')
        self.group0.button2.clicked.connect(self.Cancel)
        self.group0.hbox7.addWidget(self.label)
        self.group0.hbox7.addWidget(self.line)
        self.group0.hbox7.addWidget(self.filename_window1)
        self.group0.hbox7.addWidget(self.group0.button1)
        self.group0.hbox7.addWidget(self.group0.button2)
        self.group0.vbox.addItem(self.group0.hbox1)
        self.group0.vbox.addItem(self.group0.hbox2)
        self.group0.vbox.addItem(self.group0.hbox3)
        self.group0.vbox.addItem(self.group0.hbox4)
        self.group0.vbox.addItem(self.group0.hbox5)
        self.group0.vbox.addItem(self.group0.hbox6)
        self.group0.vbox.addItem(self.group0.hbox7)
        self.group0.setLayout(self.group0.vbox)
        self.group0.setMaximumHeight(300)
        self.layout().addWidget(self.group0)
        self.setWindowTitle('Gán ID6 cho câu hỏi')
        for i in (self.label1, self.label2, self.label3, self.label4, self.label5, self.label6):
            i.setMinimumWidth(60)

        self.setGeometry(685, 440, 680, 600)

    def ID1_change(self):
        try:
            ID1 = self.combo1.currentText()[1]
            self.combo2.clear()
            for ID_1 in Call_ID_1(ID1)[1]:
                self.combo2.addItem(ID_1)

        except Exception as er:
            self.combo2.clear()

    def ID2_change(self):
        try:
            ID1 = self.combo1.currentText()[1]
            ID2 = self.combo2.currentText()[1]
            self.combo3.clear()
            for ID_3 in Call_ID_2(ID1, ID2)[1]:
                self.combo3.addItem(ID_3)

        except Exception as er:
            self.combo3.clear()

    def ID3_change(self):
        try:
            ID1 = self.combo1.currentText()[1]
            ID2 = self.combo2.currentText()[1]
            ID3 = self.combo3.currentText()[1]
            self.combo5.clear()
            for ID_4 in Call_ID_3(ID1, ID2, ID3)[1]:
                self.combo5.addItem(ID_4)

        except Exception as er:
            self.combo5.clear()

    def ID4_change(self):
        try:
            self.line.setText(self.combo1.currentText()[1] + self.combo2.currentText()[1] + self.combo3.currentText()[1] + self.combo4.currentText()[1] + self.combo5.currentText()[1] + '-' + self.combo6.currentText()[1])
        except Exception as err:
            self.line.setText('')

    def ID5_change(self):
        try:
            ID1 = self.combo1.currentText()[1]
            ID2 = self.combo2.currentText()[1]
            ID3 = self.combo3.currentText()[1]
            ID4 = self.combo5.currentText()[1]
            self.combo6.clear()
            for ID_5 in Call_ID_4(ID1, ID2, ID3, ID4)[1]:
                self.combo6.addItem(ID_5)

            self.line.setText(self.combo1.currentText()[1] + self.combo2.currentText()[1] + self.combo3.currentText()[1] + self.combo4.currentText()[1] + self.combo5.currentText()[1] + '-' + self.combo6.currentText()[1])
        except Exception as er:
            print(er)

    def ID6_full(self):
        try:
            self.line.setText(self.combo1.currentText()[1] + self.combo2.currentText()[1] + self.combo3.currentText()[1] + self.combo4.currentText()[1] + self.combo5.currentText()[1] + '-' + self.combo6.currentText()[1])
        except Exception as err:
            self.line.setText('')

    def ApplyID(self):
        try:
            if 1 == 1:
                if 1 == 1:
                    with codecs.open('Temp//temp.tex', 'r', 'utf-8') as (f):
                        filename = f.read()
                    with codecs.open('Temp//One.tex', 'r', 'utf-8') as (f):
                        cau = f.read()
                        cau_n = cau.replace('\\begin{ex}', '\\begin{ex}%[' + self.line.text() + ']').replace('\\begin{bt}', '\\begin{bt}%[' + self.line.text() + ']')
                    with codecs.open('Temp//One.tex', 'w', 'utf-8') as (f):
                        f.write(cau_n)
                    with codecs.open(filename, 'r', 'utf-8') as (f):
                        data = f.read()
                        data_n = data.replace(cau, cau_n)
                    with codecs.open(filename, 'w', 'utf-8') as (f):
                        f.write(data_n)
                    self.close()
        except Exception as err:
            pass

    def Cancel(self):
        self.close()