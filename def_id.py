# coding=utf-8
# def_id.py
import re, os, sys, csv, codecs, time
from datetime import datetime, timedelta
from urllib.request import urlopen
import math, argparse, subprocess, signal, shutil, errno, unicodedata, webbrowser
from fractions import Fraction
from decimal import Decimal
from def_calculation import *
from src_reg import *
from def_bbt import *
from def_convert import *
from def_ban_quyen import *
from def_mix import *
list_danh_sach_ID6 = [
 '0D1?1-1', '0D1?1-2', '0D1?1-3', '0D1?1-4', '0D1?1-5', '0D1?2-1', '0D1?2-2', '0D1?3-1', '0D1?3-2', '0D1?3-3', '0D1?4-1', '0D1?4-2', '0D1?5-1', '0D1?5-2', '0D2?1-1', '0D2?1-2', '0D2?1-3', '0D2?1-4', '0D2?2-1', '0D2?2-2', '0D2?2-3', '0D2?2-4', '0D2?2-5', '0D2?3-1', '0D2?3-2', '0D2?3-3', '0D2?3-4', '0D2?3-5', '0D3?1-1', '0D3?1-2', '0D3?1-3', '0D3?2-1', '0D3?2-2', '0D3?2-3', '0D3?2-4', '0D3?2-5', '0D3?2-6', '0D3?2-7', '0D3?3-1', '0D3?3-2', '0D3?3-3', '0D3?3-4', '0D3?3-5', '0D4?1-1', '0D4?1-2', '0D4?1-3', '0D4?1-4', '0D4?1-5', '0D4?2-1', '0D4?2-2', '0D4?2-3', '0D4?2-4', '0D4?2-5', '0D4?2-6', '0D4?3-1', '0D4?3-2', '0D4?3-3', '0D4?3-4', '0D4?3-5', '0D4?4-1', '0D4?4-2', '0D4?4-3', '0D4?4-4', '0D4?5-1', '0D4?5-2', '0D4?5-3', '0D4?5-4', '0D4?5-5', '0D4?5-6', '0D4?5-7', '0D4?5-8', '0D5?1-1', '0D5?1-2', '0D5?1-3', '0D5?2-1', '0D5?2-2', '0D5?2-3', '0D5?2-4', '0D5?3-1', '0D5?3-2', '0D5?3-3', '0D5?3-4', '0D5?4-1', '0D5?4-2', '0D6?1-1', '0D6?1-2', '0D6?1-3', '0D6?1-4', '0D6?1-5', '0D6?2-1', '0D6?2-2', '0D6?2-3', '0D6?2-4', '0D6?2-5', '0D6?2-6', '0D6?2-7', '0D6?3-1', '0D6?3-2', '0D6?3-3', '0D6?3-4', '0D6?3-5', '0D6?3-6', '0D6?3-7', '0D6?3-8', '0H1?1-1', '0H1?1-2', '0H1?1-3', '0H1?2-1', '0H1?2-2', '0H1?2-3', '0H1?2-4', '0H1?2-5', '0H1?3-1', '0H1?3-2', '0H1?3-3', '0H1?3-4', '0H1?3-5', '0H1?3-6', '0H1?3-7', '0H1?4-1', '0H1?4-2', '0H1?4-3', '0H1?4-4', '0H1?4-5', '0H2?1-1', '0H2?1-2', '0H2?1-3', '0H2?1-4', '0H2?2-1', '0H2?2-2', '0H2?2-3', '0H2?2-4', '0H2?2-5', '0H2?3-1', '0H2?3-2', '0H2?3-3', '0H2?3-4', '0H3?1-1', '0H3?1-2', '0H3?1-3', '0H3?1-4', '0H3?1-5', '0H3?1-6', '0H3?1-7', '0H3?2-1', '0H3?2-2', '0H3?2-3', '0H3?2-4', '0H3?2-5', '0H3?2-6', '0H3?3-1', '0H3?3-2', '0H3?3-3', '0H3?3-4', '1D1?1-1', '1D1?1-2', '1D1?1-3', '1D1?1-4', '1D1?1-5', '1D1?1-6', '1D1?2-1', '1D1?3-1', '1D1?3-2', '1D1?3-3', '1D1?3-4', '1D1?3-5', '1D1?3-6', '1D1?3-7', '1D1?3-8', '1D2?1-1', '1D2?1-2', '1D2?1-3', '1D2?2-1', '1D2?2-2', '1D2?2-3', '1D2?2-4', '1D2?2-5', '1D2?2-6', '1D2?3-1', '1D2?3-2', '1D2?3-3', '1D2?4-1', '1D2?4-2', '1D2?5-1', '1D2?5-2', '1D2?5-3', '1D2?5-4', '1D2?5-5', '1D3?1-1', '1D3?1-2', '1D3?2-1', '1D3?2-2', '1D3?2-3', '1D3?2-4', '1D3?2-5', '1D3?2-6', '1D3?3-1', '1D3?3-2', '1D3?3-3', '1D3?3-4', '1D3?3-5', '1D3?3-6', '1D3?4-1', '1D3?4-2', '1D3?4-3', '1D3?4-4', '1D3?4-5', '1D3?4-6', '1D3?4-7', '1D4?1-1', '1D4?1-2', '1D4?1-3', '1D4?1-4', '1D4?1-5', '1D4?1-6', '1D4?2-1', '1D4?2-2', '1D4?2-3', '1D4?2-4', '1D4?2-5', '1D4?2-6', '1D4?2-7', '1D4?2-8', '1D4?3-1', '1D4?3-2', '1D4?3-3', '1D4?3-4', '1D4?3-5', '1D4?3-6', '1D4?3-7', '1D5?1-1', '1D5?2-1', '1D5?2-2', '1D5?2-3', '1D5?2-4', '1D5?2-5', '1D5?2-6', '1D5?3-1', '1D5?3-2', '1D5?4-1', '1D5?5-1', '1D5?5-2', '1D5?5-3', '1H1?1-1', '1H1?1-2', '1H1?2-1', '1H1?2-2', '1H1?2-3', '1H1?3-1', '1H1?3-2', '1H1?3-3', '1H1?3-4', '1H1?4-1', '1H1?4-2', '1H1?4-3', '1H1?4-4', '1H1?5-1', '1H1?5-2', '1H1?5-3', '1H1?5-4', '1H1?6-1', '1H1?6-2', '1H1?7-1', '1H1?7-2', '1H1?7-3', '1H1?7-4', '1H1?8-1', '1H1?8-2', '1H2?1-1', '1H2?1-2', '1H2?1-3', '1H2?1-4', '1H2?1-5', '1H2?1-6', '1H2?2-1', '1H2?2-2', '1H2?2-3', '1H2?2-4', '1H2?2-5', '1H2?2-6', '1H2?3-1', '1H2?3-2', '1H2?3-3', '1H2?3-4', '1H2?3-5', '1H2?4-1', '1H2?4-2', '1H2?4-3', '1H2?4-4', '1H2?4-5', '1H2?4-6', '1H2?5-1', '1H2?5-2', '1H2?5-3', '1H3?1-1', '1H3?1-2', '1H3?1-3', '1H3?1-4', '1H3?1-5', '1H3?2-1', '1H3?2-2', '1H3?2-3', '1H3?2-4', '1H3?3-1', '1H3?3-2', '1H3?3-3', '1H3?3-4', '1H3?4-1', '1H3?4-2', '1H3?4-3', '1H3?4-4', '1H3?4-5', '1H3?4-6', '1H3?5-1', '1H3?5-2', '1H3?5-3', '1H3?5-4', '1H3?5-5', '2D1?1-1', '2D1?1-2', '2D1?1-3', '2D1?1-4', '2D1?1-5', '2D1?2-1', '2D1?2-2', '2D1?2-3', '2D1?2-4', '2D1?2-5', '2D1?2-6', '2D1?2-7', '2D1?3-1', '2D1?3-2', '2D1?3-3', '2D1?3-4', '2D1?3-5', '2D1?3-6', '2D1?3-7', '2D1?4-1', '2D1?4-2', '2D1?4-3', '2D1?4-4', '2D1?5-1', '2D1?5-2', '2D1?5-3', '2D1?5-4', '2D1?5-5', '2D1?5-6', '2D1?5-7', '2D1?5-8', '2D2?1-1', '2D2?1-2', '2D2?1-3', '2D2?2-1', '2D2?2-2', '2D2?2-3', '2D2?2-4', '2D2?3-1', '2D2?3-2', '2D2?3-3', '2D2?4-1', '2D2?4-2', '2D2?4-3', '2D2?4-4', '2D2?4-5', '2D2?4-6', '2D2?4-7', '2D2?5-1', '2D2?5-2', '2D2?5-3', '2D2?5-4', '2D2?5-5', '2D2?5-6', '2D2?5-7', '2D2?6-1', '2D2?6-2', '2D2?6-3', '2D2?6-4', '2D2?6-5', '2D2?6-6', '2D2?6-7', '2D3?1-1', '2D3?1-2', '2D3?1-3', '2D3?2-1', '2D3?2-2', '2D3?2-3', '2D3?2-4', '2D3?3-1', '2D3?3-2', '2D3?3-3', '2D3?3-4', '2D3?3-5', '2D3?3-6', '2D3?3-7', '2D4?1-1', '2D4?1-2', '2D4?1-3', '2D4?2-1', '2D4?2-2', '2D4?2-3', '2D4?2-4', '2D4?2-5', '2D4?3-1', '2D4?3-2', '2D4?3-3', '2D4?3-4', '2D4?3-5', '2D4?4-1', '2D4?4-2', '2D4?4-3', '2D4?4-4', '2D4?5-1', '2D4?5-2', '2H1?1-1', '2H1?1-2', '2H1?1-3', '2H1?1-4', '2H1?2-1', '2H1?2-2', '2H1?2-3', '2H1?3-1', '2H1?3-2', '2H1?3-3', '2H1?3-4', '2H1?3-5', '2H1?3-6', '2H2?1-1', '2H2?1-2', '2H2?1-3', '2H2?1-4', '2H2?1-5', '2H2?1-6', '2H2?2-1', '2H2?2-2', '2H2?2-3', '2H2?2-4', '2H2?2-5', '2H2?2-6', '2H3?1-1', '2H3?1-2', '2H3?1-3', '2H3?1-4', '2H3?2-1', '2H3?2-2', '2H3?2-3', '2H3?2-4', '2H3?2-5', '2H3?2-6', '2H3?2-7', '2H3?2-8', '2H3?3-1', '2H3?3-2', '2H3?3-3', '2H3?3-4', '2H3?3-5', '2H3?3-6', '2H3?3-7', '2H3?3-8', '2H3?4-1', '2H3?4-2']
h0 = 104
d1 = 154
h1 = 243
d2 = 318
h2 = 413
list_danh_sach_ID6_10 = list_danh_sach_ID6[:h0]
list_danh_sach_ID6_10D = list_danh_sach_ID6[:h0]
list_danh_sach_ID6_10H = list_danh_sach_ID6[h0:d1]
list_danh_sach_ID6_11 = list_danh_sach_ID6[h0:h1]
list_danh_sach_ID6_11D = list_danh_sach_ID6[d1:h1]
list_danh_sach_ID6_11H = list_danh_sach_ID6[h1:d2]
list_danh_sach_ID6_12 = list_danh_sach_ID6[d2:]
list_danh_sach_ID6_12D = list_danh_sach_ID6[d2:h2]
list_danh_sach_ID6_12H = list_danh_sach_ID6[h2:]

