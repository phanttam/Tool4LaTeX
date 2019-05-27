# coding=utf-8
# def_bbt.py
import re, os, sys, csv, codecs, time
from datetime import datetime, timedelta
from urllib.request import urlopen
import math, argparse, subprocess, signal, shutil, errno, unicodedata, webbrowser
from fractions import Fraction
from decimal import Decimal
from def_calculation import *
from src_reg import *
from def_bbt import *
from def_id import *
from def_convert import *
from def_ban_quyen import *

def view_dt_chuan(block):
    block = block.replace('++', '+')
    block = block.replace('+-', '-')
    block = block.replace('+0', '')
    block = block.replace('\\frac', '\\dfrac')
    return block


def view_he_so_a(num):
    if float(num) == 1:
        he_so_a = ''
    else:
        if float(num) == -1:
            he_so_a = '-'
        else:
            he_so_a = get_frac(num)
    return he_so_a


def view_he_so_b(num):
    if float(num) == 1:
        he_so_a = '+'
    else:
        if float(num) == -1:
            he_so_a = '-'
        else:
            if float(num) > 0:
                he_so_a = '+' + get_frac(num)
            else:
                he_so_a = get_frac(num)
    return he_so_a


def view_he_so_c(num):
    if float(num) == 0:
        he_so_a = ''
    else:
        if float(num) > 0:
            he_so_a = '+' + get_frac(num)
        else:
            he_so_a = get_frac(num)
    return he_so_a


def view_dt_bac_khong(a):
    if float(a) == 0:
        heso = '0'
    else:
        heso = get_frac(a)
    return heso


def view_dt_bac_nhat(a, b, x):
    if float(a) == 0:
        block = view_dt_bac_khong(b)
    else:
        block = view_he_so_a(a) + str(x) + view_he_so_c(b)
    block = view_dt_chuan(block)
    return block


def view_dt_bac_hai(a, b, c, x):
    if float(a) == 0:
        block = view_dt_bac_nhat(b, c, x=x)
    else:
        block = view_he_so_a(a) + str(x) + '^2+' + view_dt_bac_nhat(b, c, x=x)
    block = view_dt_chuan(block)
    return block


def view_dt_bac_ba(a, b, c, d, x):
    if float(a) == 0:
        block = view_dt_bac_hai(b, c, d, x=x)
    else:
        block = view_he_so_a(a) + str(x) + '^3+' + view_dt_bac_hai(b, c, d, x=x)
    block = view_dt_chuan(block)
    return block


def view_dt_bac_bon(a, b, c, d, e, x):
    if float(a) == 0:
        block = view_dt_bac_ba(b, c, d, e, x=x)
    else:
        block = view_he_so_a(a) + str(x) + '^4+' + view_dt_bac_ba(b, c, d, e, x=x)
    block = view_dt_chuan(block)
    return block


def bbt_bac_nhat_source(a, b):
    if a == 0:
        block = 'Hàm hằng không vẽ bảng biến thiên'
    else:
        block = ''
        block += "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$+\\infty$}\n"
        if a > 0:
            block += '\\tkzTabLine{,+,}\n\\tkzTabVar{-/$-\\infty$,+/$+\\infty$}\n'
        else:
            block += '\\tkzTabLine{,-,}\n\\tkzTabVar{+/$+\\infty$,-/$-\\infty$}\n'
        block += '\\end{tikzpicture}'
        return block


