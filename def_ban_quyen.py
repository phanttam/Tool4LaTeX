# coding=utf-8
# def_ban_quyen.py
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
REG_INF = Registry_Inf_get()

def get_number_diag(number):
    if number == '':
        number = 0
    else:
        if '/' in number:
            number = float(Fraction(number))
        else:
            if '.' in number:
                number = float(number)
            else:
                if float(number) == int(number):
                    number = int(number)
    return number


def TB_update_FREE(self, text):
    return QMessageBox.question(self, 'Thông báo', text + 'Bạn cần đăng kí thông tin để sử dụng.\nCác bạn vào tab Thông tin.\nĐiền đủ 3 thông tin.\nNhấn tạo file đăng kí.\nNhấn Gửi file đăng kí\nĐính kèm file ten-sdt.tex inbox cho tác giả.', QMessageBox.Yes)


def TB_Error_PdfLaTeX(self, text):
    return QMessageBox.question(self, 'Error!', 'Đã xảy ra lỗi trong quá trình PdfLaTeX.\nHãy copy code vào trong TeXstudio, sửa và biên dịch lại.\nThông báo lỗi:' + text, QMessageBox.Yes)


def TB_Error_Input(self, text):
    return QMessageBox.question(self, 'Lỗi do nhập dữ liệu', 'Bạn cần nhập dữ liệu đúng.\nHãy nhập số nguyên, số hữu tỷ!!!\nChú ý: Ô không nhập liệu mặc định là 0.\n' + text, QMessageBox.Yes)


def TB_Error_TQ(self, text):
    if 'No such file or directory' in text:
        return QMessageBox.question(self, 'Error!', 'Vui lòng chọn file(s) (thư mục) trước khi thao tác.', QMessageBox.Yes)
    else:
        return QMessageBox.question(self, 'Error!', 'Đã xảy ra lỗi.\nThông báo lỗi: ' + text, QMessageBox.Yes)