def ID_information_so(ID):
    Lop = ''
    Mon = ''
    Chuong = ''
    Mucdo = ''
    Bai = ''
    Dang = ''
    if ID[0] == '0':
        Lop = '[0] Lớp 10'
        if ID[1] == 'D':
            Mon = '[D] ĐẠI SỐ'
            if ID[2] == '1':
                Chuong = '[1] Mệnh đề. Tập hợp'
                if ID[4] == '1':
                    Bai = '[1] Mệnh đề'
                    if ID[6] == '1':
                        Dang = '[1] Nhận biết mệnh đề, mệnh đề chứa biến'
                    if ID[6] == '2':
                        Dang = '[2] Xét tính đúng - sai của mệnh đề'
                    if ID[6] == '3':
                        Dang = '[3] Phủ định của một mệnh đề'
                    if ID[6] == '4':
                        Dang = '[4] Mệnh đề kéo theo, mệnh đề đảo, hai mệnh đề tương đương'
                    if ID[6] == '5':
                        Dang = '[5] Mệnh đề với kí hiệu $\\forall$ và $\\exists$'
                if ID[4] == '2':
                    Bai = '[2] Tập hợp'
                    if ID[6] == '1':
                        Dang = '[1] Tập hợp và phần tử của tập hợp'
                    if ID[6] == '2':
                        Dang = '[2] Tập hợp con - Hai tập hợp bằng nhau'
                if ID[4] == '3':
                    Bai = '[3] Các phép toán tập hợp'
                    if ID[6] == '1':
                        Dang = '[1] Giao và hợp của hai tập hợp'
                    if ID[6] == '2':
                        Dang = '[2] Hiệu và phần bù của hai tập hợp'
                    if ID[6] == '3':
                        Dang = '[3] Toán thực tế ứng dụng của tập hợp'
                if ID[4] == '4':
                    Bai = '[4] Các tập hợp số'
                    if ID[6] == '1':
                        Dang = '[1] Xác định các khoảng, đoạn, nửa khoảng, các phép toán giao, hợp'
                    if ID[6] == '2':
                        Dang = '[2] Xác định hiệu và phần bù của các khoảng, đoạn, nửa khoảng'
                if ID[4] == '5':
                    Bai = '[5] Số gần đúng. Sai số'
                    if ID[6] == '1':
                        Dang = '[1] Tính và ước lượng sai số tuyệt đối'
                    if ID[6] == '2':
                        Dang = '[2] Tính và xác định độ chính xác của kết quả'
            if ID[2] == '2':
                Chuong = '[2] Hàm số bậc nhất và bậc hai'
                if ID[4] == '1':
                    Bai = '[1] Hàm số'
                    if ID[6] == '1':
                        Dang = '[1] Tính giá trị của hàm số'
                    if ID[6] == '2':
                        Dang = '[2] Tìm tập xác định của hàm số'
                    if ID[6] == '3':
                        Dang = '[3] Tính đồng biến, nghịch biến của hàm số'
                    if ID[6] == '4':
                        Dang = '[4] Tính chẵn, lẻ của hàm số'
                if ID[4] == '2':
                    Bai = '[2] Hàm số $y=ax+b$'
                    if ID[6] == '1':
                        Dang = '[1] Tính đồng biến, nghịch biến của hàm số'
                    if ID[6] == '2':
                        Dang = '[2] Xác định hàm số bậc nhất'
                    if ID[6] == '3':
                        Dang = '[3] Đồ thị'
                    if ID[6] == '4':
                        Dang = '[4] Bài toán tương giao'
                    if ID[6] == '5':
                        Dang = '[5] Toán thực tế ứng dụng hàm số bậc nhất'
                if ID[4] == '3':
                    Bai = '[3] Hàm số bậc hai'
                    if ID[6] == '1':
                        Dang = '[1] TXĐ, bảng biến thiên, tính đơn điệu, GTLN - GTNN của hàm số bậc hai*'
                    if ID[6] == '2':
                        Dang = '[2] Xác định hàm số bậc hai'
                    if ID[6] == '3':
                        Dang = '[3] Đồ thị'
                    if ID[6] == '4':
                        Dang = '[4] Bài toán tương giao'
                    if ID[6] == '5':
                        Dang = '[5] Toán thực tế ứng dụng hàm số bậc hai'
            if ID[2] == '3':
                Chuong = '[3] Phương trình - Hệ phương trình'
                if ID[4] == '1':
                    Bai = '[1] Đại cương về phương trình'
                    if ID[6] == '1':
                        Dang = '[1] Tìm điều kiện của phương trình'
                    if ID[6] == '2':
                        Dang = '[2] Nghiệm của phương trình'
                    if ID[6] == '3':
                        Dang = '[3] Giải phương trình bằng cách biến đổi tương đương hoặc hệ quả'
                if ID[4] == '2':
                    Bai = '[2] Phương trình quy về phương trình bậc nhất, bậc hai'
                    if ID[6] == '1':
                        Dang = '[1] Phương trình tích'
                    if ID[6] == '2':
                        Dang = '[2] Phương trình chứa ẩn trong dấu giá trị tuyệt đối'
                    if ID[6] == '3':
                        Dang = '[3] Phương trình chứa ẩn ở mẫu'
                    if ID[6] == '4':
                        Dang = '[4] Phương trình chứa ẩn dưới dấu căn'
                    if ID[6] == '5':
                        Dang = '[5] Định lí Vi-et và ứng dụng'
                    if ID[6] == '6':
                        Dang = '[6] Giải và biện luận phương trình'
                    if ID[6] == '7':
                        Dang = '[7] Phương trình bậc cao và các bài toán liên quan *'
                if ID[4] == '3':
                    Bai = '[3] Phương trình và hệ phương trình bậc nhất nhiều ẩn'
                    if ID[6] == '1':
                        Dang = '[1] Giải và biện luận phương trình bậc nhất hai ẩn'
                    if ID[6] == '2':
                        Dang = '[2] Giải và biện luận hệ phương trình bậc nhất hai ẩn'
                    if ID[6] == '3':
                        Dang = '[3] Giải hệ phương trình bậc nhất hai ẩn, ba ẩn'
                    if ID[6] == '4':
                        Dang = '[4] Giải hệ phương trình bậc cao'
                    if ID[6] == '5':
                        Dang = '[5] Toán thực tế giải phương trình, hệ phương trình'
            if ID[2] == '4':
                Chuong = '[4] Bất đẳng thức - Bất phương trình'
                if ID[4] == '1':
                    Bai = '[1] Bất đẳng thức'
                    if ID[6] == '1':
                        Dang = '[1] Chứng minh BĐT dựa vào định nghĩa và tính chất'
                    if ID[6] == '2':
                        Dang = '[2] Chứng minh BĐT dựa vào BĐT Cauchy'
                    if ID[6] == '3':
                        Dang = '[3] Chứng minh BĐT dựa vào BĐT Bunhiacopxki'
                    if ID[6] == '4':
                        Dang = '[4] Bất đẳng thức về giá trị tuyệt đối'
                    if ID[6] == '5':
                        Dang = '[5] Ứng dụng BĐT để giải PT, HPT, BPT, tìm GTLN-GTNN'
                if ID[4] == '2':
                    Bai = '[2] Bất phương trình và hệ bất phương trình một ẩn'
                    if ID[6] == '1':
                        Dang = '[1] Tìm điều kiện xác định của bất phương trình - hệ phương trình'
                    if ID[6] == '2':
                        Dang = '[2] Bất phương trình - hệ bất phương trình tương đương'
                    if ID[6] == '3':
                        Dang = '[3] Giải bất phương trình bậc nhất một ẩn và biểu diễn tập nghiệm'
                    if ID[6] == '4':
                        Dang = '[4] Giải hệ bất phương trình bậc nhất một ẩn và biểu diễn tập nghiệm'
                    if ID[6] == '5':
                        Dang = '[5] Bất phương trình - hệ bất phương trình bậc nhất một ẩn chứa tham số'
                    if ID[6] == '6':
                        Dang = '[6] Toán thực tế giải bất phương trình, hệ bất phương trình'
                if ID[4] == '3':
                    Bai = '[3] Dấu của nhị thức bậc nhất'
                    if ID[6] == '1':
                        Dang = '[1] Nhận dạng nhị thức và xét dấu biểu thức'
                    if ID[6] == '2':
                        Dang = '[2] Bất phương trình tích'
                    if ID[6] == '3':
                        Dang = '[3] Bất phương có ẩn ở mẫu'
                    if ID[6] == '4':
                        Dang = '[4] Dấu nhị thức bậc nhất trên một miền'
                    if ID[6] == '5':
                        Dang = '[5] Giải PT, BPT chứa dấu giá trị tuyệt đối'
                if ID[4] == '4':
                    Bai = '[4] Bất phương trình bậc nhất hai ẩn'
                    if ID[6] == '1':
                        Dang = '[1] Bất phương trình bậc nhất hai ẩn và các bài toán liên quan'
                    if ID[6] == '2':
                        Dang = '[2] Hệ bất phương trình bậc nhất hai ẩn và các bài toán liên quan'
                    if ID[6] == '3':
                        Dang = '[3] Các bài toán ứng dụng thực tế'
                    if ID[6] == '4':
                        Dang = '[4] Miền nghiệm của hệ bất phương trình bậc nhất hai ẩn'
                if ID[4] == '5':
                    Bai = '[5] Dấu của tam thức bậc hai'
                    if ID[6] == '1':
                        Dang = '[1] Nhận dạng tam thức và xét dấu biểu thức'
                    if ID[6] == '2':
                        Dang = '[2] Giải và các bài toán liên quan bất phương trình bậc hai'
                    if ID[6] == '3':
                        Dang = '[3] Giải và các bài toán liên quan bất phương trình tích, thương'
                    if ID[6] == '4':
                        Dang = '[4] Giải và các bài toán liên quan hệ bất phương bậc hai'
                    if ID[6] == '5':
                        Dang = '[5] Phương trình và bất phương trình chứa dấu giá trị tuyệt đối'
                    if ID[6] == '6':
                        Dang = '[6] Phương trình và bất phương trình chứa căn thức'
                    if ID[6] == '7':
                        Dang = '[7] Phương trình và bất phương trình chứa dấu giá trị tuyệt đối có tham số'
                    if ID[6] == '8':
                        Dang = '[8] Phương trình và bất phương trình chứa căn thức có tham số'
            if ID[2] == '5':
                Chuong = '[5] Thống kê'
                if ID[4] == '1':
                    Bai = '[1] Bảng phân bố tần số và tần suất'
                    if ID[6] == '1':
                        Dang = '[1] Bảng phân bố tần số và tần suất'
                    if ID[6] == '2':
                        Dang = '[2] Bảng phân bố tần số và tần suất ghép lớp'
                    if ID[6] == '3':
                        Dang = '[3] Câu hỏi lý thuyết'
                if ID[4] == '2':
                    Bai = '[2] Biểu đồ'
                    if ID[6] == '1':
                        Dang = '[1] Biểu đồ tần số và tần suất hình cột'
                    if ID[6] == '2':
                        Dang = '[2] Biểu đồ đường gấp khúc'
                    if ID[6] == '3':
                        Dang = '[3] Biểu đồ hình quạt'
                    if ID[6] == '4':
                        Dang = '[4] Câu hỏi lý thuyết'
                if ID[4] == '3':
                    Bai = '[3] Số trung bình cộng. Số trung vị. Mốt'
                    if ID[6] == '1':
                        Dang = '[1] Số trung bình cộng'
                    if ID[6] == '2':
                        Dang = '[2] Số trung vị'
                    if ID[6] == '3':
                        Dang = '[3] Mốt'
                    if ID[6] == '4':
                        Dang = '[4] Câu hỏi lý thuyết'
                if ID[4] == '4':
                    Bai = '[4] Phương sai và độ lệch chuẩn'
                    if ID[6] == '1':
                        Dang = '[1] Tính phương sai, độ lệch chuẩn dựa vào bảng số liệu cho trước'
                    if ID[6] == '2':
                        Dang = '[2] Câu hỏi lý thuyết'
            if ID[2] == '6':
                Chuong = '[6] Cung và góc lượng giác. Công thức lượng giác'
                if ID[4] == '1':
                    Bai = '[1] Cung và góc lượng giác'
                    if ID[6] == '1':
                        Dang = '[1] Mối liên hệ giữa độ và radian'
                    if ID[6] == '2':
                        Dang = '[2] Độ dài của một cung tròn'
                    if ID[6] == '3':
                        Dang = '[3] Biểu diễn cung lên đường tròn lượng giác'
                    if ID[6] == '4':
                        Dang = '[4] Các bài toán thực tế, liên môn'
                    if ID[6] == '5':
                        Dang = '[5] Câu hỏi lý thuyết'
                if ID[4] == '2':
                    Bai = '[2] Giá trị lượng giác của một cung'
                    if ID[6] == '1':
                        Dang = '[1] Xét dấu của các giá trị lượng giác'
                    if ID[6] == '2':
                        Dang = '[2] Tính giá trị lượng giác của một cung'
                    if ID[6] == '3':
                        Dang = '[3] Giá trị lượng giác của các cung có liên quan đặc biệt'
                    if ID[6] == '4':
                        Dang = '[4] Tìm giá trị lớn nhất, giá trị nhỏ nhất của biểu thức lượng giác'
                    if ID[6] == '5':
                        Dang = '[5] Rút gọn biểu thức lượng giác. Đẳng thức lượng giác'
                    if ID[6] == '6':
                        Dang = '[6] Các bài toán có yếu tố thực tế, liên môn'
                    if ID[6] == '7':
                        Dang = '[7] Câu hỏi lý thuyết'
                if ID[4] == '3':
                    Bai = '[3] Công thức lượng giác'
                    if ID[6] == '1':
                        Dang = '[1] Áp dụng công thức cộng'
                    if ID[6] == '2':
                        Dang = '[2] Áp dụng công thức nhân đôi - hạ bậc'
                    if ID[6] == '3':
                        Dang = '[3] Áp dụng công thức biến đổi tích thành tổng, tổng thành tích'
                    if ID[6] == '4':
                        Dang = '[4] Kết hợp các công thức lượng giác'
                    if ID[6] == '5':
                        Dang = '[5] Tìm giá trị lớn nhất, giá trị nhỏ nhất của biểu thức lượng giác'
                    if ID[6] == '6':
                        Dang = '[6] Nhận dạng tam giác'
                    if ID[6] == '7':
                        Dang = '[7] Các bài toán có yếu tố thực tế, liên môn'
                    if ID[6] == '8':
                        Dang = '[8] Câu hỏi lý thuyết'
    if ID[0] == '0':
        Lop = '[0] Lớp 10'
        if ID[1] == 'H':
            Mon = '[H] HÌNH HỌC'
            if ID[2] == '1':
                Chuong = '[1] Véc-tơ'
                if ID[4] == '1':
                    Bai = '[1] Các định nghĩa'
                    if ID[6] == '1':
                        Dang = '[1] Xác định một véc-tơ'
                    if ID[6] == '2':
                        Dang = '[2] Sự cùng phương và hướng của hai véc-tơ'
                    if ID[6] == '3':
                        Dang = '[3] Hai véc-tơ bằng nhau, độ dài của véc-tơ'
                if ID[4] == '2':
                    Bai = '[2] Tổng và hiệu của hai véc-tơ'
                    if ID[6] == '1':
                        Dang = '[1] Tổng của hai véc-tơ, tổng của nhiều véc-tơ'
                    if ID[6] == '2':
                        Dang = '[2] Chứng minh đẳng thức véc-tơ'
                    if ID[6] == '3':
                        Dang = '[3] Xác định vị trí của một điểm nhờ đẳng thức véc-tơ'
                    if ID[6] == '4':
                        Dang = '[4] Tìm véc-tơ đối, hiệu của hai véc-tơ'
                    if ID[6] == '5':
                        Dang = '[5] Tính độ dài của vec-tơ tổng, hiệu'
                if ID[4] == '3':
                    Bai = '[3] Tích của véc-tơ với một số'
                    if ID[6] == '1':
                        Dang = '[1] Xác định véc-tơ $k\\vec{a}$, tính độ dài véc-tơ'
                    if ID[6] == '2':
                        Dang = '[2] Chứng minh các đẳng thức véc-tơ, thu gọn biểu thức *'
                    if ID[6] == '3':
                        Dang = '[3] Xác định vị trí của một điểm nhờ đẳng thức véc-tơ'
                    if ID[6] == '4':
                        Dang = '[4] Phân tích một véc-tơ theo hai véc-tơ không cùng phương'
                    if ID[6] == '5':
                        Dang = '[5] Chứng minh ba điểm thẳng hàng, hai đường thẳng song song, hai điểmtrùng nhau'
                    if ID[6] == '6':
                        Dang = '[6] Tập hợp điểm'
                    if ID[6] == '7':
                        Dang = '[7] Cực trị'
                if ID[4] == '4':
                    Bai = '[4] Hệ trục toạ độ'
                    if ID[6] == '1':
                        Dang = '[1] Tìm tọa độ của một điểm và độ dài đại số của một véc-tơ trên trục $(O,\\vec(e))$'
                    if ID[6] == '2':
                        Dang = '[2] Tìm tọa độ các véc-tơ tổng, hiệu'
                    if ID[6] == '3':
                        Dang = '[3] Xác định tọa độ của véc-tơ và của một điểm trên mặt phẳng tọa độ $Oxy$'
                    if ID[6] == '4':
                        Dang = '[4] Phân tích một véc-tơ theo hai véc-tơ không cùng phương'
                    if ID[6] == '5':
                        Dang = '[5] Chứng minh ba điểm thẳng hàng, véc-tơ cùng phương, hai đường thẳngsong song'
            if ID[2] == '2':
                Chuong = '[2] Tích vô hướng của hai véc-tơ và ứng dụng'
                if ID[4] == '1':
                    Bai = '[1] Giá trị lượng giác của một góc bất kì từ $0^\\circ$đến $180^\\circ$'
                    if ID[6] == '1':
                        Dang = '[1] Xét dấu của các giá trị lượng giác'
                    if ID[6] == '2':
                        Dang = '[2] Tính các giá trị lượng giác'
                    if ID[6] == '3':
                        Dang = '[3] Chứng minh, rút gọn các biểu thức lượng giác'
                    if ID[6] == '4':
                        Dang = '[4] Xác định góc giữa hai véc-tơ, góc giữa hai đường thẳng'
                if ID[4] == '2':
                    Bai = '[2] Tích vô hướng'
                    if ID[6] == '1':
                        Dang = '[1] Tính tích vô hướng của hai véc-tơ và xác định góc **'
                    if ID[6] == '2':
                        Dang = '[2] Chứng minh đẳng thức về tích vô hướng hoặc độ dài'
                    if ID[6] == '3':
                        Dang = '[3] Điều kiện vuông góc'
                    if ID[6] == '4':
                        Dang = '[4] Các bài toán tìm điểm và tập hợp điểm **'
                    if ID[6] == '5':
                        Dang = '[5] Cực trị và chứng minh bất đẳng thức***'
                if ID[4] == '3':
                    Bai = '[3] Các hệ thức lượng trong tam giác'
                    if ID[6] == '1':
                        Dang = '[1] Tính toán các đại lượng trong tam giác'
                    if ID[6] == '2':
                        Dang = '[2] Chứng minh các hệ thức'
                    if ID[6] == '3':
                        Dang = '[3] Nhận dạng tam giác'
                    if ID[6] == '4':
                        Dang = '[4] Giải tam giác và các ứng dụng thực tế'
            if ID[2] == '3':
                Chuong = '[3] Phương pháp tọa độ trong mặt phẳng'
                if ID[4] == '1':
                    Bai = '[1] Phương trình đường thẳng'
                    if ID[6] == '1':
                        Dang = '[1] Xác định các yếu tố của đường thẳng'
                    if ID[6] == '2':
                        Dang = '[2] Viết phương trình đường thẳng'
                    if ID[6] == '3':
                        Dang = '[3] Vị trí tương đối giữa hai đường thẳng'
                    if ID[6] == '4':
                        Dang = '[4] Bài toán liên quan góc giữa hai đường thẳng'
                    if ID[6] == '5':
                        Dang = '[5] Bài toán liên quan công thức khoảng cách'
                    if ID[6] == '6':
                        Dang = '[6] Bài toán liên quan đến tìm điểm'
                    if ID[6] == '7':
                        Dang = '[7] Bài toán thực tế'
                if ID[4] == '2':
                    Bai = '[2] Phương trình đường tròn'
                    if ID[6] == '1':
                        Dang = '[1] Xác định tâm, bán kính và điều kiện là đường tròn'
                    if ID[6] == '2':
                        Dang = '[2] Viết phương trình đường tròn'
                    if ID[6] == '3':
                        Dang = '[3] Viết phương trình đường tiếp tuyến của đường tròn'
                    if ID[6] == '4':
                        Dang = '[4] Vị trí tương đối của đường tròn và đường thẳng, hai đường tròn'
                    if ID[6] == '5':
                        Dang = '[5] Các dạng toán tổng hợp đường thẳng và đường tròn'
                    if ID[6] == '6':
                        Dang = '[6] Bài toán thực tế'
                if ID[4] == '3':
                    Bai = '[3] Phương trình đường elip'
                    if ID[6] == '1':
                        Dang = '[1] Xác định các yếu tố của elip'
                    if ID[6] == '2':
                        Dang = '[2] Viết phương trình chính tắc của elip'
                    if ID[6] == '3':
                        Dang = '[3] Bài toán tìm điểm trên elip'
                    if ID[6] == '4':
                        Dang = '[4] Bài toán thực tế'
    if ID[0] == '1':
        Lop = '[1] Lớp 11'
        if ID[1] == 'D':
            Mon = '[D] ĐẠI SỐ & GIẢI TÍCH'
            if ID[2] == '1':
                Chuong = '[1] Hàm số lượng giác. Phương trình lượng giác'
                if ID[4] == '1':
                    Bai = '[1] Các hàm số lượng giác'
                    if ID[6] == '1':
                        Dang = '[1] Tìm tập xác định'
                    if ID[6] == '2':
                        Dang = '[2] Xét tính đơn điệu'
                    if ID[6] == '3':
                        Dang = '[3] Xét tính chẵn, lẻ'
                    if ID[6] == '4':
                        Dang = '[4] Xét tính tuần hoàn, tìm chu kỳ'
                    if ID[6] == '5':
                        Dang = '[5] Tìm tập giá trị và min-max'
                    if ID[6] == '6':
                        Dang = '[6] Bảng biến thiên và đồ thị'
                if ID[4] == '2':
                    Bai = '[2] Phương trình lượng giác cơ bản'
                    if ID[6] == '1':
                        Dang = '[1] Phương trình lượng giác cơ bản'
                if ID[4] == '3':
                    Bai = '[3] Phương trình lượng giác thường gặp'
                    if ID[6] == '1':
                        Dang = '[1] Phương trình bậc n theo một hàm số lượng giác'
                    if ID[6] == '2':
                        Dang = '[2] Phương trình đẳng cấp bậc n đối với sinx và cosx'
                    if ID[6] == '3':
                        Dang = '[3] Phương trình bậc nhất đối với sinx và cosx (a.sinx+bcosx=c)'
                    if ID[6] == '4':
                        Dang = '[4] Phương trình đối xứng, phản đối xứng'
                    if ID[6] == '5':
                        Dang = '[5] Phương trình lượng giác không mẫu mực'
                    if ID[6] == '6':
                        Dang = '[6] Phương trình lượng giác có chứa ẩn ở mẫu số'
                    if ID[6] == '7':
                        Dang = '[7] Phương trình lượng giác có chứa tham số'
                    if ID[6] == '8':
                        Dang = '[8] Bài toán thực tế'
            if ID[2] == '2':
                Chuong = '[2] Tổ hợp. Xác suất. Nhị thức Newton'
                if ID[4] == '1':
                    Bai = '[1] Quy tắc cộng-quy tắc nhân'
                    if ID[6] == '1':
                        Dang = '[1] Bài toán sử dụng quy tắc cộng'
                    if ID[6] == '2':
                        Dang = '[2] Bài toán sử dụng quy tắc nhân'
                    if ID[6] == '3':
                        Dang = '[3] Bài toán kết hợp quy tắc cộng và quy tắc nhân'
                if ID[4] == '2':
                    Bai = '[2] Hoán vị-chỉnh hợp-tổ hợp'
                    if ID[6] == '1':
                        Dang = '[1] Bài toán chỉ sử dụng P hoặc C hoặc A'
                    if ID[6] == '2':
                        Dang = '[2] Bài toán kết hợp P, C và A'
                    if ID[6] == '3':
                        Dang = '[3] Bài toán liên quan đến hình học'
                    if ID[6] == '4':
                        Dang = '[4] Hoán vị bàn tròn'
                    if ID[6] == '5':
                        Dang = '[5] Hoán vị lặp'
                    if ID[6] == '6':
                        Dang = '[6] Giải phương trình, bất phương trình, hệ, chứng minh liên quan đến P, C,A'
                if ID[4] == '3':
                    Bai = '[3] Nhị thức Newton'
                    if ID[6] == '1':
                        Dang = '[1] Khai triển một nhị thức Newton'
                    if ID[6] == '2':
                        Dang = '[2] Tìm hệ số, số hạng trong khai triển nhị thức Newton'
                    if ID[6] == '3':
                        Dang = '[3] Chứng minh, tính giá trị của biểu thức đại số tổ hợp có sử dụng nhị thứcNewton'
                if ID[4] == '4':
                    Bai = '[4] Phép thử và biến cố'
                    if ID[6] == '1':
                        Dang = '[1] Mô tả không gian mẫu, biến cố'
                    if ID[6] == '2':
                        Dang = '[2] Các câu hỏi lý thuyết tổng hợp'
                if ID[4] == '5':
                    Bai = '[5] Xác suất của biến cố'
                    if ID[6] == '1':
                        Dang = '[1] Các câu hỏi lý thuyết tổng hợp'
                    if ID[6] == '2':
                        Dang = '[2] Tính xác suất bằng định nghĩa'
                    if ID[6] == '3':
                        Dang = '[3] Tính xác suất bằng công thức cộng'
                    if ID[6] == '4':
                        Dang = '[4] Tính xác suất bằng công thức nhân'
                    if ID[6] == '5':
                        Dang = '[5] Bài toán kết hợp quy tắc cộng và quy tắc nhân xác suất'
            if ID[2] == '3':
                Chuong = '[3] Dãy số - Cấp số cộng- Cấp số nhân'
                if ID[4] == '1':
                    Bai = '[1] Phương pháp quy nạp'
                    if ID[6] == '1':
                        Dang = '[1] Các dạng toán áp dụng trực tiếp phương pháp quy nạp'
                    if ID[6] == '2':
                        Dang = '[2] Câu hỏi lý thuyết'
                if ID[4] == '2':
                    Bai = '[2] Dãy số'
                    if ID[6] == '1':
                        Dang = '[1] Biểu diễn dãy số, tìm công thức tổng quát dãy số'
                    if ID[6] == '2':
                        Dang = '[2] Tìm hạng tử trong dãy số'
                    if ID[6] == '3':
                        Dang = '[3] Dãy số tăng, dãy số giảm'
                    if ID[6] == '4':
                        Dang = '[4] Dãy số bị chặn trên, bị chặn dưới'
                    if ID[6] == '5':
                        Dang = '[5] Tìm giới hạn của dãy số'
                    if ID[6] == '6':
                        Dang = '[6] Câu hỏi lý thuyết'
                if ID[4] == '3':
                    Bai = '[3] Cấp số cộng'
                    if ID[6] == '1':
                        Dang = '[1] Nhận diện cấp số cộng'
                    if ID[6] == '2':
                        Dang = '[2] Tìm công thức của cấp số cộng'
                    if ID[6] == '3':
                        Dang = '[3] Tìm hạng tử trong cấp số cộng'
                    if ID[6] == '4':
                        Dang = '[4] Tìm điều kiện và chứng minh một dãy số là cấp số cộng *'
                    if ID[6] == '5':
                        Dang = '[5] Tính tổng của dãy nhiều số hạng liên quan đến cấp số cộng, tổng các hạngtử của cấp số cộng'
                    if ID[6] == '6':
                        Dang = '[6] Các bài toán thực tế'
                if ID[4] == '4':
                    Bai = '[4] Cấp số nhân'
                    if ID[6] == '1':
                        Dang = '[1] Nhận diện cấp số nhân'
                    if ID[6] == '2':
                        Dang = '[2] Tìm công thức của cấp số nhân'
                    if ID[6] == '3':
                        Dang = '[3] Tìm hạng tử trong cấp số nhân'
                    if ID[6] == '4':
                        Dang = '[4] Tìm điều kiện và chứng minh một dãy số là cấp số nhân *'
                    if ID[6] == '5':
                        Dang = '[5] Tính tổng của dãy nhiều số hạng liên quan đến cấp số nhân, tổng các hạngtử của cấp số nhân'
                    if ID[6] == '6':
                        Dang = '[6] Kết hợp cấp số nhân và cấp số cộng'
                    if ID[6] == '7':
                        Dang = '[7] Các bài toán thực tế'
            if ID[2] == '4':
                Chuong = '[4] Giới hạn'
                if ID[4] == '1':
                    Bai = '[1] Giới hạn của dãy số'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Nguyên lí kẹp'
                    if ID[6] == '3':
                        Dang = '[3] Dùng phương pháp đặt thừa số'
                    if ID[6] == '4':
                        Dang = '[4] Dùng lượng liên hợp'
                    if ID[6] == '5':
                        Dang = '[5] Cấp số nhân lùi vô hạn'
                    if ID[6] == '6':
                        Dang = '[6] Toán thực tế, liên môn liên quan đến giới hạn dãy số'
                if ID[4] == '2':
                    Bai = '[2] Giới hạn của hàm số'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Thay số trực tiếp'
                    if ID[6] == '3':
                        Dang = '[3] '
                    if ID[6] == '0':
                        Dang = '[0] vô cùng'
                    if ID[6] == '4':
                        Dang = '[4] '
                    if ID[6] == 'v':
                        Dang = '[v] vô cùng'
                    if ID[6] == '5':
                        Dang = '[5] Giới hạn một bên'
                    if ID[6] == '6':
                        Dang = '[6] Giới hạn bằng vô cùng'
                    if ID[6] == '7':
                        Dang = '[7] '
                    if ID[6] == 'v':
                        Dang = '[v] vô cùng, số chia vô cùng'
                    if ID[6] == '8':
                        Dang = '[8] Toán thực tế, liên môn về giới hạn hàm số'
                if ID[4] == '3':
                    Bai = '[3] Hàm số liên tục'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Xét tính liên tục bằng đồ thị'
                    if ID[6] == '3':
                        Dang = '[3] Hàm số liên tục tại một điểm'
                    if ID[6] == '4':
                        Dang = '[4] Hàm số liên tục trên khoảng, đoạn'
                    if ID[6] == '5':
                        Dang = '[5] Bài toán chứa tham số'
                    if ID[6] == '6':
                        Dang = '[6] Chứng minh phương trình có nghiệm'
                    if ID[6] == '7':
                        Dang = '[7] Toán thực tế, liên môn về hàm số liên tục'
            if ID[2] == '5':
                Chuong = '[5] Đạo hàm'
                if ID[4] == '1':
                    Bai = '[1] Đạo hàm và ý nghĩa của đạo hàm'
                    if ID[6] == '1':
                        Dang = '[1] Tính đạo hàm bằng định nghĩa'
                if ID[4] == '2':
                    Bai = '[2] Quy tắc tính đạo hàm'
                    if ID[6] == '1':
                        Dang = '[1] Tính đạo hàm và bài toán liên quan'
                    if ID[6] == '2':
                        Dang = '[2] Tiếp tuyến tại điểm'
                    if ID[6] == '3':
                        Dang = '[3] Tiếp tuyến cho sẵn hệ số góc, song song - vuông góc'
                    if ID[6] == '4':
                        Dang = '[4] Tiếp tuyến đi qua một điểm'
                    if ID[6] == '5':
                        Dang = '[5] Tổng hợp về tiếp tuyến và các kiến thức liên quan'
                    if ID[6] == '6':
                        Dang = '[6] Bài toán quãng đường, vận tốc, gia tốc'
                if ID[4] == '3':
                    Bai = '[3] Đạo hàm của các hàm số lượng giác'
                    if ID[6] == '1':
                        Dang = '[1] Tính đạo hàm và bài toán liên quan'
                    if ID[6] == '2':
                        Dang = '[2] Giới hạn hàm số lượng giác'
                if ID[4] == '4':
                    Bai = '[4] Vi phân'
                    if ID[6] == '1':
                        Dang = '[1] Tính vi phân và bài toán liên quan'
                if ID[4] == '5':
                    Bai = '[5] Đạo hàm cấp hai'
                    if ID[6] == '1':
                        Dang = '[1] Tính đạo hàm các cấp'
                    if ID[6] == '2':
                        Dang = '[2] Mối liên hệ giữa hàm số và đạo hàm các cấp'
                    if ID[6] == '3':
                        Dang = '[3] Ứng dụng vào tính tổng khai triển nhị thức và giới hạn**'
    if ID[0] == '1':
        Lop = '[1] Lớp 11'
        if ID[1] == 'H':
            Mon = '[H] HÌNH HỌC'
            if ID[2] == '1':
                Chuong = '[1] Phép dời hình và phép đồng dạng trong mặt phẳng'
                if ID[4] == '1':
                    Bai = '[1] Phép biến hình'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Bài toán xác định một phép đặt tương ứng có là phép dời hình hay không?'
                if ID[4] == '2':
                    Bai = '[2] Phép tịnh tiến'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Tìm ảnh hoặc tạo ảnh khi thực hiện phép tịnh tiến'
                    if ID[6] == '3':
                        Dang = '[3] Ứng dụng phép tịnh tiến'
                if ID[4] == '3':
                    Bai = '[3] Phép đối xứng trục'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Tìm ảnh hoặc tạo ảnh khi thực hiện phép đối xứng trục'
                    if ID[6] == '3':
                        Dang = '[3] Xác định trục đối xứng và số trục đối xứng của một hình'
                    if ID[6] == '4':
                        Dang = '[4] Ứng dụng phép đối xứng trục'
                if ID[4] == '4':
                    Bai = '[4] Phép đối xứng tâm'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Tìm ảnh, tạo ảnh khi thực hiện phép đối xứng tâm'
                    if ID[6] == '3':
                        Dang = '[3] Xác định hình có tâm đối xứng'
                    if ID[6] == '4':
                        Dang = '[4] Ứng dụng phép đối xứng tâm'
                if ID[4] == '5':
                    Bai = '[5] Phép quay'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Xác định vị trí ảnh của điểm, hình khi thực hiện phép quay cho trước'
                    if ID[6] == '3':
                        Dang = '[3] Tìm tọa độ ảnh của điểm, phương trình của một đường thẳng khi thựchiện phép quay'
                    if ID[6] == '4':
                        Dang = '[4] Ứng dụng phép quay'
                if ID[4] == '6':
                    Bai = '[6] Khái niệm về phép dời hình và hai hình bằng nhau'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Xác định ảnh khi thực hiện phép dời hình'
                if ID[4] == '7':
                    Bai = '[7] Phép vị tự'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Xác định ảnh, tạo ảnh khi thực hiện phép vị tự'
                    if ID[6] == '3':
                        Dang = '[3] Tìm tâm vị tự của hai đường tròn'
                    if ID[6] == '4':
                        Dang = '[4] Ứng dụng phép vị tự'
                if ID[4] == '8':
                    Bai = '[8] Phép đồng dạng'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Xác định ảnh, tạo ảnh khi thực hiện phép đồng dạng'
            if ID[2] == '2':
                Chuong = '[2] Quan hệ song song trong không gian'
                if ID[4] == '1':
                    Bai = '[1] Đại cương về đường thẳng và mặt phẳng'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Xác định giao tuyến của hai mặt phẳng'
                    if ID[6] == '3':
                        Dang = '[3] Tìm giao điểm của đường thẳng và mặt phẳng'
                    if ID[6] == '4':
                        Dang = '[4] Xác định thiết diện'
                    if ID[6] == '5':
                        Dang = '[5] Chứng minh ba điểm thẳng hàng đồng quy và ba đường thẳng đồng quy'
                    if ID[6] == '6':
                        Dang = '[6] Bài toán điểm cố định và quỹ tích của một điểm'
                if ID[4] == '2':
                    Bai = '[2] Hai đường thẳng chéo nhau và hai đường thẳng song song'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Chứng minh hai đường thẳng song song'
                    if ID[6] == '3':
                        Dang = '[3] Tìm giao điểm của đường thẳng và mặt phẳng'
                    if ID[6] == '4':
                        Dang = '[4] Tìm giao tuyến, thiết diện bằng cách kẻ song song *'
                    if ID[6] == '5':
                        Dang = '[5] Chứng minh ba điểm thẳng hàng'
                    if ID[6] == '6':
                        Dang = '[6] Xác định quỹ tích và các yếu tố định'
                if ID[4] == '3':
                    Bai = '[3] Đường thẳng và mặt phẳng song song'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Đường thẳng song song với mặt phẳng *'
                    if ID[6] == '3':
                        Dang = '[3] Giao tuyến của hai mặt phẳng *'
                    if ID[6] == '4':
                        Dang = '[4] Thiết diện *'
                    if ID[6] == '5':
                        Dang = '[5] Giao điểm *'
                if ID[4] == '4':
                    Bai = '[4] Hai mặt phẳng song song'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Hai mặt phẳng song song *'
                    if ID[6] == '3':
                        Dang = '[3] Giao tuyến của hai mặt phẳng *'
                    if ID[6] == '4':
                        Dang = '[4] Thiết diện *'
                    if ID[6] == '5':
                        Dang = '[5] Giao điểm *'
                    if ID[6] == '6':
                        Dang = '[6] Các bài toán tổng hợp'
                if ID[4] == '5':
                    Bai = '[5] Phép chiếu song song. Hình biểu diễn của một hình không gian'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Vẽ hình biểu diễn'
                    if ID[6] == '3':
                        Dang = '[3] Xác định song song'
            if ID[2] == '3':
                Chuong = '[3] Véc-tơ trong không gian. Quan hệ vuông góc trongkhông gian'
                if ID[4] == '1':
                    Bai = '[1] Véc-tơ trong không gian'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lý thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Đẳng thức véc-tơ'
                    if ID[6] == '3':
                        Dang = '[3] Phân tích véc-tơ theo các véc-tơ cho trước'
                    if ID[6] == '4':
                        Dang = '[4] Điều kiện đồng phẳng của ba véc-tơ'
                    if ID[6] == '5':
                        Dang = '[5] Ba điểm thẳng hàng, hai đường thẳng song song'
                if ID[4] == '2':
                    Bai = '[2] Hai đường thẳng vuông góc'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lí thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Xác định góc giữa hai véc-tơ (dùng định nghĩa)'
                    if ID[6] == '3':
                        Dang = '[3] Xác định góc giữa hai đường thẳng (dùng định nghĩa)'
                    if ID[6] == '4':
                        Dang = '[4] Ứng dụng tích vô hướng của hai véc-tơ'
                if ID[4] == '3':
                    Bai = '[3] Đường thẳng vuông góc với mặt phẳng'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lí thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Xác định quan hệ vuông góc giữa đường thẳng và mặt phẳng, đường thẳngvà đường thẳng'
                    if ID[6] == '3':
                        Dang = '[3] Xác định góc giữa mặt phẳng và đường thẳng'
                    if ID[6] == '4':
                        Dang = '[4] Dựng mặt phẳng vuông góc với đường thẳng cho trước. Thiết diện'
                if ID[4] == '4':
                    Bai = '[4] Hai mặt phẳng vuông góc'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lí thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Xác định quan hệ vuông góc giữa mặt phẳng và mặt phẳng, đường thẳngvà mặt phẳng'
                    if ID[6] == '3':
                        Dang = '[3] Xác định góc giữa hai mặt phẳng, đường và mặt *'
                    if ID[6] == '4':
                        Dang = '[4] Dựng mặt phẳng vuông góc với mặt phẳng cho trước. Thiết diện'
                    if ID[6] == '5':
                        Dang = '[5] Hình chiếu vuông góc của đa giác trên mặt phẳng'
                    if ID[6] == '6':
                        Dang = '[6] Góc giữa hai véc-tơ, hai đường thẳng trong các hình lăng trụ, lập phương'
                if ID[4] == '5':
                    Bai = '[5] Khoảng cách'
                    if ID[6] == '1':
                        Dang = '[1] Câu hỏi lí thuyết'
                    if ID[6] == '2':
                        Dang = '[2] Tính độ dài đoạn thẳng và khoảng cách từ một điểm đến đường thẳng ***'
                    if ID[6] == '3':
                        Dang = '[3] Khoảng cách từ một điểm đến một mặt phẳng'
                    if ID[6] == '4':
                        Dang = '[4] Khoảng cách giữa hai đường thẳng chéo nhau'
                    if ID[6] == '5':
                        Dang = '[5] Xác định đường vuông góc chung của hai đường thẳng chéo nhau'
    if ID[0] == '2':
        Lop = '[2] Lớp 12'
        if ID[1] == 'D':
            Mon = '[D] GIẢI TÍCH'
            if ID[2] == '1':
                Chuong = '[1] Ứng dụng đạo hàm để khảo sát hàm số'
                if ID[4] == '1':
                    Bai = '[1] Sự đồng biến và nghịch biến của hàm số'
                    if ID[6] == '1':
                        Dang = '[1] Xét tính đơn điệu của hàm số cho bởi công thức'
                    if ID[6] == '2':
                        Dang = '[2] Xét tính đơn điệu dựa vào bảng biến thiên, đồ thị'
                    if ID[6] == '3':
                        Dang = '[3] Tìm tham số m để hàm số đơn điệu'
                    if ID[6] == '4':
                        Dang = '[4] Ứng dụng tính đơn điệu để chứng minh bất đẳng thức, giải phương trình,bất phương trình, hệ phương trình'
                    if ID[6] == '5':
                        Dang = '[5] Câu hỏi lý thuyết'
                if ID[4] == '2':
                    Bai = '[2] Cực trị của hàm số'
                    if ID[6] == '1':
                        Dang = '[1] Tìm cực trị của hàm số cho bởi công thức'
                    if ID[6] == '2':
                        Dang = '[2] Tìm cực trị dựa vào BBT, đồ thị'
                    if ID[6] == '3':
                        Dang = '[3] Tìm m để hàm số đạt cực trị tại 1 điểm $x_0$ cho trước'
                    if ID[6] == '4':
                        Dang = '[4] Tìm m để hàm số, đồ thị hàm số bậc ba có cực trị thỏa mãn điều kiện'
                    if ID[6] == '5':
                        Dang = '[5] Tìm m để hàm số, đồ thị hàm số trùng phương có cực trị thỏa mãn điều kiện'
                    if ID[6] == '6':
                        Dang = '[6] Tìm m để hàm số, đồ thị hàm số các hàm số khác có cực trị thỏa mãn điềukiện'
                    if ID[6] == '7':
                        Dang = '[7] Câu hỏi lý thuyết'
                if ID[4] == '3':
                    Bai = '[3] Giá trị lớn nhất và giá trị nhỏ nhất của hàm số'
                    if ID[6] == '1':
                        Dang = '[1] GTLN, GTNN trên đoạn [a; b]'
                    if ID[6] == '2':
                        Dang = '[2] GTLN, GTNN trên khoảng'
                    if ID[6] == '3':
                        Dang = '[3] Sử dụng các đánh giá, bất đẳng thức cổ điển'
                    if ID[6] == '4':
                        Dang = '[4] Ứng dụng GTNN, GTLN trong bài toán phương trình, bất phương trình,hệ phương trình'
                    if ID[6] == '5':
                        Dang = '[5] GTLN, GTNN hàm nhiều biến'
                    if ID[6] == '6':
                        Dang = '[6] Bài toán ứng dụng, tối ưu, thực tế'
                    if ID[6] == '7':
                        Dang = '[7] Câu hỏi lý thuyết'
                if ID[4] == '4':
                    Bai = '[4] Đường tiệm cận'
                    if ID[6] == '1':
                        Dang = '[1] Bài toán xác định các đường tiệm cận của hàm số (không chứa tham số)hoặc biết BBT, đồ thị'
                    if ID[6] == '2':
                        Dang = '[2] Bài toán xác định các đường tiệm cận của hàm số có chứa tham số'
                    if ID[6] == '3':
                        Dang = '[3] Bài toán liên quan đến đồ thị hàm số và các đường tiệm cận'
                    if ID[6] == '4':
                        Dang = '[4] Câu hỏi lý thuyết'
                if ID[4] == '5':
                    Bai = '[5] Khảo sát sự biến thiên và vẽ đồ thị hàm số'
                    if ID[6] == '1':
                        Dang = '[1] Nhận dạng đồ thị, bảng biến thiên *'
                    if ID[6] == '2':
                        Dang = '[2] Các phép biến đổi đồ thị'
                    if ID[6] == '3':
                        Dang = '[3] Biện luận số giao điểm dựa vào đồ thị, bảng biến thiên'
                    if ID[6] == '4':
                        Dang = '[4] Sự tương giao của hai đồ thị (liên quan đến tọa độ giao điểm)'
                    if ID[6] == '5':
                        Dang = '[5] Đồ thị của hàm đạo hàm'
                    if ID[6] == '6':
                        Dang = '[6] Phương trình tiếp tuyến của đồ thị hàm số'
                    if ID[6] == '7':
                        Dang = '[7] Điểm đặc biệt của đồ thị hàm số'
                    if ID[6] == '8':
                        Dang = '[8] Câu hỏi lý thuyết'
            if ID[2] == '2':
                Chuong = '[2] Hàm số lũy thừa- Hàm số mũ và Hàm số lô-ga-rít'
                if ID[4] == '1':
                    Bai = '[1] Lũy thừa'
                    if ID[6] == '1':
                        Dang = '[1] Tính giá trị của biểu thức chứa lũy thừa'
                    if ID[6] == '2':
                        Dang = '[2] Biến đổi, rút gọn, biểu diễn các biểu thức chứa lũy thừa'
                    if ID[6] == '3':
                        Dang = '[3] So sánh các lũy thừa'
                if ID[4] == '2':
                    Bai = '[2] Hàm số lũy thừa'
                    if ID[6] == '1':
                        Dang = '[1] Tập xác định của hàm số chứa hàm lũy thừa'
                    if ID[6] == '2':
                        Dang = '[2] Đạo hàm hàm số lũy thừa'
                    if ID[6] == '3':
                        Dang = '[3] Khảo sát sự biến thiên và đồ thị hàm số lũy thừa'
                    if ID[6] == '4':
                        Dang = '[4] Tìm giá trị lớn nhất, giá trị nhỏ nhất của biểu thức chứa hàm lũy thừa'
                if ID[4] == '3':
                    Bai = '[3] Lô-ga-rít'
                    if ID[6] == '1':
                        Dang = '[1] Tính giá trị biểu thức chứa lô-ga-rít'
                    if ID[6] == '2':
                        Dang = '[2] Biến đổi, rút gọn, biểu diễn biểu thức chứa lô-ga-rít'
                    if ID[6] == '3':
                        Dang = '[3] So sánh các biểu thức lô-ga-rít'
                if ID[4] == '4':
                    Bai = '[4] Hàm số mũ. Hàm số lô-ga-rít'
                    if ID[6] == '1':
                        Dang = '[1] Tập xác định, tập giá trị của hàm số mũ, hàm số lô-ga-rít'
                    if ID[6] == '2':
                        Dang = '[2] Tính đạo hàm hàm số mũ, hàm số lô-ga-rít'
                    if ID[6] == '3':
                        Dang = '[3] Khảo sát sự biến thiên và đồ thị của hàm số mũ, lô-ga-rít'
                    if ID[6] == '4':
                        Dang = '[4] Tìm giá trị lớn nhất, nhỏ nhất của biểu thức chứa hàm mũ, hàm lô-ga-rít'
                    if ID[6] == '5':
                        Dang = '[5] Bài toán thực tế'
                    if ID[6] == '6':
                        Dang = '[6] Giới hạn, liên tục liên quan hàm số mũ, lô-ga-rít'
                    if ID[6] == '7':
                        Dang = '[7] Lý thuyết tổng hợp hàm số lũy thừa, mũ, lô-ga-rít'
                if ID[4] == '5':
                    Bai = '[5] Phương trình mũ và phương trình lô-ga-rít'
                    if ID[6] == '1':
                        Dang = '[1] Phương trình cơ bản'
                    if ID[6] == '2':
                        Dang = '[2] Phương pháp đưa về cùng cơ số'
                    if ID[6] == '3':
                        Dang = '[3] Phương pháp đặt ẩn phụ'
                    if ID[6] == '4':
                        Dang = '[4] Phương pháp lô-ga-rít hóa, mũ hóa'
                    if ID[6] == '5':
                        Dang = '[5] Phương pháp hàm số, đánh giá'
                    if ID[6] == '6':
                        Dang = '[6] Bài toán thực tế'
                    if ID[6] == '7':
                        Dang = '[7] Hệ phương trình mũ, lô-ga-rít'
                if ID[4] == '6':
                    Bai = '[6] Bất phương trình mũ và lô-ga-rít'
                    if ID[6] == '1':
                        Dang = '[1] Bất phương trình cơ bản'
                    if ID[6] == '2':
                        Dang = '[2] Phương pháp đưa về cùng cơ số'
                    if ID[6] == '3':
                        Dang = '[3] Phương pháp đặt ẩn phụ'
                    if ID[6] == '4':
                        Dang = '[4] Phương pháp lô-ga-rít hóa, mũ hóa'
                    if ID[6] == '5':
                        Dang = '[5] Phương pháp hàm số, đánh giá'
                    if ID[6] == '6':
                        Dang = '[6] Bài toán thực tế'
                    if ID[6] == '7':
                        Dang = '[7] Hệ bất phương trình mũ, lô-ga-rít'
            if ID[2] == '3':
                Chuong = '[3] Nguyên hàm, tích phân và ứng dụng'
                if ID[4] == '1':
                    Bai = '[1] Nguyên hàm'
                    if ID[6] == '1':
                        Dang = '[1] Định nghĩa, tính chất và nguyên hàm cơ bản'
                    if ID[6] == '2':
                        Dang = '[2] Phương pháp đổi biến số'
                    if ID[6] == '3':
                        Dang = '[3] Phương pháp nguyên hàm từng phần'
                if ID[4] == '2':
                    Bai = '[2] Tích phân'
                    if ID[6] == '1':
                        Dang = '[1] Định nghĩa, tính chất và tích phân cơ bản'
                    if ID[6] == '2':
                        Dang = '[2] Phương pháp đổi biến số'
                    if ID[6] == '3':
                        Dang = '[3] Phương pháp tích phân từng phần'
                    if ID[6] == '4':
                        Dang = '[4] Tích phân của hàm ẩn. Tích phân đặc biệt'
                if ID[4] == '3':
                    Bai = '[3] Ứng dụng của tích phân'
                    if ID[6] == '1':
                        Dang = '[1] Diện tích hình phẳng được giới hạn bởi các đồ thị'
                    if ID[6] == '2':
                        Dang = '[2] Bài toán thực tế sử dụng diện tích hình phẳng'
                    if ID[6] == '3':
                        Dang = '[3] Thể tích giới hạn bởi các đồ thị (tròn xoay)'
                    if ID[6] == '4':
                        Dang = '[4] Thể tích tính theo mặt cắt S(x)'
                    if ID[6] == '5':
                        Dang = '[5] Bài toán thực tế và ứng dụng thể tích'
                    if ID[6] == '6':
                        Dang = '[6] Ứng dụng vào tính tổng khai triển nhị thức'
                    if ID[6] == '7':
                        Dang = '[7] Ứng dụng tích phân vào bài toán liên môn (lý, hóa, sinh, kinh tế)***'
            if ID[2] == '4':
                Chuong = '[4] Số phức'
                if ID[4] == '1':
                    Bai = '[1] Khái niệm số phức'
                    if ID[6] == '1':
                        Dang = '[1] Xác định các yếu tố cơ bản của số phức'
                    if ID[6] == '2':
                        Dang = '[2] Biểu diễn hình học cơ bản của số phức'
                    if ID[6] == '3':
                        Dang = '[3] Câu hỏi lý thuyết'
                if ID[4] == '2':
                    Bai = '[2] Phép cộng, trừ và nhân số phức'
                    if ID[6] == '1':
                        Dang = '[1] Thực hiện phép tính'
                    if ID[6] == '2':
                        Dang = '[2] Xác định các yếu tố cơ bản của số phức qua các phép toán'
                    if ID[6] == '3':
                        Dang = '[3] Bài toán quy về giải phương trình, hệ phương trình nghiệm thực'
                    if ID[6] == '4':
                        Dang = '[4] Bài toán tập hợp điểm'
                    if ID[6] == '5':
                        Dang = '[5] Câu hỏi lý thuyết'
                if ID[4] == '3':
                    Bai = '[3] Phép chia số phức'
                    if ID[6] == '1':
                        Dang = '[1] Thực hiện phép tính'
                    if ID[6] == '2':
                        Dang = '[2] Xác định các yếu tố cơ bản của số phức qua các phép toán'
                    if ID[6] == '3':
                        Dang = '[3] Bài toán quy về giải phương trình, hệ phương trình nghiệm thực'
                    if ID[6] == '4':
                        Dang = '[4] Bài toán tập hợp điểm'
                    if ID[6] == '5':
                        Dang = '[5] Câu hỏi lý thuyết'
                if ID[4] == '4':
                    Bai = '[4] Phương trình bậc hai hệ số thực'
                    if ID[6] == '1':
                        Dang = '[1] Giải phương trình. Tính toán biểu thức nghiệm'
                    if ID[6] == '2':
                        Dang = '[2] Định lí Viet và ứng dụng'
                    if ID[6] == '3':
                        Dang = '[3] Phương trình quy về bậc hai'
                    if ID[6] == '4':
                        Dang = '[4] Câu hỏi lý thuyết'
                if ID[4] == '5':
                    Bai = '[5] Cực trị'
                    if ID[6] == '1':
                        Dang = '[1] Phương pháp hình học'
                    if ID[6] == '2':
                        Dang = '[2] Phương pháp đại số'
    if ID[0] == '2':
        Lop = '[2] Lớp 12'
        if ID[1] == 'H':
            Mon = '[H] HÌNH HỌC'
            if ID[2] == '1':
                Chuong = '[1] Khối đa diện'
                if ID[4] == '1':
                    Bai = '[1] Khái niệm về khối đa diện'
                    if ID[6] == '1':
                        Dang = '[1] Nhận diện hình đa diện, khối đa diện'
                    if ID[6] == '2':
                        Dang = '[2] Xác định số đỉnh, cạnh, mặt bên của một khối đa diện'
                    if ID[6] == '3':
                        Dang = '[3] Phân chia, lắp ghép các khối đa diện'
                    if ID[6] == '4':
                        Dang = '[4] Phép biến hình trong không gian'
                if ID[4] == '2':
                    Bai = '[2] Khối đa diện lồi và khối đa diện đều'
                    if ID[6] == '1':
                        Dang = '[1] Nhận diện đa diện lồi'
                    if ID[6] == '2':
                        Dang = '[2] Nhận diện loại đa diện đều'
                    if ID[6] == '3':
                        Dang = '[3] Tính chất đối xứng'
                if ID[4] == '3':
                    Bai = '[3] Khái niệm về thể tích của khối đa diện'
                    if ID[6] == '1':
                        Dang = '[1] Diện tích xung quanh, diện tích toàn phần của khối đa diện'
                    if ID[6] == '2':
                        Dang = '[2] Tính thể tích các khối đa diện'
                    if ID[6] == '3':
                        Dang = '[3] Tỉ số thể tích'
                    if ID[6] == '4':
                        Dang = '[4] Các bài toán khác(góc, khoảng cách,...) liên quan đến thể tích khối đa diện'
                    if ID[6] == '5':
                        Dang = '[5] Bài toán thực tế về khối đa diện'
                    if ID[6] == '6':
                        Dang = '[6] Bài toán cực trị'
            if ID[2] == '2':
                Chuong = '[2] Mặt nón, mặt trụ, mặt cầu'
                if ID[4] == '1':
                    Bai = '[1] Khái niệm về mặt tròn xoay'
                    if ID[6] == '1':
                        Dang = '[1] Thể tích khối nón, khối trụ'
                    if ID[6] == '2':
                        Dang = '[2] Diện tích xung quanh, diện tích toàn phần, độ dài đường sinh, chiều cao,bán kính đáy, thiết diện'
                    if ID[6] == '3':
                        Dang = '[3] Khối tròn xoay nội tiếp, ngoại tiếp khối đa diện'
                    if ID[6] == '4':
                        Dang = '[4] Bài toán thực tế về khối nón, khối trụ'
                    if ID[6] == '5':
                        Dang = '[5] Bài toán cực trị về khối nón, khối trụ'
                    if ID[6] == '6':
                        Dang = '[6] Câu hỏi lý thuyết'
                if ID[4] == '2':
                    Bai = '[2] Mặt cầu'
                    if ID[6] == '1':
                        Dang = '[1] Bài toán sử dụng định nghĩa, tính chất, vị trí tương đối'
                    if ID[6] == '2':
                        Dang = '[2] Khối cầu ngoại tiếp khối đa diện'
                    if ID[6] == '3':
                        Dang = '[3] Khối cầu nội tiếp khối đa diện'
                    if ID[6] == '4':
                        Dang = '[4] Bài toán thực tế về khối cầu'
                    if ID[6] == '5':
                        Dang = '[5] Bài toán cực trị về khối cầu'
                    if ID[6] == '6':
                        Dang = '[6] Bài toán tổng hợp về khối nón, khối trụ, khối cầu'
            if ID[2] == '3':
                Chuong = '[3] Phương pháp tọa độ trong không gian'
                if ID[4] == '1':
                    Bai = '[1] Hệ tọa độ trong không gian'
                    if ID[6] == '1':
                        Dang = '[1] Tìm tọa độ điểm, véc-tơ liên quan đến hệ trục $Oxyz$'
                    if ID[6] == '2':
                        Dang = '[2] Tích vô hướng và ứng dụng'
                    if ID[6] == '3':
                        Dang = '[3] Phương trình mặt cầu (xác định tâm, bán kính, viết PT mặt cầu đơn giản,vị trí tương đối hai mặt cầu, điểm đến mặt cầu, đơn giản)'
                    if ID[6] == '4':
                        Dang = '[4] Các bài toán cực trị'
                if ID[4] == '2':
                    Bai = '[2] Phương trình mặt phẳng'
                    if ID[6] == '1':
                        Dang = '[1] Tích có hướng và ứng dụng'
                    if ID[6] == '2':
                        Dang = '[2] Xác định VTPT'
                    if ID[6] == '3':
                        Dang = '[3] Viết phương trình mặt phẳng'
                    if ID[6] == '4':
                        Dang = '[4] Tìm tọa độ điểm liên quan đến mặt phẳng'
                    if ID[6] == '5':
                        Dang = '[5] Góc'
                    if ID[6] == '6':
                        Dang = '[6] Khoảng cách'
                    if ID[6] == '7':
                        Dang = '[7] Vị trí tương đối giữa hai mặt phẳng, giữa mặt cầu và mặt phẳng'
                    if ID[6] == '8':
                        Dang = '[8] Các bài toán cực trị'
                if ID[4] == '3':
                    Bai = '[3] Phương trình đường thẳng trong không gian'
                    if ID[6] == '1':
                        Dang = '[1] Xác định VTCP'
                    if ID[6] == '2':
                        Dang = '[2] Viết phương trình đường thẳng'
                    if ID[6] == '3':
                        Dang = '[3] Tìm tọa độ điểm liên quan đến đường thẳng'
                    if ID[6] == '4':
                        Dang = '[4] Góc'
                    if ID[6] == '5':
                        Dang = '[5] Khoảng cách'
                    if ID[6] == '6':
                        Dang = '[6] Vị trí tương đối giữa hai đường thẳng, giữa đường thẳng và mặt phẳng'
                    if ID[6] == '7':
                        Dang = '[7] Bài toán liên quan giữa đường thẳng - mặt phẳng - mặt cầu'
                    if ID[6] == '8':
                        Dang = '[8] Các bài toán cực trị'
                if ID[4] == '4':
                    Bai = '[4] Ứng dụng của phương pháp tọa độ'
                    if ID[6] == '1':
                        Dang = '[1] Bài toán HHKG'
                    if ID[6] == '2':
                        Dang = '[2] Bài toán đại số'
    if ID[3] == 'Y':
        Mucdo = '[Y] Nhận biết'
    if ID[3] == 'B':
        Mucdo = '[B] Thông hiểu'
    if ID[3] == 'K':
        Mucdo = '[K] Vận dụng thấp'
    if ID[3] == 'T':
        Mucdo = '[T] Bài toán thực tế'
    if ID[3] == 'G':
        Mucdo = '[G] Vận dụng cao'
    return (Lop, Mon, Chuong, Mucdo, Bai, Dang)