def bbt_bac_hai_source(a, b, c):
    d = float(-b / 2 / a)
    xi = get_frac(Fraction(d).limit_denominator())
    e = a * d ** 2 + b * d + c
    yi = get_frac(Fraction(e).limit_denominator())
    block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}{$-\\infty$,$" + xi + '$,$+\\infty$}\n'
    if float(a) > 0:
        block += '\\tkzTabLine{,-,0,+,}\n\\tkzTabVar{+/$+\\infty$,-/$' + yi + '$,+/$+\\infty$}\n\\end{tikzpicture}'
    else:
        block += '\\tkzTabLine{,+,0,-,}\n\\tkzTabVar{-/$-\\infty$,+/$' + yi + '$,-/$-\\infty$}\n\\end{tikzpicture}'
    return block


def bbt_bac_ba_source(a, b, c, d):

    def ham_f(x):
        y = a * x * x * x + b * x * x + c * x + d
        return y

    Delta = b * b - 3 * a * c
    xi = -b / 3 / a
    yi = ham_f(xi)
    if Delta < 0:
        if a > 0:
            block = bbt_bac_nhat_source(1, 0)
        else:
            block = bbt_bac_nhat_source(-1, 0)
    else:
        if Delta == 0:
            if a > 0:
                block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + get_frac(xi) + '$,$+\\infty$}\n\\tkzTabLine{,+,0,+,}\n\\tkzTabVar{-/$-\\infty$,R/,+/$+\\infty$}\n\\tkzTabVal{1}{3}{0.5}{}{$' + get_frac(yi) + '$}\n\\end{tikzpicture}\n'
            else:
                block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + get_frac(xi) + '$,$+\\infty$}\n\\tkzTabLine{,-,0,-,}\n\\tkzTabVar{+/$+\\infty$,R/,-/$-\\infty$}\n\\tkzTabVal{1}{3}{0.5}{}{$' + get_frac(yi) + '$}\n\\end{tikzpicture}\n'
        else:
            x_1, x_2, y_1, y_2 = Calc_CT_bac_ba(a, b, c, d)
            if a > 0:
                block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + x_1 + '$,$' + x_2 + '$,$+\\infty$}\n\\tkzTabLine{,+,0,-,0,+,}\n\\tkzTabVar{-/$-\\infty$,+/$' + str(y_1) + '$,-/$' + str(y_2) + '$,+/$+\\infty$}\n\\end{tikzpicture}\n'
            else:
                block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + x_1 + '$,$' + x_2 + '$,$+\\infty$}\n\\tkzTabLine{,-,0,+,0,-,}\n\\tkzTabVar{+/$+\\infty$,-/$' + str(y_1) + '$,+/$' + str(y_2) + '$,-/$-\\infty$}\n\\end{tikzpicture}\n'
    return block


def bbt_trung_phuong_source(a, b, c):
    yo = get_frac(c)
    i = 1
    if i == 1:
        if a * b >= 0:
            block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$0$,$+\\infty$}\n"
            if a > 0:
                block += '\\tkzTabLine{,-,0,+,}\n\\tkzTabVar{+/$+\\infty$,-/$' + yo + '$,+/$+\\infty$}\n'
            else:
                block += '\\tkzTabLine{,+,0,-,}\n\\tkzTabVar{-/$-\\infty$,+/$' + yo + '$,-/$-\\infty$}\n'
        else:
            e = -b / 2 / a
            d = math.sqrt(float(e))
            if float(d) == int(d):
                xi = str(int(d))
            else:
                if float(4 * a * d) == int(4 * a * d):
                    xi = get_frac(d)
                else:
                    y, z, w = get_sqrt_nor(-2 * a * b, 2 * a)
                    xi = ptbh_view(0, y, z, w)
            yi = get_frac(a * d ** 4 + b * d ** 2 + c)
            block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$-" + xi + '$,$0$,$' + xi + '$,$+\\infty$}\n'
            if a > 0:
                block += '\\tkzTabLine{,-,0,+,0,-,0,+,}\n\\tkzTabVar{+/$+\\infty$,-/$' + yi + '$,+/$' + yo + '$,-/$' + yi + '$,+/$+\\infty$}\n'
            else:
                block += '\\tkzTabLine{,+,0,-,0,+,0,-,}\n\\tkzTabVar{-/$-\\infty$,+/$' + yi + '$,-/$' + yo + '$,+/$' + yi + '$,-/$-\\infty$}\n'
        block += '\\end{tikzpicture}'
    return block


def bbt_mot_mot_source(a, b, c, d):

    def ham_f(x):
        y = (a * x + b) / (c * x + d)
        return y

    Delta = a * d - b * c
    xi = get_frac(-d / c)
    yi = get_frac(a / c)
    if c == 0:
        if d == 0:
            block = 'ERROR!!!\nDữ liệu hàm sai, mời các bạn nhập lại!'
        elif a == 0:
            block = 'Hàm số không đổi trên $\\mathbb{R}$.'
        elif float(a / d) > 0:
            block = bbt_bac_nhat_source(1, 0)
        else:
            block = bbt_bac_nhat_source(-1, 0)
    else:
        block = 'Bảng biến thiên của hàm số $y=\\dfrac{' + view_dt_bac_nhat(a, b, x='x') + '}{' + view_dt_bac_nhat(c, d, x='x') + '}$.\n\n'
    if Delta > 0:
        block += "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + xi + '$,$+\\infty$}\n\\tkzTabLine{,+,d,+,}\n\\tkzTabVar{-/$' + yi + '$,+D-/$+\\infty$/$-\\infty$,+/$' + yi + '$}\n\\end{tikzpicture}\n'
    else:
        if Delta < 0:
            block += "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + xi + '$,$+\\infty$}\n\\tkzTabLine{,-,d,-,}\n\\tkzTabVar{+/$' + yi + '$,-D+/$-\\infty$/$+\\infty$,-/$' + yi + '$}\n\\end{tikzpicture}\n'
        else:
            block += 'Hàm số không đổi trên $\\mathbb{R}\\setminus\\{' + xi + '\\}$.'
    return block


