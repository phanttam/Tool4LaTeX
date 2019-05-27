# coding=utf-8
# def_Bank.py
import re, os, sys, csv, codecs, time
from datetime import datetime, timedelta
from urllib.request import urlopen
import math, argparse, subprocess, signal, shutil, errno, unicodedata, webbrowser
from fractions import Fraction
from decimal import Decimal
from random import *
from def_calculation import *
from src_reg import *
from def_id import *
from def_convert import *
from def_ban_quyen import *
list_danh_sach_ID6 = [
 '0D1?1-1', '0D1?1-2', '0D1?1-3', '0D1?1-4', '0D1?1-5', '0D1?2-1', '0D1?2-2', '0D1?3-1', '0D1?3-2', '0D1?3-3', '0D1?4-1', '0D1?4-2', '0D1?5-1', '0D1?5-2', '0D2?1-1', '0D2?1-2', '0D2?1-3', '0D2?1-4', '0D2?2-1', '0D2?2-2', '0D2?2-3', '0D2?2-4', '0D2?2-5', '0D2?3-1', '0D2?3-2', '0D2?3-3', '0D2?3-4', '0D2?3-5', '0D3?1-1', '0D3?1-2', '0D3?1-3', '0D3?2-1', '0D3?2-2', '0D3?2-3', '0D3?2-4', '0D3?2-5', '0D3?2-6', '0D3?3-1', '0D3?3-2', '0D3?3-3', '0D3?3-4', '0D3?3-5', '0D4?1-1', '0D4?1-2', '0D4?1-3', '0D4?1-4', '0D4?1-5', '0D4?2-1', '0D4?2-2', '0D4?2-3', '0D4?2-4', '0D4?2-5', '0D4?2-6', '0D4?3-1', '0D4?3-2', '0D4?3-3', '0D4?3-4', '0D4?3-5', '0D4?4-1', '0D4?4-2', '0D4?4-3', '0D4?4-4', '0D4?5-1', '0D4?5-2', '0D4?5-3', '0D4?5-4', '0D4?5-5', '0D4?5-6', '0D4?5-7', '0D4?5-8', '0D5?1-1', '0D5?1-2', '0D5?1-3', '0D5?2-1', '0D5?2-2', '0D5?2-3', '0D5?2-4', '0D5?3-1', '0D5?3-2', '0D5?3-3', '0D5?3-4', '0D5?4-1', '0D5?4-2', '0D6?1-1', '0D6?1-2', '0D6?1-3', '0D6?1-4', '0D6?1-5', '0D6?2-1', '0D6?2-2', '0D6?2-3', '0D6?2-4', '0D6?2-5', '0D6?2-6', '0D6?2-7', '0D6?3-1', '0D6?3-2', '0D6?3-3', '0D6?3-4', '0D6?3-5', '0D6?3-6', '0D6?3-7', '0D6?3-8', '0H1?1-1', '0H1?1-2', '0H1?1-3', '0H1?2-1', '0H1?2-2', '0H1?2-3', '0H1?2-4', '0H1?2-5', '0H1?3-1', '0H1?3-2', '0H1?3-3', '0H1?3-4', '0H1?3-5', '0H1?3-6', '0H1?3-7', '0H1?4-1', '0H1?4-2', '0H1?4-3', '0H1?4-4', '0H1?4-5', '0H2?1-1', '0H2?1-2', '0H2?1-3', '0H2?1-4', '0H2?2-1', '0H2?2-2', '0H2?2-3', '0H2?2-4', '0H2?2-5', '0H2?3-1', '0H2?3-2', '0H2?3-3', '0H2?3-4', '0H3?1-1', '0H3?1-2', '0H3?1-3', '0H3?1-4', '0H3?1-5', '0H3?1-6', '0H3?1-7', '0H3?2-1', '0H3?2-2', '0H3?2-3', '0H3?2-4', '0H3?2-5', '0H3?2-6', '0H3?3-1', '0H3?3-2', '0H3?3-3', '0H3?3-4', '1D1?1-1', '1D1?1-2', '1D1?1-3', '1D1?1-4', '1D1?1-5', '1D1?1-6', '1D1?2-1', '1D1?3-1', '1D1?3-2', '1D1?3-3', '1D1?3-4', '1D1?3-5', '1D1?3-6', '1D1?3-7', '1D1?3-8', '1D2?1-1', '1D2?1-2', '1D2?1-3', '1D2?2-1', '1D2?2-2', '1D2?2-3', '1D2?2-4', '1D2?2-5', '1D2?2-6', '1D2?3-1', '1D2?3-2', '1D2?3-3', '1D2?4-1', '1D2?4-2', '1D2?5-1', '1D2?5-2', '1D2?5-3', '1D2?5-4', '1D2?5-5', '1D3?1-1', '1D3?1-2', '1D3?2-1', '1D3?2-2', '1D3?2-3', '1D3?2-4', '1D3?2-5', '1D3?2-6', '1D3?3-1', '1D3?3-2', '1D3?3-3', '1D3?3-4', '1D3?3-5', '1D3?3-6', '1D3?4-1', '1D3?4-2', '1D3?4-3', '1D3?4-4', '1D3?4-5', '1D3?4-6', '1D3?4-7', '1D4?1-1', '1D4?1-2', '1D4?1-3', '1D4?1-4', '1D4?1-5', '1D4?1-6', '1D4?2-1', '1D4?2-2', '1D4?2-3', '1D4?2-4', '1D4?2-5', '1D4?2-6', '1D4?2-7', '1D4?2-8', '1D4?3-1', '1D4?3-2', '1D4?3-3', '1D4?3-4', '1D4?3-5', '1D4?3-6', '1D4?3-7', '1D5?1-1', '1D5?2-1', '1D5?2-2', '1D5?2-3', '1D5?2-4', '1D5?2-5', '1D5?2-6', '1D5?3-1', '1D5?3-2', '1D5?4-1', '1D5?5-1', '1D5?5-2', '1D5?5-3', '1H1?1-1', '1H1?1-2', '1H1?2-1', '1H1?2-2', '1H1?2-3', '1H1?3-1', '1H1?3-2', '1H1?3-3', '1H1?3-4', '1H1?4-1', '1H1?4-2', '1H1?4-3', '1H1?4-4', '1H1?5-1', '1H1?5-2', '1H1?5-3', '1H1?6-1', '1H1?6-2', '1H1?7-1', '1H1?7-2', '1H1?7-3', '1H1?7-4', '1H1?8-1', '1H1?8-2', '1H2?1-1', '1H2?1-2', '1H2?1-3', '1H2?1-4', '1H2?1-5', '1H2?1-6', '1H2?2-1', '1H2?2-2', '1H2?2-3', '1H2?2-4', '1H2?2-5', '1H2?2-6', '1H2?3-1', '1H2?3-2', '1H2?3-3', '1H2?3-4', '1H2?3-5', '1H2?4-1', '1H2?4-2', '1H2?4-3', '1H2?4-4', '1H2?4-5', '1H2?4-6', '1H2?5-1', '1H2?5-2', '1H2?5-3', '1H3?1-1', '1H3?1-2', '1H3?1-3', '1H3?1-4', '1H3?1-5', '1H3?2-1', '1H3?2-2', '1H3?2-3', '1H3?2-4', '1H3?3-1', '1H3?3-2', '1H3?3-3', '1H3?3-4', '1H3?4-1', '1H3?4-2', '1H3?4-3', '1H3?4-4', '1H3?4-5', '1H3?4-6', '1H3?5-1', '1H3?5-2', '1H3?5-3', '1H3?5-4', '1H3?5-5', '2D1?1-1', '2D1?1-2', '2D1?1-3', '2D1?1-4', '2D1?1-5', '2D1?2-1', '2D1?2-2', '2D1?2-3', '2D1?2-4', '2D1?2-5', '2D1?2-6', '2D1?2-7', '2D1?3-1', '2D1?3-2', '2D1?3-3', '2D1?3-4', '2D1?3-5', '2D1?3-6', '2D1?3-7', '2D1?4-1', '2D1?4-2', '2D1?4-3', '2D1?4-4', '2D1?5-1', '2D1?5-2', '2D1?5-3', '2D1?5-4', '2D1?5-5', '2D1?5-6', '2D1?5-7', '2D1?5-8', '2D2?1-1', '2D2?1-2', '2D2?1-3', '2D2?2-1', '2D2?2-2', '2D2?2-3', '2D2?2-4', '2D2?3-1', '2D2?3-2', '2D2?3-3', '2D2?4-1', '2D2?4-2', '2D2?4-3', '2D2?4-4', '2D2?4-5', '2D2?4-6', '2D2?4-7', '2D2?5-1', '2D2?5-2', '2D2?5-3', '2D2?5-4', '2D2?5-5', '2D2?5-6', '2D2?6-1', '2D2?6-2', '2D2?6-3', '2D2?6-4', '2D2?6-5', '2D2?6-6', '2D3?1-1', '2D3?1-2', '2D3?1-3', '2D3?2-1', '2D3?2-2', '2D3?2-3', '2D3?2-4', '2D3?3-1', '2D3?3-2', '2D3?3-3', '2D3?3-4', '2D3?3-5', '2D3?3-6', '2D4?1-1', '2D4?1-2', '2D4?1-3', '2D4?2-1', '2D4?2-2', '2D4?2-3', '2D4?2-4', '2D4?2-5', '2D4?3-1', '2D4?3-2', '2D4?3-3', '2D4?3-4', '2D4?3-5', '2D4?4-1', '2D4?4-2', '2D4?4-3', '2D4?4-4', '2D4?5-1', '2D4?5-2', '2H1?1-1', '2H1?1-2', '2H1?1-3', '2H1?1-4', '2H1?2-1', '2H1?2-2', '2H1?2-3', '2H1?3-1', '2H1?3-2', '2H1?3-3', '2H1?3-4', '2H1?3-5', '2H1?3-6', '2H2?1-1', '2H2?1-2', '2H2?1-3', '2H2?1-4', '2H2?1-5', '2H2?1-6', '2H2?2-1', '2H2?2-2', '2H2?2-3', '2H2?2-4', '2H2?2-5', '2H2?2-6', '2H3?1-1', '2H3?1-2', '2H3?1-3', '2H3?1-4', '2H3?2-1', '2H3?2-2', '2H3?2-3', '2H3?2-4', '2H3?2-5', '2H3?2-6', '2H3?2-7', '2H3?2-8', '2H3?3-1', '2H3?3-2', '2H3?3-3', '2H3?3-4', '2H3?3-5', '2H3?3-6', '2H3?3-7', '2H3?3-8', '2H3?4-1', '2H3?4-2']