def Delete_file_rong(filename):
    content = ''
    with codecs.open(filename, 'r', 'utf-8') as (f):
        block = f.read()
        for line in block:
            content += line.strip()

        f.close()
    if content == '':
        os.unlink(filename)


def Call_ID_1(ID_1):
    list_ID1 = ['D', 'H']
    list_Mon = []
    if str(ID_1) == '2':
        list_Mon = [
         '[D] GIẢI TÍCH 12', '[H] HÌNH HỌC 12']
    if ID_1 == '1':
        list_Mon = [
         '[D] ĐẠI SỐ \\& GIẢI TÍCH 11', '[H] HÌNH HỌC 11']
    if ID_1 == '0':
        list_Mon = [
         '[D] ĐẠI SỐ 10', '[H] HÌNH HỌC 10']
    return (
     list_ID1, list_Mon)


def Call_ID_2(ID_1, ID_2):
    list_Chuong = []
    list_ID2 = []
    i = 1
    for ID in list_danh_sach_ID6:
        if str(ID_1) == ID[0] and str(ID_2) == ID[1] and ID[2] == str(i):
            i += 1
            list_ID2.append(ID[2])
            list_Chuong.append(ID_information_so(str(ID_1) + str(ID_2) + str(ID[2]) + '  ')[2])
            continue

    return (
     list_ID2, list_Chuong)


