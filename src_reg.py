# coding=utf-8
# src_reg.py
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
from def_information import *
key = 0
ver = '.4.3'
if key == 0:
    REG_INF, block_ban_quyen = check_inf()
else:
    REG_INF = 5
    block_ban_quyen = ''
if REG_INF == 5:
    banquyen = 'ADMIN user'
if REG_INF == 4:
    banquyen = 'PRO user'
else:
    if REG_INF == 3:
        banquyen = 'VIP user'
    else:
        if REG_INF == 2:
            banquyen = 'FREE user'
        else:
            banquyen = 'Bạn chưa đăng kí bản quyền'
if REG_INF > 1:
    version = '1.1' + ver
else:
    version = '1.0' + ver

def Registry_Inf_get():
    return REG_INF


class Registry_Inf(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.grip = QGridLayout()
        self.setLayout(self.grip)
        self.group0 = QGroupBox('Thông tin phần mềm Tool4LaTeX')
        self.group0.vbox = QGridLayout()
        self.group0.label1 = QLabel()
        self.group0.label2 = QLabel()
        self.group0.label3 = QLabel()
        self.group0.label4 = QLabel()
        self.group0.label5 = QLabel()
        self.group0.label6 = QLabel()
        self.group0.label7 = QLabel()
        self.group0.label8 = QLabel()
        self.group0.label9 = QLabel()
        self.group0.label10 = QLabel()
        self.group0.label11 = QLabel()
        self.group0.label12 = QLabel()
        self.group0.label1.setText('Tác giả phần mềm')
        self.group0.label2.setText('<a href="https://www.facebook.com/phanthanhtam295">Phan Thanh Tâm - 0907991160 - THPT Trần Hưng Đạo - Gò Vấp - TP.HCM</a>')
        self.group0.label2.setOpenExternalLinks(True)
        self.group0.label3.setText('Phiên bản')
        self.group0.label4.setText(version)
        self.group0.label5.setText('Tình trạng bản quyền')
        self.group0.label6.setText(banquyen)
        self.group0.label7.setText('Group facebook')
        self.group0.label8.setText('<a href="https://www.facebook.com/groups/NhomLaTeX/">https://www.facebook.com/groups/NhomLaTeX/</a>')
        self.group0.label8.setOpenExternalLinks(True)
        self.group0.label9.setText('Page facebook')
        self.group0.label10.setText('<a href="https://www.facebook.com/NhomLaTeX">https://www.facebook.com/NhomLaTeX</a>')
        self.group0.label10.setOpenExternalLinks(True)
        self.group0.label11.setText('Group Ngân hàng Offline')
        self.group0.label12.setText('<a href="https://www.facebook.com/groups/315792662486949/">Ngân hàng Offline - 10.000 câu hỏi</a>')
        self.group0.label12.setOpenExternalLinks(True)
        self.group0.setLayout(self.group0.vbox)
        self.group0.vbox.addWidget(self.group0.label1, 0, 0)
        self.group0.vbox.addWidget(self.group0.label2, 0, 1, 1, 2)
        self.group0.vbox.addWidget(self.group0.label3, 1, 0)
        self.group0.vbox.addWidget(self.group0.label4, 1, 1)
        self.group0.vbox.addWidget(self.group0.label5, 2, 0)
        self.group0.vbox.addWidget(self.group0.label6, 2, 1)
        self.group0.vbox.addWidget(self.group0.label7, 3, 0)
        self.group0.vbox.addWidget(self.group0.label8, 3, 1)
        self.group0.vbox.addWidget(self.group0.label9, 4, 0)
        self.group0.vbox.addWidget(self.group0.label10, 4, 1)
        self.group0.vbox.addWidget(self.group0.label11, 5, 0)
        self.group0.vbox.addWidget(self.group0.label12, 5, 1)
        self.group0.setMinimumHeight(200)
        self.group1 = QGroupBox('Cài đặt MikTeX 2.9')
        self.group1.vbox = QGridLayout()
        self.group1.hbox = QHBoxLayout()
        self.group1.hbox2 = QHBoxLayout()
        self.group1.label1 = QLabel()
        self.group1.label2 = QLabel()
        self.group1.label3 = QLabel()
        self.group1.label4 = QLabel()
        self.group1.label1.setText('Link download MikTeX 64-bit. Chọn Download')
        self.group1.label2.setText('<a href="https://miktex.org/2.9/setup">https://miktex.org/2.9/setup</a>')
        self.group1.label2.setOpenExternalLinks(True)
        self.group1.label3.setText('Link download MikTeX 32-bit. Chọn thẻ All downloads. Chọn thẻ Basic Installer 32-bit')
        self.group1.label4.setText('<a href="https://miktex.org/download#all">https://miktex.org/download#all</a>')
        self.group1.label4.setOpenExternalLinks(True)
        self.group1.setLayout(self.group1.vbox)
        self.group1.vbox.addWidget(self.group1.label1, 0, 1)
        self.group1.vbox.addWidget(self.group1.label2, 0, 2)
        self.group1.vbox.addWidget(self.group1.label3, 1, 1)
        self.group1.vbox.addWidget(self.group1.label4, 1, 2)
        self.group2 = QGroupBox('Cài đặt TeXstudio')
        self.group2.vbox = QGridLayout()
        self.group2.hbox = QHBoxLayout()
        self.group2.hbox2 = QHBoxLayout()
        self.group2.label1 = QLabel()
        self.group2.label2 = QLabel()
        self.group2.label3 = QLabel()
        self.group2.label4 = QLabel()
        self.group2.label1.setText('Link download TeXstudio. Chọn Download Now')
        self.group2.label2.setText('<a href="https://www.texstudio.org/">https://www.texstudio.org/</a>')
        self.group2.label2.setOpenExternalLinks(True)
        self.group2.setLayout(self.group2.vbox)
        self.group2.vbox.addWidget(self.group2.label1, 0, 1)
        self.group2.vbox.addWidget(self.group2.label2, 0, 2)
        self.group4 = QGroupBox('Cài đặt PDF-XChange Viewer')
        self.group4.vbox = QGridLayout()
        self.group4.hbox = QHBoxLayout()
        self.group4.hbox2 = QHBoxLayout()
        self.group4.label1 = QLabel()
        self.group4.label2 = QLabel()
        self.group4.label3 = QLabel()
        self.group4.label4 = QLabel()
        self.group4.label1.setText('Link download PDF-XChange Viewer. Chọn Download Now')
        self.group4.label2.setText('<a href="https://www.tracker-software.com/product/pdf-xchange-viewer/download?fileid=446">https://www.tracker-software.com</a>')
        self.group4.label2.setOpenExternalLinks(True)
        self.group4.setLayout(self.group4.vbox)
        self.group4.vbox.addWidget(self.group4.label1, 0, 1)
        self.group4.vbox.addWidget(self.group4.label2, 0, 2)
        self.group3 = QGroupBox('Đăng kí thông tin')
        self.group3.vbox = QGridLayout()
        self.group3.form1 = QFormLayout()
        self.group3.form2 = QFormLayout()
        self.group3.line1 = QLineEdit()
        self.group3.line2 = QLineEdit()
        self.group3.line3 = QLineEdit()
        self.group3.form1.addRow('Họ và tên', self.group3.line1)
        self.group3.form1.addRow('Số điện thoại', self.group3.line2)
        self.group3.form1.addRow('Đơn vị - Tỉnh (TP)', self.group3.line3)
        hbox = QHBoxLayout()
        button1 = QPushButton('Tạo file đăng kí')
        button2 = QPushButton('Gửi file đăng kí')
        hbox.addWidget(button1)
        button1.clicked.connect(self.get_file_reg)
        hbox.addWidget(button2)
        button2.clicked.connect(self.send_file_reg)
        self.group3.form1.addRow(hbox)
        self.group3.form2.addRow('', self.group3.line3)
        self.group3.setLayout(self.group3.vbox)
        self.group3.vbox.addLayout(self.group3.form1, 0, 0)
        self.group3.vbox.addLayout(self.group3.form2, 0, 1)
        self.group3.hbox = QHBoxLayout()
        self.group5 = QGroupBox('Update to be continue')
        self.group5.setMinimumHeight(100)
        self.group0.setMaximumHeight(190)
        self.group1.setMaximumHeight(90)
        self.group2.setMaximumHeight(65)
        self.group4.setMaximumHeight(65)
        self.layout().addWidget(self.group0)
        self.layout().addWidget(self.group1)
        self.layout().addWidget(self.group2)
        self.layout().addWidget(self.group4)
        self.layout().addWidget(self.group5)
        if REG_INF == 1:
            self.layout().addWidget(self.group3)
        if block_ban_quyen == 'PRO':
            reply = QMessageBox.question(self, 'Chú ý', 'TH1.\tBạn cần kết nối internet để cấp quyền PRO user.\n\tKhi kết nối được internet, hãy mở lại Tool4LaTeX.\n\nTH2.\tThời hạn PRO user của bạn đã hết.', QMessageBox.Yes)
        else:
            if block_ban_quyen == 'VIP':
                reply = QMessageBox.question(self, 'Chú ý', 'TH1.\tBạn cần kết nối internet để cấp quyền VIP user.\n\tKhi kết nối được internet, hãy mở lại Tool4LaTeX.\n\nTH2.\tThời hạn VIP user của bạn đã hết.', QMessageBox.Yes)

    def get_file_reg(self):
        ten = self.group3.line1.text()
        sdt = self.group3.line2.text()
        donvi = self.group3.line3.text()
        filename = strip_accents(ten + '-' + sdt)
        filename = str(filename).replace("b'", '')
        filename = str(filename).replace("'", '')
        filename = filename.replace(' ', '')
        registry_inf(filename, ten, sdt, donvi)

    def send_file_reg(self):
        webbrowser.open('https://www.facebook.com/messages/t/phanthanhtam295')