def bbt_hai_mot_source(a, b, c, m, n):

    def ham_f(x):
        y = (a * x * x + b * x + c) / (m * x + n)
        return y

    A = a * m
    B = a * n
    C = b * n - c * m
    Delta = B ** 2 - A * C
    if m == 0:
        block = bbt_bac_hai_source(a / n, b / n, c / n)
    else:
        if a == 0:
            if b * m - a * n != 0:
                block = bbt_mot_mot_source(b, c, m, n)
            else:
                block = 'Hàm số không đổi trên các khoảng xác định'
        else:
            if a * (-n / m) ** 2 + b * (-n / m) + c == 0:
                block = bbt_mot_mot_source(0, -a, m, n)
            else:
                xi = get_frac(-n / m)
                if Delta < 0:
                    if A > 0:
                        block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + xi + '$,$+\\infty$}\n\\tkzTabLine{,+,d,+,}\n\\tkzTabVar{-/$-\\infty$,+D-/$+\\infty$/$-\\infty$,+/$+\\infty$}\n\\end{tikzpicture}\n'
                    else:
                        block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + xi + '$,$+\\infty$}\n\\tkzTabLine{,-,d,-,}\n\\tkzTabVar{+/$+\\infty$,-D+/$-\\infty$/$+\\infty$,-/$-\\infty$}\n\\end{tikzpicture}\n'
                else:
                    x_1, x_2, y_1, y_2 = Calc_CT_hai_mot(a, b, c, m, n)
                    if A > 0:
                        block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + x_1 + '$,$' + xi + '$,$' + x_2 + '$,$+\\infty$}\n\\tkzTabLine{,+,0,-,d,-,0,+,}\n\\tkzTabVar{-/$-\\infty$,+/$' + y_1 + '$,-D+/$-\\infty$/$+\\infty$,-/$' + y_2 + '$,+/$+\\infty$}\n\\end{tikzpicture}\n'
                    else:
                        block = "\\begin{tikzpicture}\n\\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]\n{$x$/0.6,$y'$/0.6,$y$/2}\n{$-\\infty$,$" + x_1 + '$,$' + xi + '$,$' + x_2 + '$,$+\\infty$}\n\\tkzTabLine{,-,0,+,d,+,0,-,}\n\\tkzTabVar{+/$+\\infty$,-/$' + y_1 + '$,+D-/$+\\infty$/$-\\infty$,+/$' + y_2 + '$,-/$-\\infty$}\n\\end{tikzpicture}\n'
    return block


def dothi_hang_source(b, mien, diem, option):
    if mien == '':
        if option == '':
            Delta = 1
            xmin = str(-2)
            xmax = str(2)
            ymin = str(min(float(b) - Delta, -Delta))
            ymax = str(max(float(b) + Delta, Delta))
            dayx = ''
            dayy = ''
            for x in range(int(float(xmin)), int(float(xmax)) + 1):
                dayx += str(x) + ','

            for y in range(int(float(ymin)), int(float(ymax)) + 1):
                dayy += str(y) + ','

            dayx = dayx[:-1]
            dayy = dayy[:-1]
            dayx = dayx.replace(',0,', ',')
            dayy = dayy.replace(',0,', ',')
            scale = '1'
    block = '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n\\def\\xmin{' + xmin + '}\\def\\xmax{' + xmax + '}\\def\\ymin{' + ymin + '}\\def\\ymax{' + ymax + '}\n\\draw[->] (\\xmin-0.2,0)--(\\xmax+0.2,0) node[below] {\\footnotesize $x$};\n\\draw[->] (0,\\ymin-0.2)--(0,\\ymax+0.2) node[right] {$y$};\n\\draw (0,0) node [below left] {$O$};\n'
    if dayx != '':
        block += '\\foreach \\x in {' + dayx + '}\\draw (\\x,0.1)--(\\x,-0.1) node [below] {\\footnotesize $\\x$};\n'
    if dayy != '':
        block += '\\foreach \\y in {' + dayy + '}\\draw (0.1,\\y)--(-0.1,\\y) node [left] {\\footnotesize $\\y$};\n'
    block += '\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n\\draw[smooth,samples=200,domain=\\xmin:\\xmax] plot (\\x,{' + str(b) + '});\n'
    block += diem
    block += '\\end{tikzpicture}'
    return block