def Call_ID_3(ID_1, ID_2, ID_3):
    list_Bai = []
    list_ID3 = []
    i = 1
    for ID in list_danh_sach_ID6:
        if str(ID_1) == ID[0] and str(ID_2) == ID[1] and str(ID_3) == ID[2] and str(ID[4]) == str(i):
            i += 1
            list_ID3.append(ID[4])
            list_Bai.append(ID_information_so(str(ID_1) + str(ID_2) + str(ID_3) + '?' + ID[4] + '- ')[4])
            continue

    return (
     list_ID3, list_Bai)


def Call_ID_4(ID_1, ID_2, ID_3, ID_4):
    list_Dang = []
    list_ID4 = []
    i = 1
    for ID in list_danh_sach_ID6:
        if str(ID_1) == ID[0]:
            if str(ID_2) == ID[1]:
                if str(ID_3) == ID[2]:
                    if str(ID_4) == ID[4]:
                        list_ID4.append(ID[6])
                        list_Dang.append(ID_information_so(ID)[5])

    return (
     list_ID4, list_Dang)


def get_block_exbt(filename):
    block = codecs.open(filename, 'r', 'utf-8')
    found = False
    block_ID = ''
    i = 0
    for line in block:
        if found:
            block_ID += line
            if '\\end{ex}' in line.strip() or '\\end{bt}' in line.strip():
                found = False
                block_ID += '\n'
            else:
                if '\\begin{ex}' in line.strip() or '\\begin{bt}' in line.strip():
                    i = i + 1
                    found = True
                    block_ID += line

    return (
     block_ID, i)