list_danh_sach_ID6_10 = list_danh_sach_ID6[:153]
list_danh_sach_ID6_10D = list_danh_sach_ID6[:103]
list_danh_sach_ID6_10H = list_danh_sach_ID6[103:153]
list_danh_sach_ID6_11 = list_danh_sach_ID6[153:316]
list_danh_sach_ID6_11D = list_danh_sach_ID6[153:242]
list_danh_sach_ID6_11H = list_danh_sach_ID6[242:316]
list_danh_sach_ID6_12 = list_danh_sach_ID6[316:]
list_danh_sach_ID6_12D = list_danh_sach_ID6[316:408]
list_danh_sach_ID6_12H = list_danh_sach_ID6[408:]

def Bank_Creat_First(List_filename):
    for ID in listID6_to_listID5(list_danh_sach_ID6):
        lenght = len(listID6_to_listID5(list_danh_sach_ID6))
        i = 0
        k = 0
        block_ID = ''
        for filename in List_filename:
            for j in ('Y', 'B', 'K', 'G', 'T'):
                block, i = get_block_ID_spec(filename, ID.replace('?', j), False)
                if i != 0:
                    block_ID += block
                k += i

            with codecs.open('Bank//' + ID.replace('?', 'X') + '.tex', 'a+', 'utf-8') as (f):
                f.write(block_ID)
                f.close()
            block_ID = ''
            block = ''
            k = 0


