# coding=utf-8
# src_bbt.py
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
REG_INF = Registry_Inf_get()

class Draw_BBT(QWidget):

    def __init__(self, parent=None):
        super(Draw_BBT, self).__init__()
        self.grip = QGridLayout()
        self.setLayout(self.grip)
        self.group0 = QGroupBox('Tùy biến trong vẽ bảng biến thiên')
        self.group0.hbox = QHBoxLayout()
        self.group0.setLayout(self.group0.hbox)
        self.group0.check = QCheckBox('Hiển thị công thức hàm', self)
        self.group0.check.setChecked(True)
        self.group0.hbox.addWidget(self.group0.check)
        self.group1 = QGroupBox('Bảng biến thiên của hàm bậc nhất y = ax + b')
        self.group1.hbox = QHBoxLayout()
        self.group1.setLayout(self.group1.hbox)
        self.group1.labela = QLabel()
        self.group1.labela.setText('a = ')
        self.group1.labela.setMaximumWidth(20)
        self.group1.linea = QLineEdit()
        self.group1.linea.setText('1')
        self.group1.linea.setMaximumWidth(30)
        self.group1.labelb = QLabel()
        self.group1.labelb.setText('b = ')
        self.group1.labelb.setMaximumWidth(20)
        self.group1.lineb = QLineEdit()
        self.group1.lineb.setText('')
        self.group1.lineb.setMaximumWidth(30)
        button = QPushButton('Xuất code', self)
        button.clicked.connect(self.bbt_bac_nhat)
        self.group1.hbox.addWidget(self.group1.labela)
        self.group1.hbox.addWidget(self.group1.linea)
        self.group1.hbox.addWidget(self.group1.labelb)
        self.group1.hbox.addWidget(self.group1.lineb)
        self.group1.hbox.addWidget(button)
        self.layout().addWidget(self.group1, 2, 0)
        self.group2 = QGroupBox('Bảng biến thiên của hàm bậc hai y = ax^2 + bx + c')
        self.group2.hbox = QHBoxLayout()
        self.group2.setLayout(self.group2.hbox)
        self.group2.labela = QLabel()
        self.group2.labela.setText('a = ')
        self.group2.labela.setMaximumWidth(20)
        self.group2.linea = QLineEdit()
        self.group2.linea.setText('1')
        self.group2.linea.setMaximumWidth(30)
        self.group2.labelb = QLabel()
        self.group2.labelb.setText('b = ')
        self.group2.labelb.setMaximumWidth(20)
        self.group2.lineb = QLineEdit()
        self.group2.lineb.setText('')
        self.group2.lineb.setMaximumWidth(30)
        self.group2.labelc = QLabel()
        self.group2.labelc.setText('c = ')
        self.group2.labelc.setMaximumWidth(20)
        self.group2.linec = QLineEdit()
        self.group2.linec.setText('')
        self.group2.linec.setMaximumWidth(30)
        button = QPushButton('Xuất code', self)
        button.clicked.connect(self.bbt_bac_hai)
        self.group2.hbox.addWidget(self.group2.labela)
        self.group2.hbox.addWidget(self.group2.linea)
        self.group2.hbox.addWidget(self.group2.labelb)
        self.group2.hbox.addWidget(self.group2.lineb)
        self.group2.hbox.addWidget(self.group2.labelc)
        self.group2.hbox.addWidget(self.group2.linec)
        self.group2.hbox.addWidget(button)
        self.layout().addWidget(self.group2, 2, 1)
        self.group3 = QGroupBox('Bảng biến thiên của hàm bậc ba y = ax^3 + bx^2 + cx + d')
        self.group3.hbox = QHBoxLayout()
        self.group3.setLayout(self.group3.hbox)
        self.group3.labela = QLabel()
        self.group3.labela.setMaximumWidth(20)
        self.group3.labela.setText('a = ')
        self.group3.linea = QLineEdit()
        self.group3.linea.setText('1')
        self.group3.linea.setMaximumWidth(30)
        self.group3.labelb = QLabel()
        self.group3.labelb.setText('b = ')
        self.group3.labelb.setMaximumWidth(20)
        self.group3.lineb = QLineEdit()
        self.group3.lineb.setText('')
        self.group3.lineb.setMaximumWidth(30)
        self.group3.labelc = QLabel()
        self.group3.labelc.setText('c = ')
        self.group3.labelc.setMaximumWidth(20)
        self.group3.linec = QLineEdit()
        self.group3.linec.setText('')
        self.group3.linec.setMaximumWidth(30)
        self.group3.labeld = QLabel()
        self.group3.labeld.setText('d = ')
        self.group3.labeld.setMaximumWidth(20)
        self.group3.lined = QLineEdit()
        self.group3.lined.setText('')
        self.group3.lined.setMaximumWidth(30)
        button = QPushButton('Xuất code', self)
        button.clicked.connect(self.bbt_bac_ba)
        self.group3.hbox.addWidget(self.group3.labela)
        self.group3.hbox.addWidget(self.group3.linea)
        self.group3.hbox.addWidget(self.group3.labelb)
        self.group3.hbox.addWidget(self.group3.lineb)
        self.group3.hbox.addWidget(self.group3.labelc)
        self.group3.hbox.addWidget(self.group3.linec)
        self.group3.hbox.addWidget(self.group3.labeld)
        self.group3.hbox.addWidget(self.group3.lined)
        self.group3.hbox.addWidget(button)
        self.layout().addWidget(self.group3, 3, 0)
        self.group4 = QGroupBox('Bảng biến thiên của hàm trùng phương y = ax^4 + bx^2 + c')
        self.group4.hbox = QHBoxLayout()
        self.group4.setLayout(self.group4.hbox)
        self.group4.labela = QLabel()
        self.group4.labela.setText('a = ')
        self.group4.labela.setMaximumWidth(20)
        self.group4.linea = QLineEdit()
        self.group4.linea.setText('1')
        self.group4.linea.setMaximumWidth(30)
        self.group4.labelb = QLabel()
        self.group4.labelb.setText('b = ')
        self.group4.labelb.setMaximumWidth(20)
        self.group4.lineb = QLineEdit()
        self.group4.lineb.setText('')
        self.group4.lineb.setMaximumWidth(30)
        self.group4.labelc = QLabel()
        self.group4.labelc.setText('c = ')
        self.group4.labelc.setMaximumWidth(20)
        self.group4.linec = QLineEdit()
        self.group4.linec.setText('')
        self.group4.linec.setMaximumWidth(30)
        button = QPushButton('Xuất code', self)
        button.clicked.connect(self.bbt_trung_phuong)
        self.group4.hbox.addWidget(self.group4.labela)
        self.group4.hbox.addWidget(self.group4.linea)
        self.group4.hbox.addWidget(self.group4.labelb)
        self.group4.hbox.addWidget(self.group4.lineb)
        self.group4.hbox.addWidget(self.group4.labelc)
        self.group4.hbox.addWidget(self.group4.linec)
        self.group4.hbox.addWidget(button)
        self.layout().addWidget(self.group4, 3, 1)
        self.group5 = QGroupBox('Bảng biến thiên của hàm phân thức y = \\dfrac{ax+b}{cx+d}')
        self.group5.grip = QGridLayout()
        self.group5.setLayout(self.group5.grip)
        self.group5.labela = QLabel()
        self.group5.labela.setText('a = ')
        self.group5.labela.setMaximumWidth(20)
        self.group5.linea = QLineEdit()
        self.group5.linea.setText('1')
        self.group5.linea.setMaximumWidth(30)
        self.group5.labelb = QLabel()
        self.group5.labelb.setText('b = ')
        self.group5.labelb.setMaximumWidth(20)
        self.group5.lineb = QLineEdit()
        self.group5.lineb.setText('')
        self.group5.lineb.setMaximumWidth(30)
        self.group5.labelc = QLabel()
        self.group5.labelc.setText('c = ')
        self.group5.labelc.setMaximumWidth(20)
        self.group5.linec = QLineEdit()
        self.group5.linec.setText('1')
        self.group5.linec.setMaximumWidth(30)
        self.group5.labeld = QLabel()
        self.group5.labeld.setText('d = ')
        self.group5.labeld.setMaximumWidth(20)
        self.group5.lined = QLineEdit()
        self.group5.lined.setText('')
        self.group5.lined.setMaximumWidth(30)
        button = QPushButton('Xuất code', self)
        button.clicked.connect(self.bbt_mot_mot)
        self.group5.grip.addWidget(self.group5.labela, 1, 1)
        self.group5.grip.addWidget(self.group5.linea, 1, 2)
        self.group5.grip.addWidget(self.group5.labelb, 1, 3)
        self.group5.grip.addWidget(self.group5.lineb, 1, 4)
        self.group5.grip.addWidget(self.group5.labelc, 2, 1)
        self.group5.grip.addWidget(self.group5.linec, 2, 2)
        self.group5.grip.addWidget(self.group5.labeld, 2, 3)
        self.group5.grip.addWidget(self.group5.lined, 2, 4)
        self.group5.grip.addWidget(button, 2, 5)
        self.layout().addWidget(self.group5, 4, 0)
        self.group6 = QGroupBox('Bảng biến thiên của hàm phân thức y = \\dfrac{ax^2+bx+c}{mx+n}')
        self.group6.grip = QGridLayout()
        self.group6.setLayout(self.group6.grip)
        self.group6.labela = QLabel()
        self.group6.labela.setText('a = ')
        self.group6.labela.setMaximumWidth(20)
        self.group6.linea = QLineEdit()
        self.group6.linea.setText('1')
        self.group6.linea.setMaximumWidth(30)
        self.group6.labelb = QLabel()
        self.group6.labelb.setText('b = ')
        self.group6.labelb.setMaximumWidth(20)
        self.group6.lineb = QLineEdit()
        self.group6.lineb.setText('')
        self.group6.lineb.setMaximumWidth(30)
        self.group6.labelc = QLabel()
        self.group6.labelc.setText('c = ')
        self.group6.labelc.setMaximumWidth(20)
        self.group6.linec = QLineEdit()
        self.group6.linec.setText('')
        self.group6.linec.setMaximumWidth(30)
        self.group6.labelm = QLabel()
        self.group6.labelm.setText('m = ')
        self.group6.labelm.setMaximumWidth(20)
        self.group6.linem = QLineEdit()
        self.group6.linem.setText('1')
        self.group6.linem.setMaximumWidth(30)
        self.group6.labeln = QLabel()
        self.group6.labeln.setText('n = ')
        self.group6.labeln.setMaximumWidth(20)
        self.group6.linen = QLineEdit()
        self.group6.linen.setText('')
        self.group6.linen.setMaximumWidth(30)
        button = QPushButton('Xuất code', self)
        button.clicked.connect(self.bbt_hai_mot)
        self.group6.grip.addWidget(self.group6.labela, 1, 1)
        self.group6.grip.addWidget(self.group6.linea, 1, 2)
        self.group6.grip.addWidget(self.group6.labelb, 1, 3)
        self.group6.grip.addWidget(self.group6.lineb, 1, 4)
        self.group6.grip.addWidget(self.group6.labelc, 1, 5)
        self.group6.grip.addWidget(self.group6.linec, 1, 6)
        self.group6.grip.addWidget(self.group6.labelm, 2, 3)
        self.group6.grip.addWidget(self.group6.linem, 2, 4)
        self.group6.grip.addWidget(self.group6.labeln, 2, 5)
        self.group6.grip.addWidget(self.group6.linen, 2, 6)
        self.group6.grip.addWidget(button, 2, 7)
        self.layout().addWidget(self.group6, 4, 1)
        self.group7 = QGroupBox('Bảng biến thiên của lượng giác y = a sin (bx)')
        self.group7.hbox = QHBoxLayout()
        self.group7.setLayout(self.group7.hbox)
        self.group7.labela = QLabel()
        self.group7.labela.setText('a = ')
        self.group7.labela.setMaximumWidth(20)
        self.group7.linea = QLineEdit()
        self.group7.linea.setText('1')
        self.group7.linea.setMaximumWidth(30)
        self.group7.labelb = QLabel()
        self.group7.labelb.setText('b = ')
        self.group7.labelb.setMaximumWidth(20)
        self.group7.lineb = QLineEdit()
        self.group7.lineb.setText('2')
        self.group7.lineb.setMaximumWidth(30)
        self.group7.labelc = QLabel()
        self.group7.labelc.setText('c = ')
        self.group7.labelc.setMaximumWidth(20)
        self.group7.linec = QLineEdit()
        self.group7.linec.setText('2')
        self.group7.linec.setMaximumWidth(30)
        button = QPushButton('Xuất code', self)
        button.clicked.connect(self.bbt_bac_nhat)
        self.group7.hbox.addWidget(self.group7.labela)
        self.group7.hbox.addWidget(self.group7.linea)
        self.group7.hbox.addWidget(self.group7.labelb)
        self.group7.hbox.addWidget(self.group7.lineb)
        self.group7.hbox.addWidget(self.group7.labelc)
        self.group7.hbox.addWidget(self.group7.linec)
        self.group7.hbox.addWidget(button)
        self.group8 = QGroupBox('Bảng biến thiên của hàm bậc hai y = ax^2 + bx + c')
        self.group8.hbox = QHBoxLayout()
        self.group8.setLayout(self.group8.hbox)
        self.group8.labela = QLabel()
        self.group8.labela.setText('a = ')
        self.group8.labela.setMaximumWidth(20)
        self.group8.linea = QLineEdit()
        self.group8.linea.setText('1')
        self.group8.linea.setMaximumWidth(30)
        self.group8.labelb = QLabel()
        self.group8.labelb.setText('b = ')
        self.group8.labelb.setMaximumWidth(20)
        self.group8.lineb = QLineEdit()
        self.group8.lineb.setText('2')
        self.group8.lineb.setMaximumWidth(30)
        self.group8.labelc = QLabel()
        self.group8.labelc.setText('c = ')
        self.group8.labelc.setMaximumWidth(20)
        self.group8.linec = QLineEdit()
        self.group8.linec.setText('2')
        self.group8.linec.setMaximumWidth(30)
        button = QPushButton('Xuất code', self)
        button.clicked.connect(self.bbt_bac_nhat)
        self.group8.hbox.addWidget(self.group8.labela)
        self.group8.hbox.addWidget(self.group8.linea)
        self.group8.hbox.addWidget(self.group8.labelb)
        self.group8.hbox.addWidget(self.group8.lineb)
        self.group8.hbox.addWidget(self.group8.labelc)
        self.group8.hbox.addWidget(self.group8.linec)
        self.group8.hbox.addWidget(button)
        for group in (self.group1, self.group2, self.group3, self.group4, self.group7, self.group8):
            group.setMaximumHeight(65)

        for group in (self.group5, self.group6):
            group.setMaximumHeight(90)

        self.code = QGroupBox('Code')
        self.code.vbox = QVBoxLayout()
        self.code.setLayout(self.code.vbox)
        self.code.label = QLabel()
        self.code.vbox.addWidget(self.code.label)
        self.copy = QHBoxLayout()
        self.copy1 = QPushButton('Copy (Code Tikz)', self)
        self.copy1.clicked.connect(self.Copy_Code_Tikz)
        self.copy2 = QPushButton('Copy All (book)', self)
        self.copy2.clicked.connect(self.Copy_Full_Tikz)
        self.copy.addWidget(self.copy1)
        self.copy.addWidget(self.copy2)
        self.run = QHBoxLayout()
        self.run1 = QPushButton('PdfLaTeX (book)', self)
        self.run1.clicked.connect(self.Pdflatex_Full_Tikz)
        self.run2 = QPushButton('PdfLaTeX (standalone)', self)
        self.run2.clicked.connect(self.Pdflatex_Copy_Tikz)
        self.run.addWidget(self.run1)
        self.run.addWidget(self.run2)
        self.layout().addWidget(self.code, 6, 0, 1, 2)
        self.layout().addLayout(self.copy, 7, 0)
        self.layout().addLayout(self.run, 7, 1)
        for widget in (self.group1, self.group2, self.group3, self.group4, self.group5, self.group6):
            widget.setMinimumHeight(60)
            widget.setMaximumHeight(60)

        for widget in (self.group5, self.group6):
            widget.setMinimumHeight(90)
            widget.setMaximumHeight(90)

    def bbt_bac_nhat(self):
        try:
            a = get_number_diag(self.group1.linea.text())
            b = get_number_diag(self.group1.lineb.text())
            if a == 0:
                block = 'Hàm số không đổi trên $\\mathbb{R}$.'
            else:
                block = 'Bảng biến thiên của hàm số $y=' + view_dt_bac_nhat((float(a)), (float(b)), x='x') + '$.\n\n'
                block += bbt_bac_nhat_source(a, b)
            self.code.label.setText(block)
        except ValueError as error:
            TB_Error_Input(self, str(error))

    def bbt_bac_hai(self):
        try:
            a = get_number_diag(self.group2.linea.text())
            b = get_number_diag(self.group2.lineb.text())
            c = get_number_diag(self.group2.linec.text())
            block = 'Bảng biến thiên của hàm số $y=' + view_dt_bac_hai(a, b, c, x='x') + '$.\n\n'
            if float(a) == 0:
                block += bbt_bac_nhat_source(b, c)
            else:
                block += bbt_bac_hai_source(a, b, c)
            self.code.label.setText(block)
        except ValueError as error:
            TB_Error_Input(self, str(error))

    def bbt_bac_ba(self):
        try:
            a = get_number_diag(self.group3.linea.text())
            b = get_number_diag(self.group3.lineb.text())
            c = get_number_diag(self.group3.linec.text())
            d = get_number_diag(self.group3.lined.text())
            block = 'Bảng biến thiên của hàm số $y=' + view_dt_bac_ba(a, b, c, d, x='x') + '$.\n\n'
            if float(a) == 0:
                block += bbt_bac_hai_source(b, c, d)
            else:
                block += bbt_bac_ba_source(a, b, c, d)
            if REG_INF == 1:
                for i in (self.group3.linea.text(), self.group3.lineb.text(), self.group3.linec.text(), self.group3.lined.text()):
                    if '/' in i:
                        TB_update_FREE(self, 'Chức năng tính toán phân số hiện đang bị đóng.\n')
                        break
                    elif '.' in i:
                        TB_update_FREE(self, 'Chức năng tính toán phân số hiện đang bị đóng.\n')
                        break
                    else:
                        self.code.label.setText(block)

            else:
                self.code.label.setText(block)
        except ValueError as error:
            TB_Error_Input(self, str(error))

    def bbt_trung_phuong(self):
        try:
            a = get_number_diag(self.group4.linea.text())
            b = get_number_diag(self.group4.lineb.text())
            c = get_number_diag(self.group4.linec.text())
            block = 'Bảng biến thiên của hàm số $y=' + view_dt_bac_bon(a, 0, b, 0, c, x='x') + '$.\n\n'
            if float(a) == 0:
                block += bbt_bac_hai_source(b, 0, d)
            else:
                block += bbt_trung_phuong_source(a, b, c)
            self.code.label.setText(block)
        except ValueError as error:
            TB_Error_Input(self, str(error))

    def bbt_mot_mot(self):
        try:
            a = get_number_diag(self.group5.linea.text())
            b = get_number_diag(self.group5.lineb.text())
            c = get_number_diag(self.group5.linec.text())
            d = get_number_diag(self.group5.lined.text())
            block = bbt_mot_mot_source(a, b, c, d)
            self.code.label.setText(block)
        except ValueError as error:
            TB_Error_Input(self, str(error))

    def bbt_hai_mot(self):
        try:
            a = get_number_diag(self.group6.linea.text())
            b = get_number_diag(self.group6.lineb.text())
            c = get_number_diag(self.group6.linec.text())
            m = get_number_diag(self.group6.linem.text())
            n = get_number_diag(self.group6.linen.text())
            block = 'Bảng biến thiên của hàm số $y=\\dfrac{' + view_dt_bac_hai(a, b, c, x='x') + '}{' + view_dt_bac_nhat(m, n, x='x') + '}$.\n\n'
            block += bbt_hai_mot_source(a, b, c, m, n)
            for i in (self.group6.linea.text(), self.group6.lineb.text(), self.group6.linec.text(), self.group6.linem.text(), self.group6.linen.text()):
                if '/' in i:
                    TB_update_FREE(self, 'Chức năng tính toán phân số hiện đang bị đóng.\n')
                    break
                elif '.' in i:
                    TB_update_FREE(self, 'Chức năng tính toán phân số chưa được hoàn thiện.\n')
                    break
                else:
                    self.code.label.setText(block)

            self.code.label.setText(block)
        except ValueError as error:
            TB_Error_Input(self, str(error))

    def Copy_Code(self):
        text = self.code.label.text()
        QApplication.clipboard().setText(text)

    def Copy_Code_Tikz(self):
        try:
            text1 = self.code.label.text()
            s = text1.index('\n\n')
            text = text1[s + 2:]
            QApplication.clipboard().setText(text)
        except Exception as err:
            QApplication.clipboard().setText('')

    def Copy_Full_Tikz(self):
        text1 = self.code.label.text()
        text = '\\documentclass{book}\n\\usepackage[utf8]{vietnam}\n\\usepackage{amsmath}\n\\usepackage{tkz-tab}\n\\begin{document}\n' + text1 + '\\end{document}'
        QApplication.clipboard().setText(text)

    def Copy_Pdf_Tikz(self):
        text1 = self.code.label.text()
        text = '\\documentclass{standalone}\n\\usepackage{tkz-tab}\n\\begin{document}\n' + text1 + '\\end{document}'
        QApplication.clipboard().setText(text)

    def Pdflatex_Full_Tikz(self):
        try:
            text1 = self.code.label.text()
            text = '\\documentclass{book}\n\\usepackage[utf8]{vietnam}\n\\usepackage{amsmath,amssymb}\n\\usepackage{tkz-tab}\n\\begin{document}\n' + text1 + '\n\\end{document}'
            now = datetime.now()
            tenfile = 'BBT_book_' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second)
            PdfLaTeX('BBT', tenfile, text)
            path='BBT\\' + tenfile + '.pdf'
            if openfile(path)=='Error':
                QMessageBox.critical(self, 'Lỗi','Lỗi mở file '+path)
        except ValueError as error:
            TB_Error_PdfLaTeX(self, str(error))

    def Pdflatex_Copy_Tikz(self):
        try:
            text1 = self.code.label.text()
            s = text1.index('\n\n')
            text2 = text1[s + 2:]
            text = '\\documentclass{standalone}\n\\usepackage[utf8]{vietnam}\n\\usepackage{amsmath,amssymb}\n\\usepackage{tkz-tab}\n\\begin{document}\n' + text2 + '\n\\end{document}'
            now = datetime.now()
            tenfile = 'BBT_standalone_' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second)
            PdfLaTeX('BBT', tenfile, text)
            path='BBT\\' + tenfile + '.pdf'
            if openfile(path)=='Error':
                QMessageBox.critical(self, 'Lỗi','Lỗi mở file '+path)
        except ValueError as err:
            TB_Error_PdfLaTeX(self, str(err))