def get_list_exbt(filename):
    block = codecs.open(filename, 'r', 'utf-8')
    found = False
    block_ID = ''
    List = []
    i = 0
    for line in block:
        if '\\begin{ex}' in line.strip() or '\\begin{bt}' in line.strip():
            i = i + 1
            found = True
            block_ID += line
        else:
            if found:
                block_ID += line
                if '\\end{ex}' in line.strip() or '\\end{bt}' in line.strip():
                    found = False
                    List.append(block_ID)
                    block_ID = ''
    return (List, i)


def get_block_ID_exbt(filename, ID, state):
    block = codecs.open(filename, 'r', 'utf-8')
    found = False
    block_ID = ''
    i = 0
    for line in block:
        if found:
            block_ID += line
        if '\\end{ex}' in line.strip() or '\\end{bt}' in line.strip():
            found = False
            block_ID += '\r\n'
        elif ID in line.strip():
            if '\\begin{ex}' in line.strip() or '\\begin{bt}' in line.strip():
                i = i + 1
                found = True
                if state:
                    block_ID += '%' + filename + '\r\n'
                block_ID += line

    return (
     block_ID, i)


def get_block_ID_spec(filename, ID, state):
    block = codecs.open(filename, 'r', 'utf-8')
    found = False
    block_ID = ''
    i = 0
    for line in block:
        if found:
            block_ID += line
        if '\\end{ex}' in line.strip():
            found = False
            block_ID += '\r\n'
        elif ID in line.strip():
            if '\\begin{ex}' in line.strip():
                i = i + 1
                found = True
                if state:
                    block_ID += '%' + filename + '\r\n'
                block_ID += line

    return (
     block_ID, i)