def Bank_Get_Information():
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
    try:
        List = []
        Bank_Inf = ''
        i = 0
        for ID in list_danh_sach_ID6:
            ID_new = ID.replace('?', 'X')
            try:
                block, Y = get_block_ID_spec('Bank//' + ID_new[:-2] + '.tex', ID_new.replace(ID_new[3], 'Y'), False)
                block, B = get_block_ID_spec('Bank//' + ID_new[:-2] + '.tex', ID_new.replace(ID_new[3], 'B'), False)
                block, K = get_block_ID_spec('Bank//' + ID_new[:-2] + '.tex', ID_new.replace(ID_new[3], 'K'), False)
                block, G = get_block_ID_spec('Bank//' + ID_new[:-2] + '.tex', ID_new.replace(ID_new[3], 'G'), False)
                block, T = get_block_ID_spec('Bank//' + ID_new[:-2] + '.tex', ID_new.replace(ID_new[3], 'T'), False)
                Sum = Y + B + K + G + T
            except Exception as er:
                pass

            Bank_Inf += ID_new + ',' + str(Y) + ',' + str(B) + ',' + str(K) + ',' + str(G) + ',' + str(T) + ',' + str(Sum) + '\r\n'
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

    except Exception as er:
        pass

    with codecs.open('Bank//Bank_Information.dll', 'w', 'utf-8') as (f):
        f.write(Bank_Inf)
        f.close()
    return Bank_Inf


