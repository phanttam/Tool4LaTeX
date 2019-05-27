# coding=utf-8
# src_convert.py
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

class Convert(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group1 = QGroupBox('Convert question form (dethi3.3) to Ex_test')
        self.group1.setMinimumHeight(100)
        self.group1.hbox = QHBoxLayout()
        self.group1.hboxhd = QHBoxLayout()
        self.group1.check = QCheckBox('HD')
        self.group1.check.setChecked(True)
        self.group1.hd = QGroupBox('Hướng dẫn')
        self.group1.hboxhd.addWidget(self.group1.check)
        self.group1.hboxhd.addWidget(self.group1.hd)
        self.group1.hbox1 = QHBoxLayout()
        self.group1.label1 = QLabel('Files ')
        self.group1.label1.setMinimumWidth(30)
        self.group1.line1 = QLineEdit()
        self.group1.line1.setText('')
        self.group1.button0 = QPushButton('Hướng dẫn')
        self.group1.button0.clicked.connect(self.G1_HD)
        self.group1.button1 = QPushButton('Chọn')
        self.group1.button1.clicked.connect(self.G1_get_file_1)
        self.group1.button2 = QPushButton('Chuyển')
        self.group1.button2.clicked.connect(self.G1_get_file_2)
        self.group1.hbox.addWidget(self.group1.label1)
        self.group1.hbox.addWidget(self.group1.line1)
        self.group1.hbox.addWidget(self.group1.button0)
        self.group1.hbox.addWidget(self.group1.button1)
        self.group1.hbox.addWidget(self.group1.button2)
        self.group1.setLayout(self.group1.hbox)
        self.group2 = QGroupBox('baitracnghiem form (dethi3.5) to Ex_test')
        self.group2.setMinimumHeight(100)
        self.group2.hbox = QHBoxLayout()
        self.group2.hboxhd = QHBoxLayout()
        self.group2.check = QCheckBox('HD')
        self.group2.check.setChecked(True)
        self.group2.hd = QGroupBox('Hướng dẫn')
        self.group2.hboxhd.addWidget(self.group2.check)
        self.group2.hboxhd.addWidget(self.group2.hd)
        self.group2.hbox1 = QHBoxLayout()
        self.group2.label1 = QLabel('Files ')
        self.group2.label1.setMinimumWidth(30)
        self.group2.line1 = QLineEdit()
        self.group2.button0 = QPushButton('Hướng dẫn')
        self.group2.button0.clicked.connect(self.G2_HD)
        self.group2.button1 = QPushButton('Chọn')
        self.group2.button1.clicked.connect(self.G2_get_file_1)
        self.group2.button2 = QPushButton('Chuyển')
        self.group2.button2.clicked.connect(self.G2_get_file_2)
        self.group2.hbox.addWidget(self.group2.label1)
        self.group2.hbox.addWidget(self.group2.line1)
        self.group2.hbox.addWidget(self.group2.button0)
        self.group2.hbox.addWidget(self.group2.button1)
        self.group2.hbox.addWidget(self.group2.button2)
        self.group2.setLayout(self.group2.hbox)
        self.group3 = QGroupBox('Ex_test to baitracnghiem form (dethi3.5)')
        self.group3.setMinimumHeight(100)
        self.group3.hbox = QHBoxLayout()
        self.group3.hboxhd = QHBoxLayout()
        self.group3.check = QCheckBox('HD')
        self.group3.check.setChecked(True)
        self.group3.hd = QGroupBox('Hướng dẫn')
        self.group3.hboxhd.addWidget(self.group3.check)
        self.group3.hboxhd.addWidget(self.group3.hd)
        self.group3.hbox1 = QHBoxLayout()
        self.group3.label1 = QLabel('Files ')
        self.group3.label1.setMinimumWidth(30)
        self.group3.line1 = QLineEdit()
        self.group3.button0 = QPushButton('Hướng dẫn')
        self.group3.button0.clicked.connect(self.G2_HD)
        self.group3.button1 = QPushButton('Chọn')
        self.group3.button1.clicked.connect(self.G2_get_file_1)
        self.group3.button2 = QPushButton('Chuyển')
        self.group3.button2.clicked.connect(self.G2_get_file_2)
        self.group3.hbox.addWidget(self.group3.label1)
        self.group3.hbox.addWidget(self.group3.line1)
        self.group3.hbox.addWidget(self.group3.button0)
        self.group3.hbox.addWidget(self.group3.button1)
        self.group3.hbox.addWidget(self.group3.button2)
        self.group3.setLayout(self.group3.hbox)
        self.group4 = QGroupBox('baitracnghiem form (dethi3.5) to Ex_test')
        self.group4.setMinimumHeight(100)
        self.group4.hbox = QHBoxLayout()
        self.group4.hboxhd = QHBoxLayout()
        self.group4.check = QCheckBox('HD')
        self.group4.check.setChecked(True)
        self.group4.hd = QGroupBox('Hướng dẫn')
        self.group4.hboxhd.addWidget(self.group4.check)
        self.group4.hboxhd.addWidget(self.group4.hd)
        self.group4.hbox1 = QHBoxLayout()
        self.group4.label1 = QLabel('Files ')
        self.group4.label1.setMinimumWidth(30)
        self.group4.line1 = QLineEdit()
        self.group4.button0 = QPushButton('Hướng dẫn')
        self.group4.button0.clicked.connect(self.G2_HD)
        self.group4.button1 = QPushButton('Chọn')
        self.group4.button1.clicked.connect(self.G2_get_file_1)
        self.group4.button2 = QPushButton('Chuyển')
        self.group4.button2.clicked.connect(self.G2_get_file_2)
        self.group4.hbox.addWidget(self.group4.label1)
        self.group4.hbox.addWidget(self.group4.line1)
        self.group4.hbox.addWidget(self.group4.button0)
        self.group4.hbox.addWidget(self.group4.button1)
        self.group4.hbox.addWidget(self.group4.button2)
        self.group4.setLayout(self.group4.hbox)
        self.group5 = QGroupBox('Auto check True (Sẽ update chọn đáp án từ file Excel, Word, Pdf (từ Tex hoặc Word))')
        self.group5.setMinimumHeight(100)
        self.group5.hbox = QHBoxLayout()
        self.group5.hboxhd = QHBoxLayout()
        self.group5.check = QCheckBox('HD')
        self.group5.check.setChecked(True)
        self.group5.hd = QGroupBox('Hướng dẫn')
        self.group5.hboxhd.addWidget(self.group5.check)
        self.group5.hboxhd.addWidget(self.group5.hd)
        self.group5.hbox1 = QHBoxLayout()
        self.group5.label1 = QLabel('Files ')
        self.group5.label1.setMinimumWidth(30)
        self.group5.line1 = QLineEdit()
        self.group5.button0 = QPushButton('Hướng dẫn')
        self.group5.button0.clicked.connect(self.G5_HD)
        self.group5.button1 = QPushButton('Chọn')
        self.group5.button1.clicked.connect(self.G5_get_file_1)
        self.group5.button2 = QPushButton('Chuyển')
        self.group5.button2.clicked.connect(self.G5_get_file_2)
        self.group5.hbox.addWidget(self.group5.label1)
        self.group5.hbox.addWidget(self.group5.line1)
        self.group5.hbox.addWidget(self.group5.button0)
        self.group5.hbox.addWidget(self.group5.button1)
        self.group5.hbox.addWidget(self.group5.button2)
        self.group5.setLayout(self.group5.hbox)
        self.group7 = QGroupBox('Update to be continue')
        self.group7.setMinimumHeight(250)
        self.layout().addWidget(self.group1, 1, 1)
        self.layout().addWidget(self.group2, 2, 1)
        self.layout().addWidget(self.group5, 3, 1)
        self.layout().addWidget(self.group7, 4, 1)
        for widget in (self.group1, self.group2, self.group5):
            widget.setMinimumHeight(60)
            widget.setMaximumHeight(60)

    def G1_HD(self):
        Form_question = 'Bước 1: Nhấn chọn file hoặc nhiều file.\r\nBước 2: Nhấn Chuyển để chuyển đổi.\r\n Cấu trúc form question trong dethi.sty\n\\begin{question}\n<Đề>\n\\datcot[4]\\bonpa (hoặc \\datcot[2]\\bonpa, \\datcot\\bonpa)\n{\\dung{<paA>}}\n{\\sai{<paB>}}\n{\\sai{<paC>}}\n{\\sai{<paD>}}\n\\loigiai{\n<Lời giải>\n}\n\\end{question}\n'
        Form_ex = 'Cấu trúc form question trong dethi.sty\n\\begin{ex}\n<Đề>\n\\choice\n{\\True }\n{}\n{}\n{}\n\\loigiai{\n<Lời giải>\n}\n\\end{ex}\n'
        QMessageBox.question(self, 'Hướng dẫn', Form_question + Form_ex, QMessageBox.Yes)

    def G1_get_file_1(self):
        fname = QFileDialog.getOpenFileNames()
        filename = ''
        for i in fname[0]:
            filename += i + ','

        self.group1.line1.setText(filename[:-1])

    def G1_get_file_2(self):
        start_time = time.time()
        try:
            try:
                List = List_creat(self.group1.line1.text())
            except Exception as er:
                QMessageBox.question(self, 'Thông báo', 'Bạn chưa chọn file', QMessageBox.Yes)

            i = 0
            Print = 'Các file sau khi chuyển trong thư mục: CONVERT.\nTên các file là:\n'
            for filename in List:
                head, tail = os.path.split(filename)
                i += 1
                block = Conv_ques2ex_get_cau(filename)
                with codecs.open('CONVERT//' + tail.replace('.tex', '_ex.tex'), 'w', 'utf-8') as (f):
                    f.write(block)
                    f.close()
                    Print += tail.replace('.tex', '_ex.tex') + '\n'

            t = time.time() - start_time
            hour, minute, second = Time_convert(t)
            QMessageBox.question(self, 'Thông báo', 'Đã chuyển thành công ' + str(i) + ' file.\nThời gian xử lí: ' + str(int(hour)) + ':' + str(int(minute)) + ':' + str(round(second, 2)) + '\n' + Print, QMessageBox.Yes)
        except Exception as er:
            QMessageBox.question(self, 'Thông báo', 'Bạn chưa chọn file', QMessageBox.Yes)

    def G2_HD(self):
        Form_baithi = 'Bước 1: Nhấn chọn file hoặc nhiều file.\r\nBước 2: Nhấn Chuyển để chuyển đổi.\r\n Cấu trúc form baithitracnghiem trong dethi.sty\n\\baitracnghiem{<Mã ID> }{% <Nguồn>\n<Đề>\n}{\\bonpa{1} %Phương án đúng là A, tương tự cho 2-B, 3-C, 4-D\n{}\n{}\n{}\n{}\n}{\\\\\n<Lời giải>\n}\n'
        Form_ex = 'Cấu trúc form question trong dethi.sty\n\\begin{ex}\n<Đề>\n\\choice\n{\\True }\n{}\n{}\n{}\n\\loigiai{\n<Lời giải>\n}\n\\end{ex}\n'
        QMessageBox.question(self, 'Hướng dẫn', Form_baithi + Form_ex, QMessageBox.Yes)

    def G2_get_file_1(self):
        fname = QFileDialog.getOpenFileNames()
        filename = ''
        for i in fname[0]:
            filename += i + ','

        self.group2.line1.setText(filename[:-1])

    def G2_get_file_2(self):
        start_time = time.time()
        try:
            try:
                List = List_creat(self.group2.line1.text())
            except Exception as er:
                QMessageBox.question(self, 'Thông báo', 'Bạn chưa chọn file', QMessageBox.Yes)

            i = 0
            Print = 'Các file sau khi chuyển trong thư mục: CONVERT.\nTên các file là:\n'
            for filename in List:
                head, tail = os.path.split(filename)
                i += 1
                block = Conv_dethi2ex(filename)
                with codecs.open('CONVERT//' + tail.replace('.tex', '_ex.tex'), 'w', 'utf-8') as (f):
                    f.write(block)
                    f.close()
                    Print += tail.replace('.tex', '_ex.tex') + '\n'

            t = time.time() - start_time
            hour, minute, second = Time_convert(t)
            QMessageBox.question(self, 'Thông báo', 'Đã chuyển thành công ' + str(i) + ' file.\nThời gian xử lí: ' + str(int(hour)) + ':' + str(int(minute)) + ':' + str(round(second, 2)) + '\n' + Print, QMessageBox.Yes)
        except Exception as er:
            QMessageBox.question(self, 'Thông báo', 'Bạn chưa chọn file', QMessageBox.Yes)

    def G5_HD(self):
        Form_baithi = 'Bước 1: Nhấn chọn file hoặc nhiều file.\r\nBước 2: Nhấn Chuyển để chuyển đổi.\r\nChú ý: Trong lời giải có chứa text: Chọn, Chọn phương án, Chọn đáp án'
        QMessageBox.question(self, 'Hướng dẫn', Form_baithi, QMessageBox.Yes)

    def G5_get_file_1(self):
        fname = QFileDialog.getOpenFileNames()
        filename = ''
        for i in fname[0]:
            filename += i + ','

        self.group5.line1.setText(filename[:-1])

    def G5_get_file_2(self):
        if REG_INF == 1:
            QMessageBox.question(self, 'Thông báo', 'Vui lòng đăng kí (miễn phí) bản quyền để sử dụng', QMessageBox.Yes)
        else:
            start_time = time.time()
            List = List_creat(self.group5.line1.text())
            if List[0] == '':
                QMessageBox.question(self, 'Thông báo', 'Bạn chưa chọn file', QMessageBox.Yes)
            else:
                i = 0
                Print = 'Các file sau khi chuyển trong thư mục: CONVERT.\nTên các file là:\n'
                for filename in List:
                    head, tail = os.path.split(filename)
                    i += 1
                    block = Conv_Auto_True(filename)
                    with codecs.open('CONVERT//' + tail.replace('.tex', 'CheckTrue.tex'), 'w', 'utf-8') as (f):
                        f.write(block)
                        f.close()
                        Print += tail.replace('.tex', 'CheckTrue.tex') + '\n'

                t = time.time() - start_time
                hour, minute, second = Time_convert(t)
                QMessageBox.question(self, 'Thông báo', 'Đã chuyển thành công ' + str(i) + ' file.\nThời gian xử lí: ' + str(int(hour)) + ':' + str(int(minute)) + ':' + str(round(second, 2)) + '\n' + Print, QMessageBox.Yes)