# coding=utf-8
# src_options.py
import re, os, sys, csv, codecs, time
from datetime import datetime, timedelta
from urllib.request import urlopen
import math, argparse, subprocess, signal, shutil, errno, unicodedata, webbrowser
from fractions import Fraction
from decimal import Decimal
from random import *
from def_calculation import *
from src_reg import *
from def_bbt import *
from def_id import *
from def_convert import *
from def_ban_quyen import *

class Option(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group0 = QGroupBox('Trình bày trang in (header - footer)')
        self.group0.setMinimumHeight(100)
        self.group0.hbox = QHBoxLayout()
        self.group0.hboxhd = QHBoxLayout()
        self.group0.check = QCheckBox('HD')
        self.group0.check.setChecked(True)
        self.group0.hd = QGroupBox('Hướng dẫn')
        self.group0.hboxhd.addWidget(self.group0.check)
        self.group0.hboxhd.addWidget(self.group0.hd)
        self.group0.grip = QGridLayout()
        self.group0.label1 = QLabel('\\lhead')
        self.group0.label1.setMinimumWidth(30)
        self.group0.line1 = QLineEdit()
        self.group0.label2 = QLabel('\\chead')
        self.group0.label2.setMinimumWidth(30)
        self.group0.line2 = QLineEdit()
        self.group0.line2.setText('')
        self.group0.label3 = QLabel('\\rhead')
        self.group0.label3.setMinimumWidth(30)
        self.group0.line3 = QLineEdit()
        self.group0.label11 = QLabel('\\lfoot')
        self.group0.label11.setMinimumWidth(30)
        self.group0.line11 = QLineEdit()
        self.group0.label12 = QLabel('\\cfoot')
        self.group0.label12.setMinimumWidth(30)
        self.group0.line12 = QLineEdit()
        self.group0.line12.setText('')
        self.group0.label13 = QLabel('\\rfoot')
        self.group0.label13.setMinimumWidth(30)
        self.group0.line13 = QLineEdit()
        self.group0.button = QPushButton('Save')
        self.group0.button.clicked.connect(self.G1_Save)
        self.group0.grip.addWidget(self.group0.label1, 0, 0)
        self.group0.grip.addWidget(self.group0.line1, 0, 1)
        self.group0.grip.addWidget(self.group0.label2, 0, 2)
        self.group0.grip.addWidget(self.group0.line2, 0, 3)
        self.group0.grip.addWidget(self.group0.label3, 0, 4)
        self.group0.grip.addWidget(self.group0.line3, 0, 5)
        self.group0.grip.addWidget(self.group0.label11, 1, 0)
        self.group0.grip.addWidget(self.group0.line11, 1, 1)
        self.group0.grip.addWidget(self.group0.label12, 1, 2)
        self.group0.grip.addWidget(self.group0.line12, 1, 3)
        self.group0.grip.addWidget(self.group0.label13, 1, 4)
        self.group0.grip.addWidget(self.group0.line13, 1, 5)
        self.group0.grip.addWidget(self.group0.button, 1, 6)
        self.group0.setLayout(self.group0.grip)
        self.group0.setMaximumHeight(100)
        try:
            headfoot = codecs.open('Setting//header-footer.tex', 'r', 'utf-8').read()
            data = re.findall('\\\\lhead\\{(.*?)\\}\\s*\\\\chead\\{(.*?)\\}\\s*\\\\rhead\\{(.*?)\\}\\s*\\\\lfoot\\{(.*?)\\}\\s*\\\\cfoot\\{(.*?)\\}\\s*\\\\rfoot\\{(.*?)\\}', headfoot, re.DOTALL)
            if data != None:
                self.group0.line1.setText(data[0][0])
                self.group0.line2.setText(data[0][1])
                self.group0.line3.setText(data[0][2])
                self.group0.line11.setText(data[0][3])
                self.group0.line12.setText(data[0][4])
                self.group0.line13.setText(data[0][5])
        except Exception as er:
            self.group0.line1.setText('Trường THPT Trần Hưng Đạo')
            self.group0.line3.setText('Thầy Phan Thanh Tâm')
            self.group0.line11.setText('Số điện thoại: 0907991160')
            self.group0.line13.setText('Trang \\thepage')
        self.group1 = QGroupBox('baitracnghiem form (dethi3.5) to Ex_test')
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
        self.group1.button0 = QPushButton('Hướng dẫn')
        self.group1.button0.clicked.connect(self.G2_HD)
        self.group1.button1 = QPushButton('Chọn')
        self.group1.button1.clicked.connect(self.G2_get_file_1)
        self.group1.button2 = QPushButton('Chuyển')
        self.group1.button2.clicked.connect(self.G2_get_file_2)
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
        self.group3 = QGroupBox('baitracnghiem form (dethi3.5) to Ex_test')
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
        self.group4 = QGroupBox('Auto check True (Sẽ update chọn đáp án từ file Excel, Word, Pdf (từ Tex hoặc Word))')
        self.group4.setMinimumHeight(100)
        self.group4.hbox = QHBoxLayout()
        self.group4.hboxhd = QHBoxLayout()
        self.group4.check = QCheckBox('HD')
        self.group4.check.setChecked(True)
        self.group4.hd = QGroupBox('Hướng dẫn')
        self.group4.hboxhd.addWidget(self.group4.check)
        self.group4.hboxhd.addWidget(self.group4.hd)
        self.group5 = QGroupBox('Update to be continue')
        self.group5.setMinimumHeight(100)
        self.layout().addWidget(self.group0)
        # self.layout().addWidget(self.group1)
        # self.layout().addWidget(self.group2)
        # self.layout().addWidget(self.group3)
        # self.layout().addWidget(self.group4)
        self.layout().addWidget(self.group5)
        # self.layout().setAlignment(Qt.AlignTop)
        # for widget in (self.group0, self.group1, self.group4):
        #     widget.setMinimumHeight(100)
        #     widget.setMaximumHeight(60)

    def G1_Save(self):
        QMessageBox.question(self, 'Hướng dẫn', 'Đã lưu cài đặt trình bày trang in.', QMessageBox.Yes)
        with codecs.open('Setting//header-footer.tex', 'w', 'utf-8') as (f):
            block = '\\usepackage{fancyhdr}\n\\pagestyle{fancy}\n\\renewcommand{\\headrulewidth}{1pt}\n\\renewcommand{\\footrulewidth}{1pt}\n'
            block += '\\lhead{' + self.group0.line1.text() + '}\n'
            block += '\\chead{' + self.group0.line2.text() + '}\n'
            block += '\\rhead{' + self.group0.line3.text() + '}\n'
            block += '\\lfoot{' + self.group0.line11.text() + '}\n'
            block += '\\cfoot{' + self.group0.line12.text() + '}\n'
            block += '\\rfoot{' + self.group0.line13.text() + '}\n'
            f.write(block)
            f.close()

    def G1_get_file_1(self):
        fname = QFileDialog.getOpenFileNames()
        filename = ''
        for i in fname[0]:
            filename += i + ','

        self.group0.line1.setText(filename[:-1])

    def G1_get_file_2(self):
        start_time = time.time()
        List = List_creat(self.group0.line1.text())
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

    def G2_HD(self):
        Form_baithi = 'Bước 1: Nhấn chọn file hoặc nhiều file.\nBước 2: Nhấn Chuyển để chuyển đổi.\n Cấu trúc form baithitracnghiem trong dethi.sty\n\\baitracnghiem{<Mã ID> }{% <Nguồn>\n<Đề>\n}{\\bonpa{1} %Phương án đúng là A, tương tự cho 2-B, 3-C, 4-D\n{}\n{}\n{}\n{}\n}{\\\\\n<Lời giải>\n}\n'
        Form_ex = 'Cấu trúc form question trong dethi.sty\n\\begin{ex}\n<Đề>\n\\choice\n{\\True }\n{}\n{}\n{}\n\\loigiai{\n<Lời giải>\n}\n\\end{ex}\n'
        QMessageBox.question(self, 'Hướng dẫn', Form_baithi + Form_ex, QMessageBox.Yes)

    def G2_get_file_1(self):
        fname = QFileDialog.getOpenFileNames()
        filename = ''
        for i in fname[0]:
            filename += i + ','

        self.group1.line1.setText(filename[:-1])

    def G2_get_file_2(self):
        start_time = time.time()
        List = List_creat(self.group1.line1.text())
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