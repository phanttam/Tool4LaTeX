# coding=utf-8
# src_mix.py
import re, os, sys, csv, codecs, time
from datetime import datetime, timedelta
from urllib.request import urlopen
import math, argparse, subprocess, signal, shutil, errno, unicodedata, webbrowser
from fractions import Fraction
from decimal import Decimal
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from def_calculation import *
from src_reg import *
from def_bbt import *
from def_id import *
from def_convert import *
from def_ban_quyen import *
from def_bank import *
from def_matrix import *
from def_mix import *

class Mix_Test(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        try:
            with codecs.open('Mixed Test//Mau-100-cau.tex', 'w', 'utf8') as (f):
                for i in range(0, 25):
                    f.write('\\begin{ex}\nCâu số ' + str(4 * i + 1) + '\n\\choice\n{\\True Đúng}\n{Sai 1}\n{Sai 2}\n{Sai 3}\n\\loigiai{\nLời giải câu số ' + str(4 * i + 1) + '\n}\n\\end{ex}\n\n\\begin{ex}\nCâu số ' + str(4 * i + 2) + '\n\\choice\n{Sai 1}\n{\\True Đúng}\n{Sai 2}\n{Sai 3}\n\\loigiai{\nLời giải câu số ' + str(4 * i + 2) + '\n}\n\\end{ex}\n\n\\begin{ex}\nCâu số ' + str(4 * i + 3) + '\n\\choice\n{Sai 1}\n{Sai 2}\n{\\True Đúng}\n{Sai 3}\n\\loigiai{\nLời giải câu số ' + str(4 * i + 3) + '\n}\n\\end{ex}\n\n\\begin{ex}\nCâu số ' + str(4 * i + 4) + '\n\\choice\n{Sai 1}\n{Sai 2}\n{Sai 3}\n{\\True Đúng}\n\\loigiai{\nLời giải câu số ' + str(4 * i + 4) + '\n}\n\\end{ex}\n')

                f.close()
        except Exception as er:
            pass

        self.setLayout(QGridLayout())
        self.group = QGroupBox('Thông tin về dữ liệu của nguồn để trộn đề')
        self.group.vbox = QVBoxLayout()
        self.group.hbox = QHBoxLayout()
        self.group.hboxhd = QHBoxLayout()
        self.group.check = QCheckBox('HD')
        self.group.check.setChecked(True)
        self.group.hd = QGroupBox('Hướng dẫn')
        self.group.hboxhd.addWidget(self.group.check)
        self.group.hboxhd.addWidget(self.group.hd)
        self.group.hbox1 = QHBoxLayout()
        self.group.label1 = QLabel('Chọn đề')
        self.group.label1.setMinimumWidth(30)
        self.group.line1 = QLineEdit()
        self.group.button0 = QPushButton('Hướng dẫn')
        self.group.button0.clicked.connect(self.G1_HD)
        self.group.button1 = QPushButton('Chọn')
        self.group.button1.clicked.connect(self.G1_get_file_1)
        self.group.button2 = QPushButton('In thông tin dữ liệu nguồn')
        self.group.button2.clicked.connect(self.G1_get_file_2)
        self.group.grip = QGridLayout()
        self.group.grip.label1 = QLabel('Tổng số câu')
        self.group.grip.label2 = QLabel()
        self.group.grip.label11 = QLabel('Lớp 10')
        self.group.grip.label12 = QLabel()
        self.group.grip.label13 = QLabel('Lớp 11')
        self.group.grip.label14 = QLabel()
        self.group.grip.label15 = QLabel('Lớp 12')
        self.group.grip.label16 = QLabel()
        self.group.grip.label17 = QLabel('[D] Đại')
        self.group.grip.label18 = QLabel()
        self.group.grip.label19 = QLabel('[H] Hình')
        self.group.grip.label110 = QLabel()
        self.group.grip.addWidget(self.group.grip.label1, 1, 1)
        self.group.grip.addWidget(self.group.grip.label2, 1, 2)
        self.group.grip.addWidget(self.group.grip.label11, 2, 1)
        self.group.grip.addWidget(self.group.grip.label12, 2, 2)
        self.group.grip.addWidget(self.group.grip.label13, 2, 3)
        self.group.grip.addWidget(self.group.grip.label14, 2, 4)
        self.group.grip.addWidget(self.group.grip.label15, 2, 5)
        self.group.grip.addWidget(self.group.grip.label16, 2, 6)
        self.group.grip.addWidget(self.group.grip.label17, 1, 3)
        self.group.grip.addWidget(self.group.grip.label18, 1, 4)
        self.group.grip.addWidget(self.group.grip.label19, 1, 5)
        self.group.grip.addWidget(self.group.grip.label110, 1, 6)
        self.group.hbox2 = QHBoxLayout()
        self.group.hbox2.label1 = QLabel('Ngân hàng đề')
        self.group.hbox2.label1.setMinimumWidth(30)
        self.group.radio1 = QRadioButton('Ngân hàng Offline')
        self.group.radio2 = QRadioButton('Ngân hàng cá nhân')
        self.group.radio2.setChecked(True)
        self.group.hbox2.line1 = QLineEdit('')
        self.group.hbox1 = QHBoxLayout()
        self.group.table = QTableWidget(self)
        self.group.table.setColumnCount(9)
        item0 = QtWidgets.QTableWidgetItem('Mã ID')
        item0.setBackground(QColor(255, 0, 0))
        self.group.table.setHorizontalHeaderItem(0, item0)
        item1 = QtWidgets.QTableWidgetItem('Bài/Dạng')
        item1.setBackground(QColor(255, 0, 0))
        self.group.table.setHorizontalHeaderItem(1, item1)
        item2 = QtWidgets.QTableWidgetItem('Opt')
        item2.setBackground(QColor(255, 0, 0))
        self.group.table.setHorizontalHeaderItem(2, item2)
        item3 = QtWidgets.QTableWidgetItem('[Y]')
        item3.setBackground(QtCore.Qt.red)
        self.group.table.setHorizontalHeaderItem(3, item3)
        item4 = QtWidgets.QTableWidgetItem('[B]')
        item4.setBackground(QColor(255, 0, 0))
        self.group.table.setHorizontalHeaderItem(4, item4)
        item5 = QtWidgets.QTableWidgetItem('[K]')
        item5.setBackground(QColor(255, 0, 0))
        self.group.table.setHorizontalHeaderItem(5, item5)
        item6 = QtWidgets.QTableWidgetItem('[G]')
        item6.setBackground(QColor(255, 0, 0))
        self.group.table.setHorizontalHeaderItem(6, item6)
        item7 = QtWidgets.QTableWidgetItem('[T]')
        item7.setBackground(QColor(255, 0, 0))
        self.group.table.setHorizontalHeaderItem(7, item7)
        item8 = QtWidgets.QTableWidgetItem('Tổng')
        item8.setBackground(QColor(255, 0, 0))
        self.group.table.setHorizontalHeaderItem(8, item8)
        font = QFont()
        font.setBold(True)
        item3.setForeground(QBrush(Qt.darkCyan))
        item4.setForeground(QBrush(Qt.blue))
        item5.setForeground(QBrush(Qt.darkYellow))
        item6.setForeground(QBrush(Qt.red))
        item7.setForeground(QBrush(Qt.darkGreen))
        item3.setFont(font)
        item4.setFont(font)
        item5.setFont(font)
        item6.setFont(font)
        item7.setFont(font)
        item8.setFont(font)
        self.group.table.setColumnWidth(0, 65)
        self.group.table.setColumnWidth(2, 5)
        self.group.table.setColumnWidth(1, 260)
        self.group.table.setMaximumHeight(300)
        for x in range(2, 9):
            self.group.table.setColumnWidth(x, 35)

        self.group.hbox3 = QHBoxLayout()
        self.group.label31 = QLabel('Số câu')
        self.group.label31.setMinimumWidth(30)
        self.group.combo1 = QComboBox()
        self.group.combo1.setStyleSheet("QComboBox { combobox-popup: 0; }")
        if REG_INF == 1:
            Max_cau = 25
        if REG_INF == 2:
            Max_cau = 50
        else:
            Max_cau = 100
        for i in range(0, Max_cau):
            self.group.combo1.addItem(str(i + 1))

        self.group.label33 = QLabel('Số đề')
        self.group.label33.setMinimumWidth(30)
        self.group.combo2 = QComboBox()
        self.group.combo2.setStyleSheet("QComboBox { combobox-popup: 0; }")
        if REG_INF == 1:
            Max_de = 2
        if REG_INF == 2:
            Max_de = 8
        else:
            Max_de = 24
        for i in range(0, Max_de):
            self.group.combo2.addItem(str(i + 1))

        self.group.label34 = QLabel('Lưu tên file')
        self.group.label34.setMinimumWidth(30)
        self.group.line3 = QLineEdit()
        self.group.radiobuild = QRadioButton('Biên dịch đề')
        self.group.radiobuild.setChecked(True)
        self.group.button3 = QPushButton('Khởi tạo đề')
        self.group.button3.clicked.connect(self.G1_get_file_3)
        self.group.hbox3.addWidget(self.group.label31)
        self.group.hbox3.addWidget(self.group.combo1)
        self.group.hbox3.addWidget(self.group.label33)
        self.group.hbox3.addWidget(self.group.combo2)
        self.group.hbox3.addWidget(self.group.label34)
        self.group.hbox3.addWidget(self.group.line3)
        self.group.hbox3.addWidget(self.group.radiobuild)
        self.group.hbox3.addWidget(self.group.button3)
        self.group.hbox.addWidget(self.group.label1)
        self.group.hbox.addWidget(self.group.line1)
        self.group.hbox.addWidget(self.group.button0)
        self.group.hbox.addWidget(self.group.button1)
        self.group.hbox1.addWidget(self.group.table)
        self.group.hbox2.addWidget(self.group.radio2)
        self.group.hbox2.addWidget(self.group.radio1)
        self.group.option = QGridLayout()
        self.group.option1 = QGroupBox('Kiểu đáp án.')
        self.group.option1.setLayout(QGridLayout())
        self.group.option1.radio1 = QRadioButton('Ngẫu nhiên')
        self.group.option1.radio1.setChecked(True)
        self.group.option1.radio2 = QRadioButton('Tất cả đáp án A')
        self.group.option1.radio3 = QRadioButton('Chia đều đáp án')
        self.group.option1.radio4 = QRadioButton('Giữ phương án cũ')
        self.group.option1.layout().addWidget(self.group.option1.radio1, 1, 1)
        self.group.option1.layout().addWidget(self.group.option1.radio2, 1, 2)
        self.group.option1.layout().addWidget(self.group.option1.radio3, 1, 3)
        self.group.option1.layout().addWidget(self.group.option1.radio4, 1, 4)
        self.group.option.addWidget(self.group.option1, 1, 1)
        self.group.option2 = QGroupBox('Trộn đề theo block')
        self.group.option2.setChecked(False)
        self.group.option2.clicked.connect(self.Option2_isCheck)
        self.group.option2.setLayout(QGridLayout())
        self.group.option2.radio0 = QRadioButton('Ngẫu nhiên')
        self.group.option2.radio0.setChecked(True)
        self.group.option2.radio1 = QRadioButton('Giữ thứ tự câu')
        self.group.option2.radio2 = QRadioButton('[Y][B][K][G][T]')
        self.group.option2.radio3 = QRadioButton('[Y,B][K,G,T]')
        self.group.option2.radio4 = QRadioButton('[10][11][12]')
        self.group.option2.radio5 = QRadioButton('[D][H]')
        self.group.option2.layout().addWidget(self.group.option2.radio0, 1, 0)
        self.group.option2.layout().addWidget(self.group.option2.radio1, 1, 1)
        self.group.option.addWidget(self.group.option2, 2, 1)
        self.group.option3 = QGroupBox('Tùy chọn in đáp án PDF')
        self.group.option3.setCheckable(True)
        self.group.option3.setChecked(False)
        self.group.option3.clicked.connect(self.Option3_isCheck)
        self.group.option3.setLayout(QGridLayout())
        self.group.option3.radio1 = QRadioButton('Không in')
        self.group.option3.radio2 = QRadioButton('Form Ex_test')
        self.group.option3.radio2.setChecked(True)
        self.group.option3.radio3 = QRadioButton('Form Dethi')
        self.group.option3.radio4 = QRadioButton('Chấm tay')
        self.group.option3.radio5 = QRadioButton('Zipgrade')
        self.group.option3.radio6 = QRadioButton('TNMaker')
        self.group.option3.radio7 = QRadioButton('789.vn')
        self.group.option3.layout().addWidget(self.group.option3.radio1, 1, 1)
        self.group.option3.layout().addWidget(self.group.option3.radio2, 1, 2)
        self.group.option3.layout().addWidget(self.group.option3.radio3, 1, 3)
        self.group.option3.layout().addWidget(self.group.option3.radio4, 1, 4)
        self.group.option3.layout().addWidget(self.group.option3.radio5, 1, 5)
        self.group.option3.layout().addWidget(self.group.option3.radio6, 1, 6)
        self.group.option3.layout().addWidget(self.group.option3.radio7, 1, 7)
        self.group.option.addWidget(self.group.option3, 3, 1)
        self.group.option4 = QGroupBox('Tùy chọn lưu đáp án Excel')
        self.group.option4.setCheckable(True)
        self.group.option4.setChecked(False)
        self.group.option4.clicked.connect(self.Option4_isCheck)
        self.group.option4.setLayout(QGridLayout())
        self.group.option4.radio1 = QRadioButton('Không tạo file Excel')
        self.group.option4.radio1.setChecked(True)
        self.group.option4.radio2 = QRadioButton('Đáp án theo bảng dọc')
        self.group.option4.radio3 = QRadioButton('Đáp án theo bảng ngang')
        self.group.option4.radio4 = QRadioButton('Form BTN')
        self.group.option4.layout().addWidget(self.group.option4.radio1, 1, 1)
        self.group.option4.layout().addWidget(self.group.option4.radio2, 1, 2)
        self.group.option4.layout().addWidget(self.group.option4.radio3, 1, 3)
        self.group.option4.layout().addWidget(self.group.option4.radio4, 1, 4)
        self.group.option.addWidget(self.group.option4, 4, 1)
        self.group.optionn = QGroupBox('Làm tiêu đề (\\lamtieude)')
        self.group.optionn.setLayout(QGridLayout())
        self.group.optionn.form1 = QFormLayout()
        self.group.optionn.form2 = QFormLayout()
        self.group.optionn.line1 = QLineEdit()
        self.group.optionn.line2 = QLineEdit()
        self.group.optionn.line3 = QComboBox()
        self.group.optionn.line3.addItem('Đề thi có \\@scau\\, câu/\\@strang\\, trang.')
        self.group.optionn.line4 = QLineEdit()
        self.group.optionn.line5 = QLineEdit()
        self.group.optionn.line6 = QComboBox()
        self.group.optionn.line6.setStyleSheet("QComboBox { combobox-popup: 0; }")
        for i in range(1, 37):
            self.group.optionn.line6.addItem(str(i * 5))

        self.group.optionn.form1.addRow('\\tentruong', self.group.optionn.line1)
        self.group.optionn.form1.addRow('\\tenkhoa', self.group.optionn.line2)
        self.group.optionn.form1.addRow('\\loaidethi', self.group.optionn.line3)
        self.group.optionn.form2.addRow('\\tenkythi', self.group.optionn.line4)
        self.group.optionn.form2.addRow('\\tenmonhoc', self.group.optionn.line5)
        self.group.optionn.form2.addRow('\\thoigian', self.group.optionn.line6)
        self.group.optionn.layout().addLayout(self.group.optionn.form1, 1, 1)
        self.group.optionn.layout().addLayout(self.group.optionn.form2, 1, 2)
        self.group.option.addWidget(self.group.optionn, 5, 1)
        try:
            tieude = codecs.open('Setting//lamtieude.tex', 'r', 'utf-8').read()
            data = re.findall('\\\\newcommand{\\\\@ttruong}{(.*?)}\\s*\\\\newcommand{\\\\@tkhoa}{(.*?)}\\n\\\\newcommand{\\\\@ldethi}{(.*?)}\\n\\\\newcommand{\\\\@tkythi}{(.*?)}\\n\\\\newcommand{\\\\@tmonhoc}{(.*?)}\\n\\\\newcommand{\\\\@tgian}{(.*?)}', tieude, re.DOTALL)
            self.group.optionn.line1.setText(data[0][0])
            self.group.optionn.line2.setText(data[0][1])
            self.group.optionn.line3.setCurrentText(data[0][2])
            self.group.optionn.line4.setText(data[0][3])
            self.group.optionn.line5.setText(data[0][4])
            self.group.optionn.line6.setCurrentText(data[0][5])
        except Exception as er:
            self.group.optionn.line1.setText('Sở GD\\&ĐT TP. Hồ Chí Minh')
            self.group.optionn.line2.setText('THPT Trần Hưng Đạo')
            self.group.optionn.line3.setCurrentText('Đề thi có \\lastpage trang')
            self.group.optionn.line4.setText('Đề thi thử THPT Quốc Gia năm 2019')
            self.group.optionn.line5.setText('Môn Toán')
            self.group.optionn.line6.setCurrentText('90')

        self.group.optionm = QGroupBox('Mã đề')
        self.group.optionm.setLayout(QGridLayout())
        self.group.optionm.radio1 = QRadioButton('xxx')
        self.group.optionm.radio1.setChecked(True)
        self.group.optionm.radio2 = QRadioButton('[1]xx')
        self.group.optionm.radio3 = QRadioButton('xx[1]')
        self.group.optionm.radio4 = QRadioButton('xxx+1')
        self.group.optionm.combo = QComboBox()
        self.group.optionm.combo.setStyleSheet("QComboBox { combobox-popup: 0; }")
        for i in range(0, 1000):
            self.group.optionm.combo.addItem(str(i))

        self.group.optionm.radio5 = QRadioButton('Nhập tay')
        self.group.optionm.line = QLineEdit()
        self.group.optionm.line.setMaximumWidth(100)
        self.group.optionm.layout().addWidget(self.group.optionm.radio1, 1, 1)
        self.group.optionm.layout().addWidget(self.group.optionm.radio2, 1, 2)
        self.group.optionm.layout().addWidget(self.group.optionm.radio3, 1, 3)
        self.group.optionm.layout().addWidget(self.group.optionm.radio4, 1, 4)
        self.group.optionm.layout().addWidget(self.group.optionm.combo, 1, 5)
        self.group.optionm.layout().addWidget(self.group.optionm.radio5, 1, 6)
        self.group.optionm.layout().addWidget(self.group.optionm.line, 1, 7)
        self.group.option.addWidget(self.group.optionm, 6, 1)
        self.group.setLayout(self.group.vbox)
        self.group.vbox.addLayout(self.group.hbox)
        self.group.vbox.addLayout(self.group.grip)
        self.group.vbox.addLayout(self.group.hbox1)
        self.group.vbox.addLayout(self.group.option)
        self.group.vbox.addLayout(self.group.hbox3)
        self.group2 = QGroupBox('baitracnghiem form (dethi3.5) to Ex_test')
        self.group7 = QGroupBox('Update to be continue')
        self.group7.setMinimumHeight(150)
        self.group7 = QGroupBox('Update to be continue')
        self.group7.setMinimumHeight(150)
        self.layout().addWidget(self.group, 0, 1)
        self.group.setMinimumHeight(200)
        self.group7.setMinimumHeight(100)

    def G1_HD(self):
        Form_question = 'Bước 1: Nhấn chọn một file.\nBước 2: Nhấn Lưu và in ma trận đề.'
        QMessageBox.question(self, 'Hướng dẫn', Form_question, QMessageBox.Yes)

    def G1_get_file_1(self):
        try:
            if self.group.line1.text() == '':
                fname = QFileDialog.getOpenFileName()
                self.group.line1.setText(fname[0])
            List_file = self.group.line1.text()
            List = []
            for file in List_creat(List_file):
                List += Random_GetListEX_FromFile(file)

            Max = len(List)
            if REG_INF == 1:
                Max_cau = min(25, Max)
            if REG_INF == 2:
                Max_cau = min(50, Max)
            else:
                Max_cau = Max
            self.group.combo1.clear()
            for i in range(0, Max_cau):
                self.group.combo1.addItem(str(i + 1))

        except Exception as er:
            TB_Error_TQ(self, str(er))

    def G1_get_file_2(self):
        start_time = time.time()
        type_arrange = ['Y', 'B', 'K', 'G', 'T']
        filename = self.group.line1.text()
        if filename == '':
            QMessageBox.question(self, 'Thông báo', 'Bạn chưa chọn file', QMessageBox.Yes)
        else:
            try:
                ID_loi = []
                list_ID = ID_get_list(filename)
                list_ID_n = ID_arrange_bai(list_ID, type_arrange)
                for ID1 in list_ID:
                    if ID1 not in list_ID_n:
                        ID_loi.append(ID1)

                block = ''
                Matrix_info = Matrix_Get_List(self.group.line1.text())
                General_info = Bank_General_Information(Matrix_info)
                Mucdo = General_info[0]
                TQ = General_info[1]
                font = QFont()
                font.setBold(True)
                self.group.grip.label2.setText(Mucdo[5])
                self.group.grip.label12.setText(TQ[0] + ' (' + str(round(float(TQ[0]) * 100 / float(Mucdo[5]) + 0.01, 1)) + '%)')
                self.group.grip.label14.setText(TQ[1] + ' (' + str(round(float(TQ[1]) * 100 / float(Mucdo[5]) + 0.01, 1)) + '%)')
                self.group.grip.label16.setText(TQ[2] + ' (' + str(round(float(TQ[2]) * 100 / float(Mucdo[5]) + 0.01, 1)) + '%)')
                self.group.grip.label18.setText(TQ[3] + ' (' + str(round(float(TQ[3]) * 100 / float(Mucdo[5]) + 0.01, 1)) + '%)')
                self.group.grip.label110.setText(TQ[4] + ' (' + str(round(float(TQ[4]) * 100 / float(Mucdo[5]) + 0.01, 1)) + '%)')
                self.group.grip.label2.setFont(font)
                self.group.grip.label12.setFont(font)
                self.group.grip.label14.setFont(font)
                self.group.grip.label16.setFont(font)
                self.group.grip.label18.setFont(font)
                self.group.grip.label110.setFont(font)
                Data = ID_thong_ke_ma_tran_ID6(filename, list_ID_n)
                i = 0
                j = 0
                self.group.table.setRowCount(len(Data))
                for ID in Data[-1:] + Data[:-1]:
                    for j in range(0, 9):
                        self.group.table.setItem(i, j, QTableWidgetItem(ID[j]))

                    item3 = QTableWidgetItem(ID[3])
                    item4 = QTableWidgetItem(ID[4])
                    item5 = QTableWidgetItem(ID[5])
                    item6 = QTableWidgetItem(ID[6])
                    item7 = QTableWidgetItem(ID[7])
                    item8 = QTableWidgetItem(ID[8])
                    item3.setForeground(QBrush(Qt.darkCyan))
                    item4.setForeground(QBrush(Qt.blue))
                    item5.setForeground(QBrush(Qt.darkYellow))
                    item6.setForeground(QBrush(Qt.red))
                    item7.setForeground(QBrush(Qt.darkGreen))
                    for item in (item3, item4, item5, item6, item7, item8):
                        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                    font = QFont()
                    font.setBold(True)
                    item3.setFont(font)
                    item4.setFont(font)
                    item5.setFont(font)
                    item6.setFont(font)
                    item7.setFont(font)
                    item8.setFont(font)
                    self.group.table.setItem(i, 3, item3)
                    self.group.table.setItem(i, 4, item4)
                    self.group.table.setItem(i, 5, item5)
                    self.group.table.setItem(i, 6, item6)
                    self.group.table.setItem(i, 7, item7)
                    self.group.table.setItem(i, 8, item8)
                    i += 1

                with codecs.open('Temp\\Matran.tex', 'w', 'utf-8') as (f):
                    for ID in Matrix_info:
                        f.write(ID[0] + ',' + ID[1] + ',' + ID[2] + ',' + ID[3] + ',' + ID[4] + ',' + ID[5] + ',' + ID[6] + '\n')

                    f.close()
            except Exception as er:
                QMessageBox.question(self, 'Thông báo', 'Chương trình xảy ra lỗi.\nVui lòng hãy kiểm tra chuẩn hóa file đã chọn.', QMessageBox.Yes)

    def G1_get_file_3(self):
        start_time = time.time()
        if 1 == 1:
            type_arrange = [
             'Y', 'B', 'K', 'G', 'T']
            filename = List_creat(self.group.line1.text())
            if filename[0] == '':
                QMessageBox.question(self, 'Thông báo', 'Bạn chưa chọn file', QMessageBox.Yes)
            else:
                if 1 == 1:
                    so_cau = int(self.group.combo1.currentText())
                    so_de = int(self.group.combo2.currentText())
                    if self.group.option1.radio1.isChecked():
                        option1 = 'A'
                    else:
                        if self.group.option1.radio2.isChecked():
                            option1 = 'B'
                        else:
                            if self.group.option1.radio3.isChecked():
                                option1 = 'C'
                            else:
                                option1 = 'D'
                    if self.group.option2.radio0.isChecked():
                        option2 = 0
                    if self.group.option2.radio1.isChecked():
                        option2 = 1
                    if self.group.optionn.isChecked():
                        pass
                    else:
                        lamtieude = ''

                    if self.group.optionm.radio1.isChecked():
                        Made = Random_Made_Auto(so_de)
                    if self.group.optionm.radio2.isChecked():
                        Made = Random_Made_First(so_de)
                    if self.group.optionm.radio3.isChecked():
                        Made = Random_Made_Last(so_de)
                    if self.group.optionm.radio4.isChecked():
                        Made_st = self.group.optionm.combo.currentText()
                        Made = Random_Made_Cont(str(Made_st), so_de)
                    if self.group.optionm.radio5.isChecked():
                        Made_st = List_creat(self.group.optionm.line.text())
                        Made = Random_Made_List(Made_st, so_de)
                    tenfile = self.group.line3.text()
                    
                    List = []
                    for file in filename:
                        List += Random_GetListEX_FromFile(file)

                    Full_de = Random_Mix_ListEX(List, so_cau, so_de, [option1, option2])
                    j = 0
                    for Test in Full_de:
                        j += 1
                        Mix_test = Random_CreatDe_One_EX(Test, [option1, option2])
                        with codecs.open('Mixed Test//' + tenfile + str(j) + '.tex', 'w', 'utf-8') as (f):
                            f.write('\\setcounter{ex}{0}\n\\Opensolutionfile{ans}[ans/ans-' + tenfile + str(j) + ']\n\n')
                            for cau in Mix_test:
                                f.write(cau + '\n')

                            f.write('\\Closesolutionfile{ans}')
                            f.close()

                    main = '\\documentclass[12pt,a4paper]{book}\n%\\usepackage{fourier}\n\\usepackage[utf8]{vietnam}\n\\usepackage{amsmath,amssymb,yhmath,mathrsfs,fancyhdr,tkz-euclide,tikz-3dplot}\n\\usepackage{framed,tikz,tkz-tab,tkz-linknodes,pgfplots,currfile,enumerate}\n\\usetikzlibrary{shapes.geometric,arrows,calc,intersections,angles,patterns,snakes,shadings,quotes}\n\\usetkzobj{all}\n\\usepgfplotslibrary{fillbetween}\n\\pgfplotsset{compat=1.9}\n\\usepackage[top=1.5cm, bottom=1.5cm, left=1.5cm, right=1.5cm] {geometry}\n\\usepackage[hidelinks,unicode,pdfencoding=unicode, psdextra]{hyperref}\n\\usepackage[loigiai]{ex_test}\n\\renewcommand{\\vec}[1]{\\protect\\overrightarrow{#1}}\n\\newcommand{\\hoac}[1]{\\left[\\begin{aligned}#1\\end{aligned}\\right.}\n\\newcommand{\\heva}[1]{\\left\\{\\begin{aligned}#1\\end{aligned}\\right.}\n\\renewcommand{\\labelenumi}{\\alph{enumi})}\n\\usepackage{multirow}\n\\usepackage{makecell}\n\\usepackage{lastpage}\n\\renewcommand{\\baselinestretch}{1.2}\n'
                    try:
                        block = codecs.open('Setting//Trangin.tex', 'r', 'utf-8')
                        for line in block:
                            main += line

                    except Exception as er:
                        pass

                    main += '\\newcommand{\\hienda}{1}% 1: hiện đáp án, 0: không hiện đáp án\n\\ifthenelse{\\hienda=1}{\\newcommand{\\lamdapan}[1]{\n\\newpage\n\\begin{center}\n\\textbf{ĐÁP ÁN}\n\\end{center}\n\\begin{multicols}{10}\n\\input{#1}\n\\end{multicols}}}{\\newcommand{\\lamdapan}[1]{}} \n\\begin{document}\n'
                    for i in range(0, int(so_de)):
                        if i == int(so_de) - 1:
                            main += '\\begin{center}\n\\textbf{ĐỀ SỐ ' + str(i + 1) + '}\n\\end{center}\n\\input{' + tenfile + str(i + 1) + '}\n\\lamdapan{ans/ans-' + tenfile + str(i + 1) + '}\n'
                        else:
                            main += '\\begin{center}\n\\textbf{ĐỀ SỐ ' + str(i + 1) + '}\n\\end{center}\n\\input{' + tenfile + str(i + 1) + '}\n\\lamdapan{ans/ans-' + tenfile + str(i + 1) + '}\n\\newpage\n'

                    main += '\n\\end{document}'
                    with codecs.open('Mixed Test//' + tenfile + '-main.tex', 'w', 'utf-8') as (f):
                        f.write(main)
                        f.close()
                    with codecs.open('Setting//lamtieude.tex', 'w', 'utf-8') as (f):
                        lamtieude = '% Định nghĩa làm tiêu đề của gói dethi\n\\newcommand{\\@ttruong}{' + self.group.optionn.line1.text() + '}\n\\newcommand{\\@tkhoa}{' + self.group.optionn.line2.text() + '}\n\\newcommand{\\@ldethi}{' + self.group.optionn.line3.currentText() + '}\n\\newcommand{\\@tkythi}{' + self.group.optionn.line4.text() + '}\n\\newcommand{\\@tmonhoc}{' + self.group.optionn.line5.text() + '}\n\\newcommand{\\@tgian}{' + self.group.optionn.line6.currentText() + '}\n\\newcommand{\\@scau}{' + self.group.combo1.currentText() + '}\n\\newcommand{\\@strang}{4}\n\\newcommand{\\@madethi}{Mã đề thi: 108}\n\\newcommand{\\tentruong}[1]{\\renewcommand{\\@ttruong}[1]{#1}}\n\\newcommand{\\tenkhoa}[1]{\\renewcommand{\\@tkhoa}{#1}}\n\\newcommand{\\loaidethi}[1]{\\renewcommand{\\@ldethi}{#1}}\n\\newcommand{\\tenkythi}[1]{\\renewcommand{\\@tkythi}{#1}}\n\\newcommand{\\tenmonhoc}[1]{\\renewcommand{\\@tmonhoc}{#1}}\n\\newcommand{\\thoigian}[1]{\\renewcommand{\\@tgian}{#1}}\n\\newcommand{\\socauhoi}[1]{\\renewcommand{\\@scau}{#1}}\n\\newcommand{\\sotrang}[1]{\\renewcommand{\\@strang}{#1}}\n\\newcommand{\\madethi}[1]{\\renewcommand{\\@madethi}{Mã đề thi: #1}}\n\\newcommand{\\lamtieude}{\n\\begin{minipage}[b]{0.35\\textwidth}\n\\centering\\textbf{\\@ttruong}\\\\\\textbf{\\@tkhoa}\\\\\\@ldethi\n\\end{minipage}\n\\hfill\n\\begin{minipage}[b]{0.65\\textwidth}\n\\centering\\textbf{\\@tkythi}\\\\\\textbf{\\@tmonhoc}\\\\\\underline{\\it Thời gian làm bài \\@tgian\\ phút.}\\\\\n\\end{minipage}\\vspace{3pt}\n\\begin{minipage}[b]{0.6\\textwidth}\n\\bf Họ và tên: \\dotfill\n\\end{minipage}\n\\begin{minipage}[b]{0.4\\textwidth}\n\\bf SBD: \\dotfill\\fbox{\\@madethi}\n\\end{minipage}\n}\n\n\\rfoot{Trang \\thepage/\\@strang\\, -- \\@madethi }'
                        f.write(lamtieude)
                        f.close()
                    main1 = '\\documentclass[12pt,a4paper]{book}\n%\\usepackage{fourier}\n\\usepackage[utf8]{vietnam}\n\\usepackage{amsmath,amssymb,yhmath,mathrsfs,fancyhdr,tkz-euclide,tikz-3dplot}\n\\usepackage{framed,tikz,tkz-tab,tkz-linknodes,pgfplots,currfile,enumerate}\n\\usetikzlibrary{shapes.geometric,arrows,calc,intersections,angles,patterns,snakes,shadings,quotes}\n\\usetkzobj{all}\n\\usepgfplotslibrary{fillbetween}\n\\pgfplotsset{compat=1.9}\n\\usepackage[top=1.5cm, bottom=1.5cm, left=1.5cm, right=1.5cm] {geometry}\n\\usepackage[hidelinks,unicode,pdfencoding=unicode, psdextra]{hyperref}\n\\usepackage[loigiai]{ex_test}\n\\renewcommand{\\vec}[1]{\\protect\\overrightarrow{#1}}\n\\newcommand{\\hoac}[1]{\\left[\\begin{aligned}#1\\end{aligned}\\right.}\n\\newcommand{\\heva}[1]{\\left\\{\\begin{aligned}#1\\end{aligned}\\right.}\n\\renewcommand{\\labelenumi}{\\alph{enumi})}\n\\usepackage{multirow}\n\\usepackage{makecell}\n\\usepackage{lastpage}\n\\renewcommand{\\baselinestretch}{1.2}\n\\usepackage{fancyhdr}\n\\pagestyle{fancy}\n\\cfoot{}\n\\renewcommand{\\headrulewidth}{0pt}\n'
                    main2 = '% Ẩn hiện làm đáp án\n\\newcommand{\\hienda}{1}% 1: hiện đáp án, 0: không hiện đáp án\n\\ifthenelse{\\hienda=1}{\\newcommand{\\lamdapan}[1]{\n\\newpage\n\\begin{center}\n\\textbf{ĐÁP ÁN}\n\\end{center}\n\\begin{multicols}{10}\n\\input{#1}\n\\end{multicols}}}{\\newcommand{\\lamdapan}[1]{}}\n\\begin{document}\n'
                    for i in range(0, so_de):
                        if i < so_de - 1:
                            main2 += '\\setcounter{ex}{0}\n\\setcounter{page}{1}\n\\madethi{' + Made[i] + '}\\sotrang{\\pageref{DE' + Made[i] + '}}\n\\lamtieude\n\\input{' + tenfile + str(i + 1) + '}\n\\label{DE' + Made[i] + '}\n\\newpage\n\\setcounter{page}{1}\n\\rfoot{Trang \\thepage/\\pageref{DA' + Made[i] + '} -- Đáp án \\@madethi}\n\\lamdapan{ans/ans-' + tenfile + str(i + 1) + '}\n\\label{DA' + Made[i] + '}\n\\newpage\n\n'
                        else:
                            main2 += '\\setcounter{ex}{0}\n\\setcounter{page}{1}\n\\madethi{' + Made[i] + '}\\sotrang{\\pageref{DE' + Made[i] + '}}\n\\lamtieude\n\\input{' + tenfile + str(i + 1) + '}\n\\label{DE' + Made[i] + '}\n\\newpage\n\\setcounter{page}{1}\n\\rfoot{Trang \\thepage/\\pageref{DA' + Made[i] + '} -- Đáp án \\@madethi}\n\\lamdapan{ans/ans-' + tenfile + str(i + 1) + '}\n\\label{DA' + Made[i] + '}\n\\end{document}'

                    with codecs.open('Mixed Test//' + tenfile + '-main.tex', 'w', 'utf-8') as (f):
                        f.write(main1)
                        f.write(lamtieude)
                        f.write(main2)
                        f.close()
                    t = time.time() - start_time
                    hour, minute, second = Time_convert(t)
                    path='Mixed Test\\' + tenfile + '-main.tex'
                    if self.group.radiobuild.isChecked():
                        try:
                            cmd = [
                             'pdflatex', '-interaction', 'nonstopmode', path]
                            proc = subprocess.Popen(cmd)
                            proc.communicate()
                            retcode = proc.returncode
                            if not retcode == 0:
                                os.unlink(filename + '.pdf')
                            raise ValueError(('Error {} executing command: {}').format(retcode, (' ').join(cmd)))
                        except Exception as err:
                            i = 0
                        path='Mixed Test\\' + tenfile + '-main.pdf'
                        if openfile(path)=='Error':
                                QMessageBox.critical(self, 'Lỗi','Lỗi mở file '+path)
                    else:
                        buttonReply = QMessageBox.question(self, 'Thông báo', 'Đã tạo file thành công.\nThời gian xử lí: ' + str(int(hour)) + ':' + str(int(minute)) + ':' + str(round(second, 2)) + '\nBạn có muốn mở file main để biên dịch không?', QMessageBox.Yes, QMessageBox.No)
                        if buttonReply == QMessageBox.Yes:
                            if openfile(path)=='Error':
                                QMessageBox.critical(self, 'Lỗi','Lỗi mở file '+path)

    def Option2_isCheck(self):
        if self.group.option2.isChecked() and REG_INF == 1:
            QMessageBox.question(self, 'Thông báo', 'Vui lòng đăng kí (miễn phí) bản quyền để sử dụng', QMessageBox.Yes)
            self.group.option2.setChecked(False)

    def Option3_isCheck(self):
        if self.group.option3.isChecked():
            if REG_INF == 1:
                QMessageBox.question(self, 'Thông báo', 'Vui lòng đăng kí (miễn phí) bản quyền để sử dụng', QMessageBox.Yes)
            else:
                QMessageBox.question(self, 'Thông báo', 'Tính năng đang cần check lại trước khi update.\nMặc định là không in đáp án PDF.', QMessageBox.Yes)
            self.group.option3.setChecked(False)

    def Option4_isCheck(self):
        if self.group.option4.isChecked():
            if REG_INF == 1:
                QMessageBox.question(self, 'Thông báo', 'Vui lòng đăng kí (miễn phí) bản quyền để sử dụng', QMessageBox.Yes)
            else:
                QMessageBox.question(self, 'Thông báo', 'Tính năng đang cần check lại trước khi update.\nMặc định là không tạo file Excel.', QMessageBox.Yes)
            self.group.option4.setChecked(False)