def get_block_ID_bt(filename, ID, state):
    block = codecs.open(filename, 'r', 'utf-8')
    found = False
    block_ID = ''
    i = 0
    for line in block:
        if found:
            block_ID += line
        if '\\end{bt}' in line.strip():
            found = False
        elif ID in line.strip():
            if '\\begin{bt}' in line.strip():
                i = i + 1
                found = True
                if state:
                    block_ID += '%' + filename + '\r\n'
                block_ID += line

    return (
     block_ID, i)


def get_block_ID_vd(filename, ID, state):
    block = codecs.open(filename, 'r', 'utf-8')
    found = False
    block_ID = ''
    i = 0
    for line in block:
        if found:
            block_ID += line
        if '\\end{vd}' in line.strip():
            found = False
        elif ID in line.strip():
            if '\\begin{vd}' in line.strip():
                i = i + 1
                found = True
                if state:
                    block_ID += '%' + filename + '\r\n'
                block_ID += line

    return (
     block_ID, i)


def Delete_file_rong(filename):
    content = ''
    with codecs.open(filename, 'r', 'utf-8') as (f):
        block = f.read()
        for line in block:
            content += line.strip()

        f.close()
    if content == '':
        os.unlink(filename)


def One_click_full_getID(fname, lop):
    list_danh_sach_ID6 = ['0D1?1-1', '0D1?1-2', '0D1?1-3', '0D1?1-4', '0D1?1-5', '0D1?2-1', '0D1?2-2', '0D1?3-1', '0D1?3-2', '0D1?3-3', '0D1?4-1', '0D1?4-2', '0D1?5-1', '0D1?5-2', '0D2?1-1', '0D2?1-2', '0D2?1-3', '0D2?1-4', '0D2?2-1', '0D2?2-2', '0D2?2-3', '0D2?2-4', '0D2?2-5', '0D2?3-1', '0D2?3-2', '0D2?3-3', '0D2?3-4', '0D2?3-5', '0D3?1-1', '0D3?1-2', '0D3?1-3', '0D3?2-1', '0D3?2-2', '0D3?2-3', '0D3?2-4', '0D3?2-5', '0D3?2-6', '0D3?3-1', '0D3?3-2', '0D3?3-3', '0D3?3-4', '0D3?3-5', '0D4?1-1', '0D4?1-2', '0D4?1-3', '0D4?1-4', '0D4?1-5', '0D4?2-1', '0D4?2-2', '0D4?2-3', '0D4?2-4', '0D4?2-5', '0D4?2-6', '0D4?3-1', '0D4?3-2', '0D4?3-3', '0D4?3-4', '0D4?3-5', '0D4?4-1', '0D4?4-2', '0D4?4-3', '0D4?4-4', '0D4?5-1', '0D4?5-2', '0D4?5-3', '0D4?5-4', '0D4?5-5', '0D4?5-6', '0D4?5-7', '0D4?5-8', '0D5?1-1', '0D5?1-2', '0D5?1-3', '0D5?2-1', '0D5?2-2', '0D5?2-3', '0D5?2-4', '0D5?3-1', '0D5?3-2', '0D5?3-3', '0D5?3-4', '0D5?4-1', '0D5?4-2', '0D6?1-1', '0D6?1-2', '0D6?1-3', '0D6?1-4', '0D6?1-5', '0D6?2-1', '0D6?2-2', '0D6?2-3', '0D6?2-4', '0D6?2-5', '0D6?2-6', '0D6?2-7', '0D6?3-1', '0D6?3-2', '0D6?3-3', '0D6?3-4', '0D6?3-5', '0D6?3-6', '0D6?3-7', '0D6?3-8', '0H1?1-1', '0H1?1-2', '0H1?1-3', '0H1?2-1', '0H1?2-2', '0H1?2-3', '0H1?2-4', '0H1?2-5', '0H1?3-1', '0H1?3-2', '0H1?3-3', '0H1?3-4', '0H1?3-5', '0H1?3-6', '0H1?3-7', '0H1?4-1', '0H1?4-2', '0H1?4-3', '0H1?4-4', '0H1?4-5', '0H2?1-1', '0H2?1-2', '0H2?1-3', '0H2?1-4', '0H2?2-1', '0H2?2-2', '0H2?2-3', '0H2?2-4', '0H2?2-5', '0H2?3-1', '0H2?3-2', '0H2?3-3', '0H2?3-4', '0H3?1-1', '0H3?1-2', '0H3?1-3', '0H3?1-4', '0H3?1-5', '0H3?1-6', '0H3?1-7', '0H3?2-1', '0H3?2-2', '0H3?2-3', '0H3?2-4', '0H3?2-5', '0H3?2-6', '0H3?3-1', '0H3?3-2', '0H3?3-3', '0H3?3-4', '1D1?1-1', '1D1?1-2', '1D1?1-3', '1D1?1-4', '1D1?1-5', '1D1?1-6', '1D1?2-1', '1D1?3-1', '1D1?3-2', '1D1?3-3', '1D1?3-4', '1D1?3-5', '1D1?3-6', '1D1?3-7', '1D1?3-8', '1D2?1-1', '1D2?1-2', '1D2?1-3', '1D2?2-1', '1D2?2-2', '1D2?2-3', '1D2?2-4', '1D2?2-5', '1D2?2-6', '1D2?3-1', '1D2?3-2', '1D2?3-3', '1D2?4-1', '1D2?4-2', '1D2?5-1', '1D2?5-2', '1D2?5-3', '1D2?5-4', '1D2?5-5', '1D3?1-1', '1D3?1-2', '1D3?2-1', '1D3?2-2', '1D3?2-3', '1D3?2-4', '1D3?2-5', '1D3?2-6', '1D3?3-1', '1D3?3-2', '1D3?3-3', '1D3?3-4', '1D3?3-5', '1D3?3-6', '1D3?4-1', '1D3?4-2', '1D3?4-3', '1D3?4-4', '1D3?4-5', '1D3?4-6', '1D3?4-7', '1D4?1-1', '1D4?1-2', '1D4?1-3', '1D4?1-4', '1D4?1-5', '1D4?1-6', '1D4?2-1', '1D4?2-2', '1D4?2-3', '1D4?2-4', '1D4?2-5', '1D4?2-6', '1D4?2-7', '1D4?2-8', '1D4?3-1', '1D4?3-2', '1D4?3-3', '1D4?3-4', '1D4?3-5', '1D4?3-6', '1D4?3-7', '1D5?1-1', '1D5?2-1', '1D5?2-2', '1D5?2-3', '1D5?2-4', '1D5?2-5', '1D5?2-6', '1D5?3-1', '1D5?3-2', '1D5?4-1', '1D5?5-1', '1D5?5-2', '1D5?5-3', '1H1?1-1', '1H1?1-2', '1H1?2-1', '1H1?2-2', '1H1?2-3', '1H1?3-1', '1H1?3-2', '1H1?3-3', '1H1?3-4', '1H1?4-1', '1H1?4-2', '1H1?4-3', '1H1?4-4', '1H1?5-1', '1H1?5-2', '1H1?5-3', '1H1?6-1', '1H1?6-2', '1H1?7-1', '1H1?7-2', '1H1?7-3', '1H1?7-4', '1H1?8-1', '1H1?8-2', '1H2?1-1', '1H2?1-2', '1H2?1-3', '1H2?1-4', '1H2?1-5', '1H2?1-6', '1H2?2-1', '1H2?2-2', '1H2?2-3', '1H2?2-4', '1H2?2-5', '1H2?2-6', '1H2?3-1', '1H2?3-2', '1H2?3-3', '1H2?3-4', '1H2?3-5', '1H2?4-1', '1H2?4-2', '1H2?4-3', '1H2?4-4', '1H2?4-5', '1H2?4-6', '1H2?5-1', '1H2?5-2', '1H2?5-3', '1H3?1-1', '1H3?1-2', '1H3?1-3', '1H3?1-4', '1H3?1-5', '1H3?2-1', '1H3?2-2', '1H3?2-3', '1H3?2-4', '1H3?3-1', '1H3?3-2', '1H3?3-3', '1H3?3-4', '1H3?4-1', '1H3?4-2', '1H3?4-3', '1H3?4-4', '1H3?4-5', '1H3?4-6', '1H3?5-1', '1H3?5-2', '1H3?5-3', '1H3?5-4', '1H3?5-5', '2D1?1-1', '2D1?1-2', '2D1?1-3', '2D1?1-4', '2D1?1-5', '2D1?2-1', '2D1?2-2', '2D1?2-3', '2D1?2-4', '2D1?2-5', '2D1?2-6', '2D1?2-7', '2D1?3-1', '2D1?3-2', '2D1?3-3', '2D1?3-4', '2D1?3-5', '2D1?3-6', '2D1?3-7', '2D1?4-1', '2D1?4-2', '2D1?4-3', '2D1?4-4', '2D1?5-1', '2D1?5-2', '2D1?5-3', '2D1?5-4', '2D1?5-5', '2D1?5-6', '2D1?5-7', '2D1?5-8', '2D2?1-1', '2D2?1-2', '2D2?1-3', '2D2?2-1', '2D2?2-2', '2D2?2-3', '2D2?2-4', '2D2?3-1', '2D2?3-2', '2D2?3-3', '2D2?4-1', '2D2?4-2', '2D2?4-3', '2D2?4-4', '2D2?4-5', '2D2?4-6', '2D2?4-7', '2D2?5-1', '2D2?5-2', '2D2?5-3', '2D2?5-4', '2D2?5-5', '2D2?5-6', '2D2?6-1', '2D2?6-2', '2D2?6-3', '2D2?6-4', '2D2?6-5', '2D2?6-6', '2D3?1-1', '2D3?1-2', '2D3?1-3', '2D3?2-1', '2D3?2-2', '2D3?2-3', '2D3?2-4', '2D3?3-1', '2D3?3-2', '2D3?3-3', '2D3?3-4', '2D3?3-5', '2D3?3-6', '2D4?1-1', '2D4?1-2', '2D4?1-3', '2D4?2-1', '2D4?2-2', '2D4?2-3', '2D4?2-4', '2D4?2-5', '2D4?3-1', '2D4?3-2', '2D4?3-3', '2D4?3-4', '2D4?3-5', '2D4?4-1', '2D4?4-2', '2D4?4-3', '2D4?4-4', '2D4?5-1', '2D4?5-2', '2H1?1-1', '2H1?1-2', '2H1?1-3', '2H1?1-4', '2H1?2-1', '2H1?2-2', '2H1?2-3', '2H1?3-1', '2H1?3-2', '2H1?3-3', '2H1?3-4', '2H1?3-5', '2H1?3-6', '2H2?1-1', '2H2?1-2', '2H2?1-3', '2H2?1-4', '2H2?1-5', '2H2?1-6', '2H2?2-1', '2H2?2-2', '2H2?2-3', '2H2?2-4', '2H2?2-5', '2H2?2-6', '2H3?1-1', '2H3?1-2', '2H3?1-3', '2H3?1-4', '2H3?2-1', '2H3?2-2', '2H3?2-3', '2H3?2-4', '2H3?2-5', '2H3?2-6', '2H3?2-7', '2H3?2-8', '2H3?3-1', '2H3?3-2', '2H3?3-3', '2H3?3-4', '2H3?3-5', '2H3?3-6', '2H3?3-7', '2H3?3-8', '2H3?4-1', '2H3?4-2']
    list_danh_sach_ID6_10 = list_danh_sach_ID6[:153]
    list_danh_sach_ID6_11 = list_danh_sach_ID6[153:316]
    list_danh_sach_ID6_12 = list_danh_sach_ID6[316:]
    so_cau = 0
    if str(lop) == '12':
        danh_sach = list_danh_sach_ID6_12
    else:
        if str(lop) == '11':
            danh_sach = list_danh_sach_ID6_11
        else:
            if str(lop) == '10':
                danh_sach = list_danh_sach_ID6_10
            else:
                danh_sach = [
                 lop]
    block = ''
    for filename in fname:
        for line in codecs.open(filename, 'r', 'utf-8'):
            block += line

    with codecs.open('Temp/full_tex.tex', 'w', 'utf-8') as (f):
        data = codecs.open(filename, 'r', 'utf-8')
        for line in data:
            f.write(line)

    for ID in danh_sach:
        ID1 = str(ID[0:3]) + 'X' + str(ID[4]) + '-' + str(ID[6])
        for i in ('Y', 'B', 'K', 'G', 'T'):
            ID2 = ID[0:3] + str(i) + ID[4] + '-' + ID[6]
            block_temp1 = ''
            block_temp, j = get_block_ID_spec('Temp/full_tex.tex', ID2)
            if block_temp == '':
                a = 1
            else:
                with codecs.open('Temp/' + ID2 + '.tex', 'w', 'utf-8') as (g):
                    so_cau += j
                    g.write(block_temp)
                    block_temp1 += block_temp
                    g.close()
                    shutil.copy2('Temp/' + ID2 + '.tex', 'ID/' + ID2 + '.tex')
                Delete_file_rong('Temp/' + ID2 + '.tex')

        with codecs.open('Temp/' + ID1 + '.tex', 'w', 'utf-8') as (f):
            block_temp1 = ''
            f.write(block_temp1)
            f.close()
        Delete_file_rong('Temp/' + ID1 + '.tex')