def dothi_bac_nhat_source(a, b, mien, diem, option):
    if mien == '':
        if option == '':
            if a != 0:
                k = -float(b) / float(a)
                Delta = 1
                xmin = str(min(k - Delta, -Delta))
                xmax = str(max(k + Delta, Delta))
                ymin = str(min(float(b) - Delta, -Delta))
                ymax = str(max(float(b) + Delta, Delta))
                dayx = ''
                dayy = ''
                for x in range(int(float(xmin)), int(float(xmax)) + 1):
                    dayx += str(x) + ','

                for y in range(int(float(ymin)), int(float(ymax)) + 1):
                    dayy += str(y) + ','

                dayx = dayx[:-1]
                dayy = dayy[:-1]
                dayx = dayx.replace(',0,', ',')
                dayy = dayy.replace(',0,', ',')
                scale = '1'
                block = '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n\\def\\xmin{' + xmin + '}\\def\\xmax{' + xmax + '}\\def\\ymin{' + ymin + '}\\def\\ymax{' + ymax + '}\n\\draw[->] (\\xmin-0.2,0)--(\\xmax+0.2,0) node[below] {\\footnotesize $x$};\n\\draw[->] (0,\\ymin-0.2)--(0,\\ymax+0.2) node[right] {$y$};\n\\draw (0,0) node [below left] {$O$};\n'
                if dayx != '':
                    block += '\\foreach \\x in {' + dayx + '}\\draw (\\x,0.1)--(\\x,-0.1) node [below] {\\footnotesize $\\x$};\n'
                if dayy != '':
                    block += '\\foreach \\y in {' + dayy + '}\\draw (0.1,\\y)--(-0.1,\\y) node [left] {\\footnotesize $\\y$};\n'
                block += '\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n\\draw[smooth,samples=200,domain=\\xmin:\\xmax] plot (\\x,{' + str(a) + '*(\\x)+' + str(b) + '});\n'
                block += diem
                block += '\\end{tikzpicture}'
            else:
                block = dothi_hang_source(b, '', '', '')
    return block


def dothi_bac_hai_source(a, b, c, mien, diem, option):
    if mien == '':
        if option == '':
            if a == 0:
                block = dothi_bac_nhat_source(a, b, mien, diem, option)
            else:
                xi = -float(b) / 2 / float(a)
                yi = -(float(b) * float(b) - 4 * float(a) * float(c)) / 4 / float(a)
                Deltax = 3
                Deltay = 4.5
                xmin = str(int(min(xi - Deltax, -1)))
                xmax = str(int(max(xi + Deltax, 1)))
                if float(a) > 0:
                    ymax = str(int(max(yi + Deltay, 1)))
                    if yi > 0:
                        ymin = '-1'
                    else:
                        ymin = str(int(yi - Deltay / 4))
                else:
                    ymin = str(min(yi - Deltay, -1))
                    if yi < 0:
                        ymax = '1'
                    else:
                        ymax = str(int(yi + Deltay / 4))
                dayx = ''
                dayy = ''
                for x in range(int(float(xmin)), int(float(xmax)) + 1):
                    dayx += str(x) + ','

                for y in range(int(float(ymin)), int(float(ymax)) + 1):
                    dayy += str(y) + ','

                dayx = dayx[:-1]
                dayy = dayy[:-1]
                dayx = dayx.replace(',0,', ',')
                dayy = dayy.replace(',0,', ',')
                scale = '1'
                block = '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n\\def\\xmin{' + xmin + '}\\def\\xmax{' + xmax + '}\\def\\ymin{' + ymin + '}\\def\\ymax{' + ymax + '}\n'
                block += '\\draw[->] (\\xmin-0.2,0)--(\\xmax+0.2,0) node[below] {\\footnotesize $x$};\n\\draw[->] (0,\\ymin-0.2)--(0,\\ymax+0.2) node[right] {\\footnotesize $y$};\n\\draw (0,0) node [below left] {\\footnotesize $O$};\n'
                if dayx != '':
                    block += '\\foreach \\x in {' + dayx + '}\\draw (\\x,0.1)--(\\x,-0.1) node [below] {\\footnotesize $\\x$};\n'
                if dayy != '':
                    block += '\\foreach \\y in {' + dayy + '}\\draw (0.1,\\y)--(-0.1,\\y) node [left] {\\footnotesize $\\y$};\n'
                block += '\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n'
                block += '\\draw[smooth,samples=200,domain=\\xmin:\\xmax] plot (\\x,{' + str(a) + '*((\\x)^2)+' + str(b) + '*\\x+' + str(c) + '});\n'
                block += dothi_diem(xi, yi, get_frac(xi), get_frac(yi))
                block += '\\end{tikzpicture}'
    return block