def Bank_General_Information(List_bank):
    Sum_Y = 0
    Sum_B = 0
    Sum_K = 0
    Sum_G = 0
    Sum_T = 0
    Sum_Sum = 0
    L10 = 0
    L11 = 0
    L12 = 0
    DS = 0
    HH = 0
    for ID in List_bank:
        Sum_Y += int(ID[1])
        Sum_B += int(ID[2])
        Sum_K += int(ID[3])
        Sum_G += int(ID[4])
        Sum_T += int(ID[5])
        Sum_Sum += int(ID[6])
        if ID[0][0] == '0':
            L10 += int(ID[6])
        else:
            if ID[0][0] == '1':
                L11 += int(ID[6])
            else:
                if ID[0][0] == '2':
                    L12 += int(ID[6])
        if ID[0][1] == 'D':
            DS += int(ID[6])
        elif ID[0][1] == 'H':
            HH += int(ID[6])

    return [
     (
      str(Sum_Y), str(Sum_B), str(Sum_K), str(Sum_G), str(Sum_T), str(Sum_Sum)), (str(L10), str(L11), str(L12), str(DS), str(HH))]


def Bank_get_List_fromID(filename, ID, state):
    block = codecs.open(filename, 'r', 'utf-8')
    found = False
    block_ID = ''
    i = 0
    Block = []
    for line in block:
        if found:
            block_ID += line
            if '\\end{ex}' in line.strip():
                found = False
                Block.append(str(block_ID))
                block_ID = ''
            else:
                if ID in line.strip():
                    i = i + 1
                    found = True
                    if state:
                        block_ID += '%' + filename + '\r\n'
                    block_ID += line

    return (
     Block, i)


def Bank_Get_Source(List_Matrix):
    Source = []
    for ID in List_Matrix:
        if 1 == 1:
            if ID[1] != '0':
                Block, i = Bank_get_List_fromID('Bank//' + ID[0][:-2] + '.tex', ID[0].replace('X', 'Y'), False)
                Source.append((ID[0].replace('X', 'Y'), ID[1], Block))
            if ID[2] != '0':
                Block, i = Bank_get_List_fromID('Bank//' + ID[0][:-2] + '.tex', ID[0].replace('X', 'B'), False)
                Source.append((ID[0].replace('X', 'B'), ID[2], Block))
            if ID[3] != '0':
                Block, i = Bank_get_List_fromID('Bank//' + ID[0][:-2] + '.tex', ID[0].replace('X', 'K'), False)
                Source.append((ID[0].replace('X', 'K'), ID[3], Block))
            if ID[4] != '0':
                Block, i = Bank_get_List_fromID('Bank//' + ID[0][:-2] + '.tex', ID[0].replace('X', 'G'), False)
                Source.append((ID[0].replace('X', 'G'), ID[4], Block))
            if ID[5] != '0':
                Block, i = Bank_get_List_fromID('Bank//' + ID[0][:-2] + '.tex', ID[0].replace('X', 'T'), False)
                Source.append((ID[0].replace('X', 'T'), ID[5], Block))

    return Source