def ID_get_from(block):
    try:
        ID6 = ''
        for ID in re.findall('%\\[(.*?)\\]', block):
            try:
                int(ID[0]) + int(ID[2]) + int(ID[4])
            except Exception as er:
                pass

            if len(ID) <= 7:
                ID6 = ID
                break

    except Exception as er:
        pass

    return ID6


def ID_get_list(filename):
    block = codecs.open(filename, 'r', 'utf-8')
    list_ID = []
    for line in block:
        if '\\begin{ex}' in line:
            ID = ID_get_from(line)
            list_ID.append(ID)

    return list_ID


def ID_rut_gon(list_ID):
    listID_n = []
    temp = ''
    for ID in list_ID:
        if ID != temp:
            listID_n.append(ID)
            temp = ID

    return listID_n


def ID_arrange_YtoG(list_ID, type_arrange):
    list_ID_n = []
    for i in type_arrange:
        for ID in list_danh_sach_ID6:
            for ID_o in list_ID:
                ID_n = ID_o
                if ID.replace('?', i) == ID_n:
                    list_ID_n.append(ID_o)

    return ID_rut_gon(list_ID_n)


def ID_arrange_bai(list_ID, type_arrange):
    list_ID_n = []
    for ID in list_danh_sach_ID6:
        for i in type_arrange:
            for ID_o in list_ID:
                ID_n = ID_o
                if ID.replace('?', i) == ID_n:
                    list_ID_n.append(ID_o)

    return ID_rut_gon(list_ID_n)