def dothi_bac_ba_source(a, b, c, d, mien, diem, option):
    if mien == '':
        if option == '':
            if a == 0:
                block = dothi_bac_hai_source(b, c, d, mien, diem, option)
            else:

                def ham_f(x):
                    y = a * x * x * x + b * x * x + c * x + d
                    return y

                Delta = b * b - 3 * a * c
                xi = -b / 3 / a
                yi = ham_f(xi)
                if Delta > 0:
                    x1 = (-1 * sign(float(a)) * float(b) - math.sqrt(Delta)) / 3 / float(a) / sign(float(a))
                    x2 = (-1 * sign(float(a)) * float(b) + math.sqrt(Delta)) / 3 / float(a) / sign(float(a))
                    y1 = ham_f(x1)
                    y2 = ham_f(x2)
                    x_1, x_2, y_1, y_2 = Calc_CT_bac_ba(a, b, c, d)
                else:
                    y1 = yi
                    y2 = yi
                Deltax = 3
                Deltay = 3
                xmin = str(int(min(xi - Deltax, -1)))
                xmax = str(int(max(xi + Deltax, 1)))
                ymin = str(int(min(yi - Deltay, y1 - 1, y2 - 1, -1)))
                ymax = str(int(max(yi + Deltay, y1 + 1, y2 + 1, 1)))
                dayx = ''
                dayy = ''
                for x in range(int(float(xmin)), int(float(xmax)) + 1):
                    dayx += str(x) + ','

                for y in range(int(float(ymin)), int(float(ymax)) + 1):
                    dayy += str(y) + ','

                dayx = dayx[:-1]
                dayy = dayy[:-1]
                dayx = dayx.replace(',0,', ',')
                dayy = dayy.replace(',0,', ',')
                scale = '1'
                block = '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n\\def\\xmin{' + xmin + '}\\def\\xmax{' + xmax + '}\\def\\ymin{' + ymin + '}\\def\\ymax{' + ymax + '}\n'
                block += '\\draw[->] (\\xmin-0.2,0)--(\\xmax+0.2,0) node[below] {\\footnotesize $x$};\n\\draw[->] (0,\\ymin-0.2)--(0,\\ymax+0.2) node[right] {\\footnotesize $y$};\n\\draw (0,0) node [below left] {\\footnotesize $O$};\n'
                if dayx != '':
                    block += '\\foreach \\x in {' + dayx + '}\\draw (\\x,0.1)--(\\x,-0.1) node [below] {\\footnotesize $\\x$};\n'
                if dayy != '':
                    block += '\\foreach \\y in {' + dayy + '}\\draw (0.1,\\y)--(-0.1,\\y) node [left] {\\footnotesize $\\y$};\n'
                block += '\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n'
                block += '\\draw[smooth,samples=200,domain=\\xmin:\\xmax] plot (\\x,{' + str(a) + '*((\\x)^3)+' + str(b) + '*((\\x)^2)+' + str(c) + '*(\\x)+' + str(d) + '});\n'
                block += dothi_diem(xi, yi, get_frac(xi), get_frac(yi))
                if Delta > 0:
                    block += dothi_diem(x1, y1, x_1, y_1)
                    block += dothi_diem(x2, y2, x_2, y_2)
                block += '\\end{tikzpicture}'
    return block


