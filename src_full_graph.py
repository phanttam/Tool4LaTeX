# coding=utf-8
# src_full_graph.py
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

class Full_Graph(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group0 = QGroupBox('Tùy biến trong vẽ bảng biến thiên')
        self.group0.hbox = QHBoxLayout()
        self.group0.setLayout(self.group0.hbox)
        self.group0.check = QCheckBox('Hiển thị công thức hàm', self)
        self.group0.check.setChecked(True)
        self.group0.hbox.addWidget(self.group0.check)
        self.group1 = QGroupBox('Khảo sát hàm bậc nhất y = ax + b')
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
        button.clicked.connect(self.khaosat_bac_nhat)
        self.group1.hbox.addWidget(self.group1.labela)
        self.group1.hbox.addWidget(self.group1.linea)
        self.group1.hbox.addWidget(self.group1.labelb)
        self.group1.hbox.addWidget(self.group1.lineb)
        self.group1.hbox.addWidget(button)
        self.group2 = QGroupBox('Khảo sát hàm bậc hai y = ax^2 + bx + c')
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
        button.clicked.connect(self.khaosat_bac_hai)
        self.group2.hbox.addWidget(self.group2.labela)
        self.group2.hbox.addWidget(self.group2.linea)
        self.group2.hbox.addWidget(self.group2.labelb)
        self.group2.hbox.addWidget(self.group2.lineb)
        self.group2.hbox.addWidget(self.group2.labelc)
        self.group2.hbox.addWidget(self.group2.linec)
        self.group2.hbox.addWidget(button)
        self.group3 = QGroupBox('Khảo sát hàm bậc ba y = ax^3 + bx^2 + cx + d')
        self.group3.hbox = QHBoxLayout()
        self.group3.setLayout(self.group3.hbox)
        self.group3.labela = QLabel()
        self.group3.labela.setText('a = ')
        self.group3.labela.setMaximumWidth(20)
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
        button.clicked.connect(self.khaosat_bac_ba)
        self.group3.hbox.addWidget(self.group3.labela)
        self.group3.hbox.addWidget(self.group3.linea)
        self.group3.hbox.addWidget(self.group3.labelb)
        self.group3.hbox.addWidget(self.group3.lineb)
        self.group3.hbox.addWidget(self.group3.labelc)
        self.group3.hbox.addWidget(self.group3.linec)
        self.group3.hbox.addWidget(self.group3.labeld)
        self.group3.hbox.addWidget(self.group3.lined)
        self.group3.hbox.addWidget(button)
        self.group4 = QGroupBox('Khảo sát hàm trùng phương y = ax^4 + bx^2 + c')
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
        button.clicked.connect(self.khaosat_bac_bon)
        self.group4.hbox.addWidget(self.group4.labela)
        self.group4.hbox.addWidget(self.group4.linea)
        self.group4.hbox.addWidget(self.group4.labelb)
        self.group4.hbox.addWidget(self.group4.lineb)
        self.group4.hbox.addWidget(self.group4.labelc)
        self.group4.hbox.addWidget(self.group4.linec)
        self.group4.hbox.addWidget(button)
        self.group5 = QGroupBox('Khảo sát hàm phân thức y = \\dfrac{ax+b}{cx+d}')
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
        button.clicked.connect(self.khaosat_bac_mot_mot)
        self.group5.grip.addWidget(self.group5.labela, 1, 1)
        self.group5.grip.addWidget(self.group5.linea, 1, 2)
        self.group5.grip.addWidget(self.group5.labelb, 1, 3)
        self.group5.grip.addWidget(self.group5.lineb, 1, 4)
        self.group5.grip.addWidget(self.group5.labelc, 2, 1)
        self.group5.grip.addWidget(self.group5.linec, 2, 2)
        self.group5.grip.addWidget(self.group5.labeld, 2, 3)
        self.group5.grip.addWidget(self.group5.lined, 2, 4)
        self.group5.grip.addWidget(button, 2, 5)
        self.group6 = QGroupBox('Khảo sát hàm phân thức y = \\dfrac{ax^2+bx+c}{mx+n}')
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
        button.clicked.connect(self.khaosat_bac_hai_mot)
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
        self.group7 = QGroupBox('Khảo sát lượng giác y = a sin (bx)')
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
        button.clicked.connect(self.khaosat_bac_nhat)
        self.group7.hbox.addWidget(self.group7.labela)
        self.group7.hbox.addWidget(self.group7.linea)
        self.group7.hbox.addWidget(self.group7.labelb)
        self.group7.hbox.addWidget(self.group7.lineb)
        self.group7.hbox.addWidget(self.group7.labelc)
        self.group7.hbox.addWidget(self.group7.linec)
        self.group7.hbox.addWidget(button)
        self.group8 = QGroupBox('Khảo sát hàm bậc hai y = ax^2 + bx + c')
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
        button.clicked.connect(self.khaosat_bac_nhat)
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
        self.copy1 = QPushButton('Copy Code', self)
        self.copy1.clicked.connect(self.Copy_Code_Tikz)
        self.copy2 = QPushButton('Copy Full - book', self)
        self.copy2.clicked.connect(self.Copy_Full_Tikz)
        self.copy.addWidget(self.copy1)
        self.copy.addWidget(self.copy2)
        self.run = QHBoxLayout()
        self.run1 = QPushButton('PdfLaTeX - book', self)
        self.run1.clicked.connect(self.Pdflatex_Full_Tikz)
        self.run.addWidget(self.run1)
        self.layout().addWidget(self.group1, 2, 0)
        if REG_INF > 0:
            self.layout().addWidget(self.group2, 2, 1)
            self.layout().addWidget(self.group3, 3, 0)
            self.layout().addWidget(self.group4, 3, 1)
            self.layout().addWidget(self.group5, 4, 0)
            self.layout().addWidget(self.group6, 4, 1)
        self.layout().addWidget(self.code, 6, 0, 1, 2)
        self.layout().addLayout(self.copy, 7, 0)
        self.layout().addLayout(self.run, 7, 1)

    def khaosat_bac_nhat(self):
        try:
            a = get_number_diag(self.group1.linea.text())
            b = get_number_diag(self.group1.lineb.text())
            block = 'Khảo sát và vẽ đồ thị hàm số $y=' + view_dt_bac_nhat(a, b, x='x') + "$.\\\\\n\\textit{Lời giải.}\n\\begin{enumerate}[$ \\star $]\n\\item Tập xác định $\\mathscr{D}=\\mathbb{R}.$\n\\item Đạo hàm $y'=" + get_dfrac(a) + sign_ineq(a) + '0, \\forall x\\in\\mathbb{R}$.\n\\item Bảng biến thiên\n'
            block += '\\begin{center}\n' + bbt_bac_nhat_source(a, b) + '\n\\end{center}\n'
            if float(a) > 0:
                tinh_don_dieu = 'đồng biến'
            else:
                tinh_don_dieu = 'nghịch biến'
            block += '\\item Hàm số ' + tinh_don_dieu + ' trên $\\mathbb{R}$.\n\\item Hàm số không có cực trị.\n'
            block += '\\item Đồ thị\n\\begin{center}\n' + dothi_bac_nhat_source(a, b, '', '', '') + '\n\\end{center}\n\\end{enumerate}\n'
            self.code.label.setText(block)
        except Exception as error:
            TB_Error_Input(self, str(error))

    def khaosat_bac_hai(self):
        try:
            a = get_number_diag(self.group2.linea.text())
            b = get_number_diag(self.group2.lineb.text())
            c = get_number_diag(self.group2.linec.text())
            block = 'Khảo sát và vẽ đồ thị hàm số $y=' + view_dt_bac_hai(a, b, c, x='x') + "$.\\\\\n\\textit{Lời giải.}\n\\begin{enumerate}[$ \\star $]\n\\item Tập xác định $\\mathscr{D}=\\mathbb{R}.$\n\\item Đạo hàm $y'=" + view_dt_bac_nhat((2 * a), b, x='x') + "$.\n\\item $y'=0\\Leftrightarrow x=" + get_dfrac(-b / 2 / a) + '$.\n\\item Giới hạn $\\lim\\limits_{x\\to\\pm\\infty}y=' + sign_heso(a) + '\\infty$.\n\\item Bảng biến thiên\n'
            block += '\\begin{center}\n' + bbt_bac_hai_source(a, b, c) + '\n\\end{center}\n'
            xi = -float(b) / 2 / float(a)
            yi = -(float(b) * float(b) - 4 * float(a) * float(c)) / 4 / float(a)
            if a > 0:
                block += '\\item Hàm số đồng biến trên $\\left(' + get_dfrac(xi) + ';+\\infty\\right)$, nghịch biến trên $\\left(-\\infty;' + get_dfrac(xi) + '\\right)$.\n\\item Hàm số đạt cực tiểu tại $x=' + get_dfrac(xi) + '$, $y_{\\textrm{CT}}=' + get_dfrac(yi) + '$.\n'
            else:
                block += '\\item Hàm số đồng biến trên $\\left(-\\infty;' + get_dfrac(xi) + '\\right)$, nghịch biến trên $\\left(' + get_dfrac(xi) + ';+\\infty\\right)$.\n\\item Hàm số đạt cực đại tại $x=' + get_dfrac(xi) + '$, $y_{\\textrm{CĐ}}=' + get_dfrac(yi) + '$.\n'
            block += '\\item Đồ thị\n\\begin{center}\n' + dothi_bac_hai_source(a, b, c, '', '', '') + '\n\\end{center}\n\\end{enumerate}\n'
            self.code.label.setText(block)
        except Exception as error:
            TB_Error_Input(self, str(error))

    def khaosat_bac_ba(self):
        try:
            a = get_number_diag(self.group3.linea.text())
            b = get_number_diag(self.group3.lineb.text())
            c = get_number_diag(self.group3.linec.text())
            d = get_number_diag(self.group3.lined.text())

            def ham_f(x):
                y = float(a) * x * x * x + float(b) * x * x + float(c) * x + float(d)
                return y

            xi = -float(b) / 3 / float(a)
            yi = ham_f(xi)
            Delta = float(b) * float(b) - 3 * float(a) * float(c)
            if Delta > 0:
                x_1, x_2, y_1, y_2 = Calc_CT_bac_ba(a, b, c, d)
            block = 'Khảo sát và vẽ đồ thị hàm số $y=' + view_dt_bac_ba(a, b, c, d, x='x') + "$.\\\\\n\\textit{Lời giải.}\n\\begin{enumerate}[$ \\star $]\n\\item Tập xác định $\\mathscr{D}=\\mathbb{R}.$\n\\item Đạo hàm $y'=" + view_dt_bac_hai((3 * a), (2 * b), c, x='x') + '$.\n'
            if Delta > 0:
                block += "\\item $y'=0\\Leftrightarrow \\hoac{&x=" + frac_dfrac(x_1) + '\\Rightarrow y=' + frac_dfrac(y_1) + '\\\\&x=' + frac_dfrac(x_2) + '\\Rightarrow y=' + frac_dfrac(y_2) + '}$\n'
            else:
                if Delta == 0:
                    block += "\\item $y'=0\\Leftrightarrow x=" + get_dfrac(xi) + '\\Rightarrow y=' + get_dfrac(yi) + '$.\n'
                else:
                    block += "\\item $y'=0\\Rightarrow$ Phương trình vô nghiệm.\n"
            block += '\\item Giới hạn $\\lim\\limits_{x\\to-\\infty}y=' + sign_heso(-a) + '\\infty$, $\\lim\\limits_{x\\to+\\infty}y=' + sign_heso(a) + '\\infty$.\n'
            block += '\\item Bảng biến thiên\n\\begin{center}\n' + bbt_bac_ba_source(a, b, c, d) + '\n\\end{center}\n'
            if Delta > 0:
                if a > 0:
                    block += '\\item Hàm số đồng biến trên $\\left(-\\infty;' + frac_dfrac(x_1) + '\\right)$ và $\\left(' + frac_dfrac(x_2) + ';+\\infty\\right)$, nghịch biến trên $\\left(' + frac_dfrac(x_1) + ';' + frac_dfrac(x_2) + '\\right)$.\n\\item Hàm số đạt cực đại tại $x=' + frac_dfrac(x_1) + '$, $y_{\\textrm{CĐ}}=' + frac_dfrac(y_1) + '$.\n\\item Hàm số đạt cực tiểu tại $x=' + frac_dfrac(x_2) + '$, $y_{\\textrm{CT}}=' + frac_dfrac(y_2) + '$.\n'
                else:
                    block += '\\item Hàm số nghịch biến trên $\\left(-\\infty;' + frac_dfrac(x_1) + '\\right)$ và $\\left(' + frac_dfrac(x_2) + ';+\\infty\\right)$, đồng biến trên $\\left(' + frac_dfrac(x_1) + ';' + frac_dfrac(x_2) + '\\right)$.\n\\item Hàm số đạt cực đại tại $x=' + frac_dfrac(x_2) + '$, $y_{\\textrm{CĐ}}=' + frac_dfrac(y_2) + '$.\n\\item Hàm số đạt cực tiểu tại $x=' + frac_dfrac(x_1) + '$, $y_{\\textrm{CT}}=' + frac_dfrac(y_1) + '$.\n'
            else:
                if a > 0:
                    block += '\\item Hàm số đồng biến trên $\\mathbb{R}$.\n\\item Hàm số không có cực trị.'
                else:
                    block += '\\item Hàm số nghịch biến trên $\\mathbb{R}$.\n\\item Hàm số không có cực trị.'
            block += "\\item Ta có $y''=" + view_dt_bac_nhat((6 * a), (2 * b), x='x') + "$; $y''=0\\Leftrightarrow x=" + get_dfrac(xi) + '\\Rightarrow y=' + get_dfrac(yi) + '$. Điểm uốn $I\\left(' + get_dfrac(xi) + ';' + get_dfrac(yi) + '\\right)$.\n'
            block += '\\item Đồ thị\n\\begin{center}\n' + dothi_bac_ba_source(a, b, c, d, '', '', '') + '\\end{center}\n\\end{enumerate}\n'
            self.code.label.setText(block)
        except Exception as error:
            TB_Error_Input(self, str(error))

    def khaosat_bac_bon(self):
        try:
            a = get_number_diag(self.group4.linea.text())
            b = get_number_diag(self.group4.lineb.text())
            c = get_number_diag(self.group4.linec.text())
            xi = '0'
            yi = float(c)
            if float(a) * float(b) < 0:
                x1 = math.sqrt(-float(b) / float(a) / 2)
                x2 = -math.sqrt(-float(b) / float(a) / 2)
                e = -b / 2 / a
                d = math.sqrt(float(e))
                if float(d) == int(d):
                    x_2 = str(int(d))
                else:
                    if float(4 * a * d) == int(4 * a * d):
                        x_2 = get_frac(d)
                    else:
                        y, z, w = get_sqrt_nor(-2 * a * b, 2 * a)
                        x_2 = ptbh_view(0, y, z, w)
                x_1 = '-' + x_2
                yo = -float(b) ** 2 / 4 / float(a) + float(c)
                y_0 = get_dfrac(yo)
            block = 'Khảo sát và vẽ đồ thị hàm số $y=' + view_dt_bac_bon(a, 0, b, 0, c, x='x') + "$.\\\\\n\\textit{Lời giải.}\n\\begin{enumerate}[$ \\star $]\n\\item Tập xác định $\\mathscr{D}=\\mathbb{R}.$\n\\item Đạo hàm $y'=" + view_dt_bac_ba((4 * a), 0, (2 * b), 0, x='x') + '$.\n'
            if a * b < 0:
                block += "\\item $y'=0\\Leftrightarrow \\hoac{&x=0\\Rightarrow y=" + frac_dfrac(c) + '\\\\&x=\\pm' + x_2 + '\\Rightarrow y=' + y_0 + '}$\n'
            else:
                block += "\\item $y'=0\\Leftrightarrow x=0\\Rightarrow y=" + get_dfrac(c) + '$\n.'
            block += '\\item Giới hạn $\\lim\\limits_{x\\to\\pm\\infty}y=' + sign_heso(a) + '\\infty$.\n\\item Bảng biến thiên\n'
            block += '\\begin{center}\n' + bbt_trung_phuong_source(a, b, c) + '\n\\end{center}\n'
            if a * b < 0:
                print(x_1)
                if a > 0:
                    block += '\\item Hàm số đồng biến trên $\\left(' + frac_dfrac(x_1) + ';0\\right)$ và $\\left(' + frac_dfrac(x_2) + ';+\\infty\\right)$.\n\\item Hàm số nghịch biến trên $\\left(-\\infty;' + frac_dfrac(x_1) + '\\right)$ và $\\left(0;' + frac_dfrac(x_2) + '\\right)$.\n\\item Hàm số đạt cực đại tại $x=0$, $y_{\\textrm{CĐ}}=' + frac_dfrac(c) + '$.\n\\item Hàm số đạt cực tiểu tại $x=\\pm' + frac_dfrac(x_2) + '$, $y_{\\textrm{CT}}=' + y_0 + '$.\n'
                else:
                    block += '\\item Hàm số nghịch biến trên $\\left(' + frac_dfrac(x_1) + ';0\\right)$ và $\\left(' + frac_dfrac(x_2) + ';+\\infty\\right)$.\n\\item Hàm số đồng biến trên $\\left(-\\infty;' + frac_dfrac(x_1) + '\\right)$ và $\\left(0;' + frac_dfrac(x_2) + '\\right)$.\n\\item Hàm số đạt cực tiểu tại $x=0$, $y_{\\textrm{CT}}=' + frac_dfrac(c) + '$.\n\\item Hàm số đạt cực đại tại $x=\\pm' + frac_dfrac(x_2) + '$, $y_{\\textrm{CĐ}}=' + y_0 + '$.\n'
            else:
                if a > 0:
                    block += '\\item Hàm số đồng biến trên $\\left(0;+\\infty\\right)$, nghịch biến trên $\\left(-\\infty;0\\right)$.\n\\item Hàm số đạt cực tiểu tại $x=0$, $y_{\\textrm{CT}}=' + frac_dfrac(c) + '$.\n'
                else:
                    block += '\\item Hàm số đồng biến trên $\\left(-\\infty;0\\right)$, nghịch biến trên $\\left(0;+\\infty\\right)$.\n\\item Hàm số đạt cực đại tại $x=0$, $y_{\\textrm{CĐ}}=' + frac_dfrac(c) + '$.\n'
            block += '\\item Đồ thị\n\\begin{center}\n' + dothi_trung_phuong_source(a, b, c, '', '', '') + '\\end{center}\n\\end{enumerate}\n'
            self.code.label.setText(block)
        except Exception as error:
            TB_Error_Input(self, str(error))

    def khaosat_bac_mot_mot(self):
        try:
            a = get_number_diag(self.group5.linea.text())
            b = get_number_diag(self.group5.lineb.text())
            c = get_number_diag(self.group5.linec.text())
            d = get_number_diag(self.group5.lined.text())
            if a * d - b * c == 0 or c == 0:
                QMessageBox.question(self, 'ERROR', 'Nhập liệu không thỏa điều kiện: $c\\ne0$ và $ad-bc\\ne0$.', QMessageBox.Yes)
            else:

                def ham_f(x):
                    y = (float(a) * x + float(b)) / (float(c) * x + float(d))
                    return y

                xi = round(-float(d) / float(c), 2)
                yi = round(float(a) / float(c), 2)
                x_0 = get_dfrac(-d / c)
                y_0 = get_dfrac(a / c)
                block = 'Khảo sát và vẽ đồ thị hàm số $y=\\dfrac{' + view_dt_bac_nhat(a, b, x='x') + '}{' + view_dt_bac_nhat(c, d, x='x') + '}$.\\\\\n\\textit{Lời giải.}\n\\begin{enumerate}[$ \\star $]\n\\item Tập xác định $\\mathscr{D}=\\mathbb{R}\\setminus\\left\\{' + x_0 + "\\right\\}.$\n\\item Đạo hàm $y'=\\dfrac{" + view_dt_bac_khong(a * d - b * c) + '}{(' + view_dt_bac_nhat(c, d, x='x') + ')^2}' + sign_ineq(a * d - b * c) + '0,\\forall x\\in\\mathscr{D}$.\n'
                block += '\\item Tiệm cận đứng: $x=' + x_0 + '$, vì $\\lim\\limits_{x\\to' + sign_ngoactron(get_frac(-d / c), sign_heso(-d / c)) + '^-}y=' + sign_heso(a * d - b * c) + '\\infty$ và $\\lim\\limits_{x\\to' + sign_ngoactron(get_frac(-d / c), sign_heso(-d / c)) + '^+}y=' + sign_heso(-a * d + b * c) + '\\infty$\n'
                block += '\\item Tiệm cận ngang: $y=' + y_0 + '$, vì $\\lim\\limits_{x\\to\\pm\\infty}y=' + y_0 + '$.\n\\item Bảng biến thiên\n'
                block += '\\begin{center}\n' + bbt_mot_mot_source(a, b, c, d) + '\n\\end{center}\n'
                if a * d - b * c > 0:
                    block += '\\item Hàm số đồng biến trên từng khoảng xác định.\n\\item Hàm số không có cực trị.\n'
                else:
                    block += '\\item Hàm số nghịch biến trên từng khoảng xác định.\n\\item Hàm số không có cực trị.\n'
                block += '\\item Đồ thị\n\\begin{center}\n' + dothi_bac_mot_mot_source(a, b, c, d, '', '', '') + '\\end{center}\n\\end{enumerate}\n'
                self.code.label.setText(block)
        except Exception as error:
            TB_Error_Input(self, str(error))

    def khaosat_bac_hai_mot(self):
        try:
            a = get_number_diag(self.group6.linea.text())
            b = get_number_diag(self.group6.lineb.text())
            c = get_number_diag(self.group6.linec.text())
            m = get_number_diag(self.group6.linem.text())
            n = get_number_diag(self.group6.linen.text())
            if REG_INF < 2:
                QMessageBox.question(self, 'Thông báo', 'Only use for VIP user', QMessageBox.Yes)
            else:
                if m == 0 or (a * (-n / m) ** 2 + b * (-n / m) + c) * n == 0:
                    QMessageBox.question(self, 'ERROR', 'Nhập liệu không thỏa điều kiện hàm phân thức (2/1).', QMessageBox.Yes)
                else:

                    def ham_f(x):
                        y = (float(a) * x ** 2 + float(b) * x + c) / (float(m) * x + float(n))
                        return y

                    x_0 = get_dfrac(-n / m)
                    y_0 = get_dfrac(a / m * (-n / m) + (b * m - a * n) / m ** 2)
                    A = a * m
                    B = a * n
                    C = b * n - c * m
                    Delta = B ** 2 - A * C
                    x_0 = get_dfrac(-n / m)
                    y_0 = get_dfrac(a / m * (-n / m) + (b * m - a * n) / m ** 2)
                    if Delta > 0:
                        x_1, x_2, y_1, y_2 = Calc_CT_hai_mot(a, b, c, m, n)
                    block = 'Khảo sát và vẽ đồ thị hàm số $y=\\dfrac{' + view_dt_bac_hai(a, b, c, x='x') + '}{' + view_dt_bac_nhat(m, n, x='x') + '}$.\\\\\n\\textit{Lời giải.}\n\\begin{enumerate}[$ \\star $]\n\\item Tập xác định $\\mathscr{D}=\\mathbb{R}\\setminus\\left\\{' + x_0 + '\\right\\}$.\n'
                    block += '\\item Tiệm cận đứng: $x=' + x_0 + '$, vì $\\lim\\limits_{x\\to' + sign_ngoactron(get_frac(-n / m), sign_heso(-n / m)) + '^-}y=' + sign_heso(-n / m - 0.001) + '\\infty$ và $\\lim\\limits_{x\\to' + sign_ngoactron(get_frac(-n / m), sign_heso(-n / m)) + '^+}y=' + sign_heso(-n / m + 0.001) + '\\infty$.\n'
                    block += '\\item Tiệm cận xiên: $y=' + view_dt_bac_nhat((a / m), ((b * m - a * n) / m ** 2), x='x') + '$, vì $y=' + view_dt_bac_nhat((a / m), ((b * m - a * n) / m ** 2), x='x') + '+\\dfrac{' + view_dt_bac_khong(a * (-n / m) ** 2 + b * (-n / m) + c) + '}{' + view_dt_bac_nhat(m, n, x='x') + '}$ và $\\lim\\limits_{x\\to\\pm\\infty}\\dfrac{' + view_dt_bac_khong(a * (-n / m) ** 2 + b * (-n / m) + c) + '}{' + view_dt_bac_nhat(m, n, x='x') + '}=0$.\n'
                    block += "\\item Đạo hàm $y'=\\dfrac{" + view_dt_bac_hai((a * m), (2 * a * n), (b * n - c * m), x='x') + '}{(' + view_dt_bac_nhat(m, n, x='x') + ')^2}$.\n'
                    if Delta < 0:
                        block += "\\item $y'=0\\Leftrightarrow " + view_dt_bac_hai((a * m), (2 * a * n), (b * n - c * m), x='x') + '\\Rightarrow$ Phương trình vô nghiệm.\n'
                        if a * m > 0:
                            tinh_don_dieu = '\\item Hàm số đồng biến trên từng khoảng xác định.\n\\item Hàm số không có cực trị.\n'
                        else:
                            tinh_don_dieu = '\\item Hàm số nghịch biến trên từng khoảng xác định.\n\\item Hàm số không có cực trị.\n'
                    else:
                        if Delta == 0:
                            QMessageBox.question(self, 'ERROR', 'Nhập liệu không thỏa điều kiện, hãy nhập một hàm khác', QMessageBox.Yes)
                        else:
                            if a * m > 0:
                                tinh_don_dieu = '\\item Hàm số đồng biến trên $\\left(-\\infty;' + frac_dfrac(x_1) + '\\right)$ và $\\left(' + frac_dfrac(x_2) + ';+\\infty\\right)$.\n\\item Hàm số nghịch biến trên $\\left(' + frac_dfrac(x_1) + ';' + x_0 + '\\right)$ và $\\left(' + x_0 + ';' + frac_dfrac(x_2) + '\\right)$.\n\\item Hàm số đạt cực đại tại $x=' + frac_dfrac(x_1) + '$, $y_{\\textrm{CĐ}}=' + frac_dfrac(y_1) + '$.\n\\item Hàm số đạt cực tiểu tại $x=' + frac_dfrac(x_2) + '$, $y_{\\textrm{CT}}=' + frac_dfrac(y_2) + '$.\n'
                            else:
                                tinh_don_dieu = '\\item Hàm số nghịch biến trên $\\left(-\\infty;' + frac_dfrac(x_1) + '\\right)$ và $\\left(' + frac_dfrac(x_2) + ';+\\infty\\right)$.\n\\item Hàm số đồng biến trên $\\left(' + frac_dfrac(x_1) + ';' + x_0 + '\\right)$ và $\\left(' + x_0 + ';' + frac_dfrac(x_2) + '\\right)$.\n\\item Hàm số đạt cực tiểu tại $x=' + frac_dfrac(x_1) + '$, $y_{\\textrm{CT}}=' + frac_dfrac(y_1) + '$.\n\\item Hàm số đạt cực đại tại $x=' + frac_dfrac(x_2) + '$, $y_{\\textrm{CĐ}}=' + frac_dfrac(y_2) + '$.\n'
                            block += "\\item $y'=0\\Leftrightarrow \\hoac{&x=" + frac_dfrac(x_1) + '\\Rightarrow y=' + frac_dfrac(y_1) + '\\\\&x=' + frac_dfrac(x_2) + '\\Rightarrow y=' + frac_dfrac(y_2) + '}$\n'
                    block += '\\item Giới hạn $\\lim\\limits_{x\\to-\\infty}y=' + sign_heso(-a / m) + '\\infty$, $\\lim\\limits_{x\\to+\\infty}y=' + sign_heso(a / m) + '\\infty$.\n'
                    block += '\\item Bảng biến thiên\n\\begin{center}\n' + bbt_hai_mot_source(a, b, c, m, n) + '\n\\end{center}\n'
                    block += tinh_don_dieu
                    block += '\\item Đồ thị\n\\begin{center}\n' + dothi_bac_hai_mot_source(a, b, c, m, n, '', '', '') + '\n\\end{center}\n\\end{enumerate}\n'
                    self.code.label.setText(block)
        except Exception as error:
            TB_Error_Input(self, str(error))

    def Copy_Code(self):
        text = self.code.label.text()
        QApplication.clipboard().setText(text)

    def Copy_Code_Tikz(self):
        if REG_INF > 1:
            text = self.code.label.text()
            QApplication.clipboard().setText(text)
        else:
            QMessageBox.question(self, 'Thông báo', 'Bạn cần đăng kí thông tin để sử dụng.\nCác bạn vào tab Thông tin.\nĐiền đủ 3 thông tin.\nNhấn tạo file đăng kí.\nNhấn Gửi file đăng kí\nĐính kèm file ten-sdt.tex inbox cho tác giả.', QMessageBox.Yes)

    def Copy_Full_Tikz(self):
        if REG_INF > 1:
            text1 = self.code.label.text()
            text = '\\documentclass{book}\n\\usepackage[utf8]{vietnam}\n\\usepackage{amsmath,amssymb,mathrsfs,enumerate}\n\\usepackage{tkz-tab,tkz-euclide}\n\\newcommand{\\hoac}[1]{\\left[\\begin{aligned}#1\\end{aligned}\\right.}\n\\begin{document}\n' + text1 + '\\end{document}'
            QApplication.clipboard().setText(text)
        else:
            QMessageBox.question(self, 'Thông báo', 'Bạn cần đăng kí thông tin để sử dụng.\nCác bạn vào tab Thông tin.\nĐiền đủ 3 thông tin.\nNhấn tạo file đăng kí.\nNhấn Gửi file đăng kí\nĐính kèm file ten-sdt.tex inbox cho tác giả.', QMessageBox.Yes)

    def Copy_Pdf_Tikz(self):
        text1 = self.code.label.text()
        text = '\\documentclass{standalone}\n\\usepackage{tkz-tab}\n\\begin{document}\n' + text1 + '\\end{document}'
        QApplication.clipboard().setText(text)

    def Pdflatex_Full_Tikz(self):
        text1 = self.code.label.text()
        text = '\\documentclass{book}\n\\usepackage[utf8]{vietnam}\n\\usepackage{amsmath,amssymb,mathrsfs,enumerate}\n\\usepackage{tkz-tab,tkz-euclide}\n\\newcommand{\\hoac}[1]{\\left[\\begin{aligned}#1\\end{aligned}\\right.}\n\\begin{document}\n' + text1 + '\\end{document}'
        now = datetime.now()
        tenfile = 'KHAOSAT_book_' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second)
        PdfLaTeX('KHAOSAT', tenfile, text)
        path='KHAOSAT\\' + tenfile + '.pdf'
        if openfile(path)=='Error':
            QMessageBox.critical(self, 'Lỗi','Lỗi mở file '+path)

    def Pdflatex_Copy_Tikz(self):
        try:
            text1 = self.code.label.text()
            s = text1.index('\n\n')
            text2 = text1[s + 2:]
        except Exception as err:
            text2 = ''

        text = '\\documentclass{standalone}\n\n\\usepackage{tkz-tab}\n\\begin{document}\n' + text2 + '\\end{document}'
        now = datetime.now()
        tenfile = 'KHAOSAT_standalone_' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second)
        PdfLaTeX('KHAOSAT', tenfile, text)
        path='KHAOSAT\\' + tenfile + '.pdf'
        if openfile(path)=='Error':
            QMessageBox.critical(self, 'Lỗi','Lỗi mở file '+path)