def ID_arrange_mon(list_ID, type_arrange):
    list_ID_n = []
    for ID in list_danh_sach_ID6_10D + list_danh_sach_ID6_11D + list_danh_sach_ID6_12D:
        for i in type_arrange:
            for ID_o in list_ID:
                ID_n = ID_o
                if ID.replace('?', i) == ID_n:
                    list_ID_n.append(ID_o)

    for ID in list_danh_sach_ID6_10H + list_danh_sach_ID6_11H + list_danh_sach_ID6_12H:
        for i in type_arrange:
            for ID_o in list_ID:
                ID_n = ID_o
                if ID.replace('?', i) == ID_n:
                    list_ID_n.append(ID_o)

    return ID_rut_gon(list_ID_n)


def ID_file_arrange_YtoG(filename, type_arrange):
    list_ID = ID_get_list(filename)
    list_ID_n = ID_arrange_YtoG(list_ID, type_arrange)
    block = ''
    for ID in list_ID_n:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    return block


def ID_file_arrange_bai(filename, type_arrange):
    list_ID = ID_get_list(filename)
    list_ID_n = ID_arrange_bai(list_ID, type_arrange)
    block = ''
    for ID in list_ID_n:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    return block


def ID_file_arrange_mon(filename, type_arrange):
    list_ID = ID_get_list(filename)
    list_ID_n = ID_arrange_mon(list_ID, type_arrange)
    block = ''
    for ID in list_ID_n:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    return block


def ID_file_arrange_loi(filename, type_arrange):
    list_ID = ID_get_list(filename)
    ID_loi = []
    list_ID_n = ID_arrange_YtoG(list_ID, type_arrange)
    for ID1 in list_ID:
        if ID1 not in list_ID_n:
            if ID1 != '':
                ID_loi.append(ID1)

    block = ''
    if len(ID_loi) != 0:
        block += '%ID Lỗi\r\n'
    for ID in ID_loi:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    return (
     ID_loi, block)


def ID_arrange_YtoG_ID5(list_ID, type_arrange):
    list_ID_n = []
    for i in type_arrange:
        for ID in listID6_to_listID5(list_danh_sach_ID6):
            for ID_o in list_ID:
                ID_n = ID_o
                if ID.replace('?', i) == ID_n:
                    list_ID_n.append(ID_o)

    return ID_rut_gon(list_ID_n)


def ID_arrange_bai_ID5(list_ID, type_arrange):
    list_ID_n = []
    for ID in listID6_to_listID5(list_danh_sach_ID6):
        for i in type_arrange:
            for ID_o in list_ID:
                ID_n = ID_o
                if ID.replace('?', i) == ID_n:
                    list_ID_n.append(ID_o)

    return ID_rut_gon(list_ID_n)


def ID_arrange_mon_ID5(list_ID, type_arrange):
    list_ID_n = []
    for ID in listID6_to_listID5(list_danh_sach_ID6_10D) + listID6_to_listID5(list_danh_sach_ID6_11D) + listID6_to_listID5(list_danh_sach_ID6_12D):
        for i in type_arrange:
            for ID_o in list_ID:
                ID_n = ID_o
                if ID.replace('?', i) == ID_n:
                    list_ID_n.append(ID_o)

    for ID in listID6_to_listID5(list_danh_sach_ID6_10H) + listID6_to_listID5(list_danh_sach_ID6_11H) + listID6_to_listID5(list_danh_sach_ID6_12H):
        for i in type_arrange:
            for ID_o in list_ID:
                ID_n = ID_o
                if ID.replace('?', i) == ID_n:
                    list_ID_n.append(ID_o)

    return ID_rut_gon(list_ID_n)


def ID_file_arrange_YtoG_ID5(filename, type_arrange):
    list_ID = ID_get_list(filename)
    ID_loi = []
    list_ID_n = ID_arrange_YtoG_ID5(list_ID, type_arrange)
    for ID1 in list_ID:
        if ID1 not in list_ID_n:
            ID_loi.append(ID1)

    block = ''
    j = 0
    for ID in list_ID_n:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    block += '%ID Lỗi\r\n'
    for ID in ID_loi:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    return block


def ID_file_arrange_bai_ID5(filename, type_arrange):
    list_ID = ID_get_list(filename)
    ID_loi = []
    list_ID_n = ID_arrange_bai_ID5(list_ID, type_arrange)
    for ID1 in list_ID:
        if ID1 not in list_ID_n:
            ID_loi.append(ID1)

    block = ''
    j = 0
    for ID in list_ID_n:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    block += '%ID Lỗi\r\n'
    for ID in ID_loi:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    return block


def ID_file_arrange_mon_ID5(filename, type_arrange):
    list_ID = ID_get_list(filename)
    ID_loi = []
    list_ID_n = ID_arrange_mon_ID5(list_ID, type_arrange)
    for ID1 in list_ID:
        if ID1 not in list_ID_n:
            ID_loi.append(ID1)

    block = ''
    j = 0
    for ID in list_ID_n:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    block += '%ID Lỗi\r\n'
    for ID in ID_loi:
        block_ID, i = get_block_ID_spec(filename, ID, False)
        block += block_ID

    return block


def ID_thong_ke_ma_tran_ID6(filename, List_ID):
    List_ID_new = []
    Temp = ''
    Sum_Y = 0
    Sum_B = 0
    Sum_K = 0
    Sum_G = 0
    Sum_T = 0
    Sum_Sum = 0
    Y = 0
    B = 0
    K = 0
    G = 0
    T = 0
    Sum = 0
    i = 0
    for ID in List_ID:
        ID_new = ID.replace(ID[3], '?')
        i += 1
        try:
            Temp = List_ID[i].replace(List_ID[i][3], '?')
        except Exception as er:
            Temp = ''

        if ID.replace(ID[3], '?') != Temp:
            for ID_mau in List_ID:
                if ID_mau.replace(ID[3], '?') == ID_new:
                    block, Y = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'Y'), False)
                    block, B = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'B'), False)
                    block, K = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'K'), False)
                    block, G = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'G'), False)
                    block, T = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'T'), False)
                    Sum = Y + B + K + G + T

            if ID.replace(ID[3], '?') != Temp:
                if len(ID) == 7:
                    List_ID_new.append((ID_new.replace('?', 'X'), 'Dạng ' + ID_information_so(ID_new)[5], '', str(Y), str(B), str(K), str(G), str(T), str(Sum)))
                else:
                    if len(ID) == 5:
                        List_ID_new.append((ID_new.replace('?', 'X'), 'Bài ' + Call_ID_3(ID_new[0], ID_new[1], ID_new[2])[1][(int(ID_new[4]) - 1)], '', str(Y), str(B), str(K), str(G), str(T), str(Sum)))
            Sum_Y += Y
            Sum_B += B
            Sum_K += K
            Sum_G += G
            Sum_T += T
            Sum_Sum += Sum
            Y = 0
            B = 0
            K = 0
            G = 0
            T = 0
            Sum = 0

    List_ID_new.append(('', 'Tổng cộng', '', str(Sum_Y), str(Sum_B), str(Sum_K), str(Sum_G), str(Sum_T), str(Sum_Sum)))
    return List_ID_new


def ID_in_thong_ke_ma_tran(List_ID):
    block = ''
    for ID in List_ID:
        for content in ID:
            block += ' & ' + content

        block += '\\\\\r\n\\hline\r\n'

    return block


def listID6_to_listID5(listID6):
    try:
        listID5 = []
        i = 0
        j = 0
        temp = ''
        for ID6 in listID6:
            i += 1
            ID5 = ID6[:-2]
            if ID5 != temp:
                j += 1
                listID5.append(ID5)
                temp = ID5

    except Exception as er:
        print(er)

    return listID5


def ID_get_Tikz(filename):
    found = False
    block = codecs.open(filename, 'r', 'utf-8')
    block_Tikz = ''
    i = 0
    for line in block:
        if found:
            if '\\end{tikzpicture}' in line.strip():
                found = False
                block_Tikz += '\\end{tikzpicture}\n\n'
            else:
                block_Tikz += line
        elif '\\begin{tikzpicture}' in line.strip():
            i = i + 1
            found = True
            s = line.index('\\begin{tikzpicture}')
            block_Tikz += line[s:]

    return (
     block_Tikz, i)


def ID_information_so_full(ID):
    ID_info = ''
    try:
        if len(ID) == 7:
            ID_inf = ID_information_so(ID)
            ID_info = ID_inf[0] + '\nMôn: ' + ID_inf[1] + '\nChương: ' + ID_inf[2] + '\nBài: ' + ID_inf[4] + '\nDạng: ' + ID_inf[5] + '\nMức độ: ' + ID_inf[3]
        else:
            if len(ID) == 6:
                ID_inf = ID_information_so(ID + '1')
                ID_info = ID_inf[0] + '\nMôn: ' + ID_inf[1] + '\nChương: ' + ID_inf[2] + '\nBài: ' + ID_inf[4] + '\nMức độ: ' + ID_inf[3]
            else:
                if len(ID) == 5:
                    ID_inf = ID_information_so(ID + '-1')
                    ID_info = ID_inf[0] + '\nMôn: ' + ID_inf[1] + '\nChương: ' + ID_inf[2] + '\nBài: ' + ID_inf[4] + '\nMức độ: ' + ID_inf[3]
                else:
                    if len(ID) == 4:
                        ID_inf = ID_information_so(ID + '1-1')
                        ID_info = ID_inf[0] + '\nMôn: ' + ID_inf[1] + '\nChương: ' + ID_inf[2] + '\nMức độ: ' + ID_inf[3]
                    else:
                        if len(ID) == 3:
                            ID_inf = ID_information_so(ID + 'Y1-1')
                            ID_info = ID_inf[0] + '\nMôn: ' + ID_inf[1] + '\nChương: ' + ID_inf[2]
                        else:
                            if len(ID) == 2:
                                ID_inf = ID_information_so(ID + '1Y1-1')
                                ID_info = ID_inf[0] + '\nMôn: ' + ID_inf[1]
                            else:
                                if len(ID) == 1:
                                    ID_inf = ID_information_so(ID + 'D1Y1-1')
                                    ID_info = ID_inf[0]
    except Exception as er:
        ID_info = ''

    return ID_info


def Matrix_Count_Max_Test(Matran):
    Max = 1000
    for ID in Matran:
        for i in range(6, 11):
            if ID[i] != '0':
                Max = min(int(int(ID[(i - 5)]) / int(ID[i])), Max)

    return Max


def Matrix_Get_List(filename):
    ListID = ID_get_list(filename)
    List_ID = ID_arrange_bai(ListID, ['Y', 'B', 'K', 'G', 'T'])
    List_ID_new = []
    Temp = ''
    Y = 0
    B = 0
    K = 0
    G = 0
    T = 0
    Sum = 0
    i = 0
    for ID in List_ID:
        ID_new = ID.replace(ID[3], '?')
        i += 1
        try:
            Temp = List_ID[i].replace(List_ID[i][3], '?')
        except Exception as er:
            Temp = ''

        if ID.replace(ID[3], '?') != Temp:
            for ID_mau in List_ID:
                if ID_mau.replace(ID[3], '?') == ID_new:
                    try:
                        block, Y = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'Y'), False)
                        block, B = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'B'), False)
                        block, K = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'K'), False)
                        block, G = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'G'), False)
                        block, T = get_block_ID_spec(filename, ID_mau.replace(ID_mau[3], 'T'), False)
                        Sum = Y + B + K + G + T
                    except Exception as er:
                        pass

            if ID.replace(ID[3], '?') != Temp:
                if len(ID) == 7:
                    List_ID_new.append((ID_new.replace('?', 'X'), str(Y), str(B), str(K), str(G), str(T), str(Sum)))
                else:
                    if len(ID) == 5:
                        List_ID_new.append((ID_new.replace('?', 'X'), str(Y), str(B), str(K), str(G), str(T), str(Sum)))
            Y = 0
            B = 0
            K = 0
            G = 0
            T = 0
            Sum = 0

    return List_ID_new


def Matrix_Change_Table(List):
    List_ID_new = []
    for ID in List:
        ID_new = ID[0]
        if len(ID_new) == 7:
            List_ID_new.append((ID[0], 'Dạng ' + ID_information_so(ID_new)[5], '', ID[1], ID[2], ID[3], ID[4], ID[5]))
        elif len(ID_new) == 5:
            List_ID_new.append((ID[0], 'Bài ' + Call_ID_3(ID_new[0], ID_new[1], ID_new[2])[1][(int(ID_new[4]) - 1)], '', ID[1], ID[2], ID[3], ID[4], ID[5]))

    return List_ID_new