def dothi_trung_phuong_source(a, b, c, mien, diem, option):
    if mien == '':
        if option == '':
            if a == 0:
                block = dothi_bac_hai_source(b, 0, c, mien, diem, option)
            else:
                xi = '0'
                yi = float(c)
                if a * b < 0:
                    x1 = math.sqrt(-b / a / 2)
                    x2 = -math.sqrt(-b / a / 2)
                    Deltax = 1.5 * x1
                    yo = -b ** 2 / 4 / a + c
                else:
                    Deltax = 3
                    Deltay = 3.5
                    yo = yi
                xmin = str(int(min(-Deltax, -3)))
                xmax = str(int(max(Deltax, 3)))
                if float(a) > 0:
                    if float(b) > 0:
                        ymin = str(int(min(yi - 1, -1)))
                        ymax = str(int(max(yi + 4, 1)))
                    else:
                        ymin = str(int(min(yo - 1, -1)))
                        ymax = str(int(max(yi + 2, yo + 4, 1)))
                else:
                    if float(b) > 0:
                        ymin = str(int(min(yi - 2, yo - 4, -1)))
                        ymax = str(int(max(yo + 1, 1)))
                    else:
                        ymin = str(int(min(yi - 4, -1)))
                        ymax = str(int(max(yi + 1, 1)))
                dayx = ''
                dayy = ''
                for x in range(int(float(xmin)), int(float(xmax)) + 1):
                    dayx += str(x) + ','

                for y in range(int(float(ymin)), int(float(ymax)) + 1):
                    dayy += str(y) + ','

                dayx = dayx[:-1]
                dayy = dayy[:-1]
                dayx = dayx.replace(',0,', ',')
                dayy = dayy.replace(',0,', ',')
                scale = '1'
                block = '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n\\def\\xmin{' + xmin + '}\\def\\xmax{' + xmax + '}\\def\\ymin{' + ymin + '}\\def\\ymax{' + ymax + '}\n'
                block += '\\draw[->] (\\xmin-0.2,0)--(\\xmax+0.2,0) node[below] {\\footnotesize $x$};\n\\draw[->] (0,\\ymin-0.2)--(0,\\ymax+0.2) node[right] {\\footnotesize $y$};\n\\draw (0,0) node [below left] {\\footnotesize $O$};\n'
                if dayx != '':
                    block += '\\foreach \\x in {' + dayx + '}\\draw (\\x,0.1)--(\\x,-0.1) node [below] {\\footnotesize $\\x$};\n'
                if dayy != '':
                    block += '\\foreach \\y in {' + dayy + '}\\draw (0.1,\\y)--(-0.1,\\y) node [left] {\\footnotesize $\\y$};\n'
                block += '\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n'
                block += '\\draw[smooth,samples=200,domain=\\xmin:\\xmax] plot (\\x,{' + str(a) + '*((\\x)^4)+' + str(b) + '*((\\x)^2)+' + str(c) + '});\n'
                block += dothi_diem(0, float(c), '0', get_frac(c))
                if a * b < 0:
                    x_1, x_2 = Solve_ptbh(a, 0, 2 * b)
                    block += dothi_diem(x1, yo, x_1, '')
                    block += dothi_diem(x2, yo, x_2, get_frac(yo))
                block += '\\end{tikzpicture}'
    return block


def dothi_bac_mot_mot_source(a, b, c, d, mien, diem, option):
    if mien == '':
        if option == '':
            if c == 0 or a * d - b * c == 0:
                block = 'Nhập dữ liệu sai.'
            else:

                def ham_f(x):
                    y = (float(a) * x + float(b)) / (float(c) * x + float(d))
                    return y

                xi = round(-float(d) / float(c), 2)
                yi = round(float(a) / float(c), 2)
                Deltax = 3.5
                Deltay = 3.5
                xmin = str(int(min(xi - Deltax, -1)))
                xmax = str(int(max(xi + Deltax, 1)))
                ymin = str(int(min(yi - Deltay, yi - Deltay, -1)))
                ymax = str(int(max(yi + Deltay, yi + Deltay, 1)))
                dayx = ''
                dayy = ''
                for x in range(int(float(xmin)), int(float(xmax)) + 1):
                    dayx += str(x) + ','

                for y in range(int(float(ymin)), int(float(ymax)) + 1):
                    dayy += str(y) + ','

                dayx = dayx[:-1]
                dayy = dayy[:-1]
                dayx = dayx.replace(',0,', ',')
                dayy = dayy.replace(',0,', ',')
                scale = '1'
                block = '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n\\def\\xmin{' + xmin + '}\\def\\xmax{' + xmax + '}\\def\\ymin{' + ymin + '}\\def\\ymax{' + ymax + '}\n'
                block += '\\draw[->] (\\xmin-0.2,0)--(\\xmax+0.2,0) node[below] {\\footnotesize $x$};\n\\draw[->] (0,\\ymin-0.2)--(0,\\ymax+0.2) node[right] {\\footnotesize $y$};\n\\draw (0,0) node [below left] {\\footnotesize $O$};\n'
                if dayx != '':
                    block += '\\foreach \\x in {' + dayx + '}\\draw (\\x,0.1)--(\\x,-0.1) node [below] {\\footnotesize $\\x$};\n'
                if dayy != '':
                    block += '\\foreach \\y in {' + dayy + '}\\draw (0.1,\\y)--(-0.1,\\y) node [left] {\\footnotesize $\\y$};\n'
                block += '\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n'
                block += '\\draw[dashed] (\\xmin,' + str(yi) + ')--(\\xmax,' + str(yi) + ');\n'
                block += '\\draw[dashed] (' + str(xi) + ',\\ymin)--(' + str(xi) + ',\\ymax);\n'
                block += '\\draw[smooth,samples=200,domain=\\xmin:' + str(xi - 0.1) + '] plot (\\x,{(' + str(a) + '*(\\x)+' + str(b) + ')/(' + str(c) + '*(\\x)+' + str(d) + ')});\n'
                block += '\\draw[smooth,samples=200,domain=' + str(xi + 0.1) + ':\\xmax] plot (\\x,{(' + str(a) + '*(\\x)+' + str(b) + ')/(' + str(c) + '*(\\x)+' + str(d) + ')});\n'
                block += dothi_view_diem(xi, yi, get_frac(-d / c), get_frac(a / c))
                block += '\\end{tikzpicture}'
    return block


