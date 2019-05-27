# coding=utf-8
# src_matrix.py
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

class Matrix_Test(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QGridLayout())
        self.group = QGroupBox('Thông tin về ma trận đề')
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
        self.group.button2 = QPushButton('Lưu và in thông tin ma trận')
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
        self.group.hbox2.button1 = QPushButton('Chọn ngân hàng đề')
        self.group.hbox2.button1.clicked.connect(self.G1_get_file_3)
        self.group.hbox2.button2 = QPushButton('Kiểm tra')
        self.group.hbox2.button2.clicked.connect(self.G1_get_file_4)
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
        header = self.group.table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for x in range(2, 9):
            self.group.table.setColumnWidth(x, 35)

        self.group.hbox3 = QHBoxLayout()
        self.group.label31 = QLabel('Số đề tối đa: ')
        self.group.label31.setMinimumWidth(30)
        self.group.label32 = QLabel()
        self.group.label32.setMinimumWidth(30)
        self.group.label33 = QLabel('Chọn số đề')
        self.group.label33.setMinimumWidth(30)
        self.group.combo = QComboBox()
        self.group.combo.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.group.label34 = QLabel('Lưu tên file')
        self.group.label34.setMinimumWidth(30)
        self.group.line3 = QLineEdit()
        self.group.button3 = QPushButton('Khởi tạo đề theo ma trận')
        self.group.button3.clicked.connect(self.G1_get_file_5)
        self.group.hbox3.addWidget(self.group.label31)
        self.group.hbox3.addWidget(self.group.label32)
        self.group.hbox3.addWidget(self.group.label33)
        self.group.hbox3.addWidget(self.group.combo)
        self.group.hbox3.addWidget(self.group.label34)
        self.group.hbox3.addWidget(self.group.line3)
        self.group.hbox3.addWidget(self.group.button3)
        self.group.hbox.addWidget(self.group.label1)
        self.group.hbox.addWidget(self.group.line1)
        self.group.hbox.addWidget(self.group.button0)
        self.group.hbox.addWidget(self.group.button1)
        self.group.hbox.addWidget(self.group.button2)
        self.group.hbox1.addWidget(self.group.table)
        self.group.hbox2.addWidget(self.group.radio2)
        self.group.hbox2.addWidget(self.group.radio1)
        self.group.hbox2.addWidget(self.group.hbox2.button2)
        self.group.setLayout(self.group.vbox)
        self.group.vbox.addLayout(self.group.hbox)
        self.group.vbox.addLayout(self.group.hbox2)
        self.group.vbox.addLayout(self.group.grip)
        self.group.vbox.addLayout(self.group.hbox1)
        self.group.vbox.addLayout(self.group.hbox3)
        self.group2 = QGroupBox('baitracnghiem form (dethi3.5) to Ex_test')
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
        self.group5 = QGroupBox('Auto check True')
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
        self.group7.setMinimumHeight(150)
        self.group7 = QGroupBox('Update to be continue')
        self.group7.setMinimumHeight(150)
        self.layout().addWidget(self.group, 0, 1)
        for widget in (self.group, self.group2, self.group5):
            widget.setMinimumHeight(350)

    def G1_HD(self):
        Form_question = 'Bước 1: Nhấn chọn một file.\r\nBước 2: Nhấn Lưu và in ma trận đề.'
        QMessageBox.question(self, 'Hướng dẫn', Form_question, QMessageBox.Yes)

    def G1_get_file_1(self):
        if REG_INF == 0:
            QMessageBox.question(self, 'Thông báo', 'Vui lòng đăng kí (miễn phí) bản quyền để sử dụng', QMessageBox.Yes)
        else:
            self.group.table.setRowCount(0)
            fname = QFileDialog.getOpenFileName()
            self.group.line1.setText(fname[0])

    def G1_get_file_2(self):
        start_time = time.time()
        type_arrange = ['Y', 'B', 'K', 'G', 'T']
        filename = self.group.line1.text()
        if filename == '':
            QMessageBox.question(self, 'Thông báo', 'Bạn chưa chọn file', QMessageBox.Yes)
        else:
            if 1 == 1:
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
                        f.write(ID[0] + ',' + ID[1] + ',' + ID[2] + ',' + ID[3] + ',' + ID[4] + ',' + ID[5] + ',' + ID[6] + '\r\n')

                    f.close()

    def G1_get_file_3(self):
        if REG_INF == 1:
            QMessageBox.question(self, 'Thông báo', 'Vui lòng đăng kí (miễn phí) bản quyền để sử dụng', QMessageBox.Yes)
        else:
            fname = QFileDialog.getOpenFileNames()
            filename = ''
            for i in fname[0]:
                filename += i + ','

            self.group.hbox2.line1.setText(filename[:-1])

    def G1_get_file_4(self):
        start_time = time.time()
        type_arrange = ['Y', 'B', 'K', 'G', 'T']
        if self.group.radio2.isChecked():
            try:
                font = QFont()
                font.setBold(True)
                i = 1
                Matrix = []
                Data = []
                Bank = codecs.open('Bank//Bank_Information.dll', 'r', 'utf-8')
                for line in Bank:
                    ID = List_creat(line.strip())
                    Data.append((ID[0], ID[1], ID[2], ID[3], ID[4], ID[5], ID[6]))

                Matran = codecs.open('Temp//Matran.tex', 'r', 'utf-8')
                for line in Matran:
                    ID = List_creat(line.strip())
                    Matrix.append((ID[0], ID[1], ID[2], ID[3], ID[4], ID[5], ID[6]))

                j = 0
                k = 0
                Matran_full = []
                for ID1 in Matrix:
                    for ID2 in Data[k:]:
                        k += 1
                        if ID1[0] == ID2[0]:
                            Matran_full.append((ID1[0], ID2[1], ID2[2], ID2[3], ID2[4], ID2[5], ID1[1], ID1[2], ID1[3], ID1[4], ID1[5]))
                            strY = QTableWidgetItem(ID2[1] + '/' + ID2[2] + '/' + ID2[3] + '/' + ID2[4] + '/' + ID2[5])
                            strY.setFont(font)
                            self.group.table.setItem(i, 2, strY)
                            i += 1
                            break

                Max_de = Matrix_Count_Max_Test(Matran_full)
                try:
                    self.group.label32.setText(str(Max_de))
                    self.group.combo.clear()
                    for i in range(0, Max_de):
                        if REG_INF <= 2:
                            self.group.combo.addItem(str(i + 1))
                            if i == 1:
                                break
                        else:
                            if REG_INF == 3:
                                self.group.combo.addItem(str(i + 1))
                                if i == 3:
                                    break
                            else:
                                self.group.combo.addItem(str(i + 1))

                except Exception as er:
                    self.group.combo.clear()

            except Exception as er:
                if str(er) == "[Errno 2] No such file or directory: 'Temp//Matran.tex'":
                    QMessageBox.question(self, 'Thông báo', 'Bạn cần chọn ma trận và Lưu và in thông tin ma trận', QMessageBox.Yes)
                else:
                    QMessageBox.question(self, 'Thông báo', 'Chương trình xảy ra lỗi.\r\nBạn cần tạo ngân hàng dữ liệu trước khi kiểm tra.', QMessageBox.Yes)

        else:
            QMessageBox.question(self, 'Thông báo', 'Ngân hàng Offline chưa xây dựng dữ liệu', QMessageBox.Yes)
            self.group.radio2.setChecked(True)

    def G1_get_file_5(self):
        start_time = time.time()
        if REG_INF == 1:
            QMessageBox.question(self, 'Thông báo', 'Bạn cần đăng kí để sử dụng chức năng này.', QMessageBox.Yes)
        else:
            if os.path.exists('Matran\\' + self.group.line3.text() + '1.tex'):
                QMessageBox.question(self, 'Thông báo', 'Tên file đã tồn tại. Bạn hãy chọn tên file kh', QMessageBox.Yes)
            else:
                List_Matrix = []
                Matran = codecs.open('Temp//Matran.tex', 'r', 'utf-8')
                for line in Matran:
                    ID = List_creat(line.strip())
                    List_Matrix.append((ID[0], ID[1], ID[2], ID[3], ID[4], ID[5], ID[6]))

                filename = self.group.line3.text()
                number = self.group.combo.currentText()
                Source = Bank_Get_Source(List_Matrix)
                Bank_Creat_File(Source, filename, int(number))
                t = time.time() - start_time
                hour, minute, second = Time_convert(t)
                with codecs.open('Temp//Matran.tex', 'r', 'utf-8') as (f):
                    f.close()
                buttonReply = QMessageBox.question(self, 'Thông báo', 'Đã tạo file thành công.\nThời gian xử lí: ' + str(int(hour)) + ':' + str(int(minute)) + ':' + str(round(second, 2)) + '\nBạn có muốn mở file main để biên dịch không?', QMessageBox.Yes, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            path='Matran\\main.tex'
            if openfile(path)=='Error':
                QMessageBox.critical(self, 'Lỗi','Lỗi mở file '+path)

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
            List = List_creat(self.group2.line1.text())
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
        except Exception as err:
            QMessageBox.question(self, 'Thông báo', 'Chương trình xảy ra lỗi.\nLỗi: ' + str(err), QMessageBox.Yes)

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
        start_time = time.time()
        List = List_creat(self.group5.line1.text())
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