def Bank_Creat_File(Source, filename, number):
    Test = []
    for i in range(0, number):
        De = []
        Test.append(De)

    for ID in Source:
        n = int(ID[1]) * number
        i = 0
        if 1 == 1:
            for cau_so in sample(range(0, len(ID[2])), n):
                Cau = ID[2][cau_so]
                if (i + 1) % number != 0:
                    Test[i].append(Cau)
                    i += 1
                else:
                    Test[i].append(Cau)
                    i = 0

    for i in range(0, number):
        with codecs.open('Matran//' + filename + str(i + 1) + '.tex', 'a+', 'utf-8') as (f):
            f.write('\\setcounter{ex}{0}\r\n\\Opensolutionfile{ans}[ans/ans-' + filename + str(i + 1) + ']\r\n')
            for j in Test[i]:
                f.write('\r\n' + j)

            f.write('\r\n\\Closesolutionfile{ans}')
        f.close()

    main = '\\documentclass[12pt,a4paper]{book}\r\n%\\usepackage{fourier}\r\n\\usepackage[utf8]{vietnam}\r\n\\usepackage{amsmath,amssymb,yhmath,mathrsfs,fancyhdr,tkz-euclide,tikz-3dplot}\r\n\\usepackage{framed,tikz,tkz-tab,tkz-linknodes,pgfplots,currfile,enumerate}\r\n\\usetikzlibrary{shapes.geometric,arrows,calc,intersections,angles,patterns,snakes,shadings,quotes}\r\n\\usetkzobj{all}\r\n\\usepgfplotslibrary{fillbetween}\r\n\\pgfplotsset{compat=1.9}\r\n\\usepackage[top=1.5cm, bottom=1.5cm, left=1.5cm, right=1.5cm] {geometry}\r\n\\usepackage[hidelinks,unicode,pdfencoding=unicode, psdextra]{hyperref}\r\n\\usepackage[loigiai]{ex_test}\r\n\\renewcommand{\\vec}[1]{\\protect\\overrightarrow{#1}}\r\n\\newcommand{\\hoac}[1]{\\left[\\begin{aligned}#1\\end{aligned}\\right.}\r\n\\newcommand{\\heva}[1]{\\left\\{\\begin{aligned}#1\\end{aligned}\\right.}\r\n\\renewcommand{\\labelenumi}{\\alph{enumi})}\r\n\\usepackage{multirow}\r\n\\usepackage{makecell}\r\n\\usepackage{lastpage}\r\n\\renewcommand{\\baselinestretch}{1.2}\r\n'
    try:
        block = codecs.open('Setting//Trangin.tex', 'r', 'utf-8')
        for line in block:
            main += line

    except Exception as er:
        pass

    main += '\\newcommand{\\hienda}{1}% 1: hiện đáp án, 0: không hiện đáp án\r\n\\ifthenelse{\\hienda=1}{\\newcommand{\\lamdapan}[1]{\r\n\\newpage\r\n\\begin{center}\r\n\\textbf{ĐÁP ÁN}\r\n\\end{center}\r\n\\begin{multicols}{10}\r\n\\input{#1}\r\n\\end{multicols}}}{\\newcommand{\\lamdapan}[1]{}} \r\n\\begin{document}\r\n'
    for i in range(0, number):
        if i == number - 1:
            main += '\\begin{center}\r\n\\textbf{ĐỀ SỐ ' + str(i + 1) + '}\r\n\\end{center}\r\n\\input{' + filename + str(i + 1) + '}\r\n\\lamdapan{ans/ans-' + filename + str(i + 1) + '}\r\n'
        else:
            main += '\\begin{center}\r\n\\textbf{ĐỀ SỐ ' + str(i + 1) + '}\r\n\\end{center}\r\n\\input{' + filename + str(i + 1) + '}\r\n\\lamdapan{ans/ans-' + filename + str(i + 1) + '}\r\n\\newpage\r\n'

    main += '\r\n\\end{document}'
    with codecs.open('Matran//main.tex', 'w', 'utf-8') as (f):
        f.write(main)
    return Test