def dothi_bac_hai_mot_source(a, b, c, m, n, mien, diem, option):
    if mien == '':
        if option == '':
            if m == 0 or a * (-n / m) ** 2 + b * (-n / m) + c == 0 or a == 0:
                block = 'Nhập dữ liệu sai.'
            else:

                def ham_f(x):
                    y = (a * x * x + b * x + c) / (m * x + n)
                    return y

                A = a * m
                B = a * n
                C = b * n - c * m
                Delta = B ** 2 - A * C
                xi = round(-float(n) / float(m), 2)
                yi = round((b * m - 2 * a * n) / m ** 2, 2)
                x1 = round(xi - 0.5, 2)
                x2 = round(xi + 0.5, 2)
                x3 = x1 - 1
                x4 = x2 + 1
                try:
                    y1 = ham_f(x1)
                    y2 = ham_f(x2)
                    y3 = ham_f(x3)
                    y4 = ham_f(x4)
                except Exception as Er:
                    ii = 0

                Deltax = 4
                if Delta < 0:
                    Deltay = 4
                else:
                    Deltay = 3
                xmin = str(int(min(xi - Deltax, -1)))
                xmax = str(int(max(xi + Deltax, 1)))
                if Delta < 0:
                    ymin = str(int(min(yi - Deltay, -1)))
                    ymax = str(int(max(yi + Deltay, 1)))
                else:
                    x1 = (-1 * sign(A) * B - math.sqrt(Delta)) / sign(A) / A
                    x2 = (-1 * sign(A) * B + math.sqrt(Delta)) / sign(A) / A
                    y1 = ham_f(x1)
                    y2 = ham_f(x2)
                    ymin = str(int(min(y1 - Deltay, y2 - Deltay, -1)))
                    ymax = str(int(max(y1 + Deltay, y2 + Deltay, 1)))
                dayx = ''
                dayy = ''
                for x in range(int(float(xmin)), int(float(xmax)) + 1):
                    dayx += str(x) + ','

                for y in range(int(float(ymin)), int(float(ymax)) + 1):
                    dayy += str(y) + ','

                dayx = dayx[:-1]
                dayy = dayy[:-1]
                dayx = dayx.replace(',0,', ',')
                dayy = dayy.replace(',0,', ',')
                scale = '1'
                block = '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n\\def\\xmin{' + xmin + '}\\def\\xmax{' + xmax + '}\\def\\ymin{' + ymin + '}\\def\\ymax{' + ymax + '}\n'
                block += '\\draw[->] (\\xmin-0.2,0)--(\\xmax+0.2,0) node[below] {\\footnotesize $x$};\n\\draw[->] (0,\\ymin-0.2)--(0,\\ymax+0.2) node[right] {\\footnotesize $y$};\n\\draw (0,0) node [below left] {\\footnotesize $O$};\n'
                if dayx != '':
                    block += '\\foreach \\x in {' + dayx + '}\\draw (\\x,0.1)--(\\x,-0.1) node [below] {\\footnotesize $\\x$};\n'
                if dayy != '':
                    block += '\\foreach \\y in {' + dayy + '}\\draw (0.1,\\y)--(-0.1,\\y) node [left] {\\footnotesize $\\y$};\n'
                block += '\\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n'
                block += '\\draw[dashed] (' + str(xi) + ',\\ymin)--(' + str(xi) + ',\\ymax);\n'
                block += '\\draw[dashed,domain=\\xmin:\\xmax] plot (\\x,{' + str(a / m) + '*(\\x)+' + str((b * m - a * n) / m ** 2) + '});\n'
                block += '\\draw[smooth,samples=200,domain=\\xmin:' + str(xi - 0.1) + '] plot (\\x,{(' + str(a) + '*((\\x)^2)+' + str(b) + '*(\\x)+' + str(c) + ')/(' + str(m) + '*(\\x)+' + str(n) + ')});\n'
                block += '\\draw[smooth,samples=200,domain=' + str(xi + 0.1) + ':\\xmax] plot (\\x,{(' + str(a) + '*((\\x)^2)+' + str(b) + '*(\\x)+' + str(c) + ')/(' + str(m) + '*(\\x)+' + str(n) + ')});\n'
                if Delta > 0:
                    x_1, x_2, y_1, y_2 = Calc_CT_hai_mot(a, b, c, m, n)
                    x1 = (-1 * sign(A) * B - math.sqrt(Delta)) / sign(A) / A
                    x2 = (-1 * sign(A) * B + math.sqrt(Delta)) / sign(A) / A
                    y1 = ham_f(x1)
                    y2 = ham_f(x2)
                    block += dothi_diem(x1, y1, x_1, y_1)
                    block += dothi_diem(x2, y2, x_2, y_2)
                block += '\\end{tikzpicture}'
    return block


def dothi_diem(xi, yi, view_x, view_y):
    block = ''
    block += '\\draw[dashed] (' + str(round(xi + 0.001, 2)) + ',0)--(' + str(round(xi + 0.001, 2)) + ',' + str(round(yi + 0.001, 2)) + ')--(0,' + str(round(yi + 0.001, 2)) + ');\\fill (' + str(round(xi + 0.001, 2)) + ',' + str(round(yi + 0.001, 2)) + ') circle (1pt);\n'
    if int(xi) != float(xi):
        if view_x != '':
            if float(yi) < 0:
                block += '\\draw (' + str(round(xi + 0.001, 2)) + ',1pt)--(' + str(round(xi + 0.001, 2)) + ',-1pt) node [above] {\\footnotesize $' + view_x + '$};\n'
            else:
                block += '\\draw (' + str(round(xi + 0.001, 2)) + ',-1pt)--(' + str(round(xi + 0.001, 2)) + ',1pt) node [below] {\\footnotesize $' + view_x + '$};\n'
    if int(yi) != float(yi):
        if view_x != '':
            if float(xi) < 0:
                block += '\\draw (1pt,' + str(round(yi + 0.001, 2)) + ')--(-1pt,' + str(round(yi + 0.001, 2)) + ') node [right] {\\footnotesize $' + view_y + '$};\n'
            else:
                block += '\\draw (-1pt,' + str(round(yi + 0.001, 2)) + ')--(1pt,' + str(round(yi + 0.001, 2)) + ') node [left] {\\footnotesize $' + view_y + '$};\n'
    return block


def dothi_view_diem(xi, yi, view_x, view_y):
    block = ''
    if int(xi) != float(xi):
        if view_x != '':
            if float(yi) < 0:
                block += '\\draw (' + str(round(xi + 0.001, 2)) + ',1pt)--(' + str(round(xi + 0.001, 2)) + ',-1pt) node [above left] {\\footnotesize $' + view_x + '$};\n'
            else:
                block += '\\draw (' + str(round(xi + 0.001, 2)) + ',-1pt)--(' + str(round(xi + 0.001, 2)) + ',1pt) node [below right] {\\footnotesize $' + view_x + '$};\n'
    if int(yi) != float(yi):
        if view_x != '':
            if float(xi) < 0:
                block += '\\draw (1pt,' + str(round(yi + 0.001, 2)) + ')--(-1pt,' + str(round(yi + 0.001, 2)) + ') node [right] {\\footnotesize $' + view_y + '$};\n'
            else:
                block += '\\draw (-1pt,' + str(round(yi + 0.001, 2)) + ')--(1pt,' + str(round(yi + 0.001, 2)) + ') node [left] {\\footnotesize $' + view_y + '$};\n'
    return block


def get_mau_phanso(num):
    if '/' in num:
        a = str(Fraction(num).limit_denominator())
        s = a.index('/')
        mau = a[s + 1:]
    else:
        if '.' in num:
            a = str(Fraction(num).limit_denominator())
            s = a.index('/')
            mau = a[s + 1:]
        else:
            mau = '1'
    return mau


def get_tu_phanso(num):
    if '/' in num:
        a = str(Fraction(num).limit_denominator())
        s = a.index('/')
        mau = a[:s]
    else:
        if '.' in num:
            a = str(Fraction(num).limit_denominator())
            s = a.index('/')
            mau = a[:s]
        else:
            mau = num
    return mau