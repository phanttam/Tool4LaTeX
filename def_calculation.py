# coding=utf-8
# def_calculation.py
import re, os, sys, codecs, time, datetime, math, argparse, subprocess, signal, shutil, errno
from fractions import Fraction
from decimal import Decimal

def get_frac(num):
    try:
        m = Fraction(num).limit_denominator()
        if Fraction(m) == int(m):
            d = str(int(m))
        else:
            if '.' in str(Fraction(m).limit_denominator()):
                s = str(num).index('.')
                d = str(round(float(num) + 0.001, 2))
            else:
                if '/' in str(Fraction(m).limit_denominator()):
                    if float(num) > 0:
                        s = str(m).index('/')
                        a = str(m)[:s]
                        b = str(m)[s + 1:]
                        if len(b) > 6:
                            d = str(round(float(num) + 0.001, 2))
                        else:
                            d = '\\frac{' + a + '}{' + b + '}'
                    else:
                        s = str(m).index('/')
                        a = str(m)[1:s]
                        b = str(m)[s + 1:]
                        if len(b) > 4:
                            d = str(round(n + 0.001, 2))
                        else:
                            d = '-\\frac{' + a + '}{' + b + '}'
                else:
                    d = str(round(num + 0.001, 2))
    except Exception as err:
        d = str(round(num + 0.001, 2))

    return d


def frac_dfrac(num):
    num = str(num).replace('\\frac', '\\dfrac')
    return num


def get_dfrac(num):
    num = get_frac(num).replace('\\frac', '\\dfrac')
    return num


def get_frac_nor(a, b):
    m = Fraction(a / b).limit_denominator()
    if float(m) != int(m):
        s = str(m).index('/')
        c = int(str(m)[:s])
        d = int(str(m)[s + 1:])
    else:
        c = int(m)
        d = 1
    return (
     c, d)


def sign(number):
    if float(number) > 0:
        d = 1
    else:
        if float(number) < 0:
            d = -1
        else:
            d = 0
    return d


def sign_str(number):
    if float(number) > 0:
        d = '+'
    else:
        if float(number) < 0:
            d = ''
        else:
            d = ''
    return d


def sign_heso(number):
    if float(number) > 0:
        d = '+'
    else:
        if float(number) < 0:
            d = '-'
        else:
            d = ''
    return d


def sign_ineq(number):
    if float(number) > 0:
        d = '>'
    else:
        if float(number) < 0:
            d = '<'
        else:
            d = '='
    return d


def sign_ngoactron(number, sign):
    if sign == '-':
        d = '\\left(' + str(number) + '\\right)'
    else:
        d = str(number)
    return d


def get_sqrt_nor(a, b):
    c, d = get_frac_nor(a, b ** 2)
    n = float(c) * float(d)
    for i in range(1, int(n)):
        j = i * i
        if int(n + 0.001) % j == 0:
            e = i

    y = int(float(c) * float(d) / e ** 2)
    x, z = get_frac_nor(e, int(d))
    return (
     x, y, z)


def ptbh_view(x, y, z, w):
    tu = ''
    if x == 0:
        if y == 1:
            tu = '\\sqrt{' + str(z) + '}'
        elif y == -1:
            tu = '-\\sqrt{' + str(z) + '}'
        elif y == 0:
            tu = '0'
        else:
            tu = str(y) + '\\sqrt{' + str(z) + '}'
    else:
        if y == 1:
            tu = str(x) + '+\\sqrt{' + str(z) + '}'
        else:
            if y == -1:
                tu = str(x) + '-\\sqrt{' + str(z) + '}'
            else:
                if y == 0:
                    tu = str(x)
                else:
                    tu = str(x) + sign_str(y) + str(y) + '\\sqrt{' + str(z) + '}'
    if w == 1:
        nghiem = tu
    else:
        nghiem = '\\frac{' + tu + '}{' + str(w) + '}'
    return nghiem


def get_tu_mau_phanso(num):
    a = str(Fraction(num).limit_denominator())
    if '/' in a:
        s = a.index('/')
        tu = int(a[:s])
        mau = int(a[s + 1:])
    else:
        tu = num
        mau = 1
    return (tu, mau)


def get_tu_phanso(num):
    a = str(Fraction(num).limit_denominator())
    if '/' in a:
        s = a.index('/')
        tu = int(a[:s])
    else:
        tu = num
    return (tu, mau)


def get_mau_phanso(num):
    a = str(Fraction(num).limit_denominator())
    if '/' in a:
        s = a.index('/')
        mau = int(a[s + 1:])
    else:
        mau = 1
    return mau


def quy_dong_bac_hai(a, b, c):
    mau_a = get_mau_phanso(a)
    mau_b = get_mau_phanso(b)
    mau_c = get_mau_phanso(c)
    M = mau_a * mau_b * mau_c / math.gcd(mau_a, math.gcd(mau_b, mau_c))
    A = M * float(a)
    B = M * float(b)
    C = M * float(c)
    return (
     A, B, C)


def Solve_ptbh(a, b, c):
    a, b, c = quy_dong_bac_hai(a, b, c)
    Delta = b * b - 4 * a * c
    if Delta > 0:
        x_1 = float((-sign(a) * b - math.sqrt(Delta)) / 2 / sign(a) / a)
        x_2 = float((-sign(a) * b + math.sqrt(Delta)) / 2 / sign(a) / a)
        if int(math.sqrt(Delta)) == float(math.sqrt(Delta)):
            nx_1 = get_frac(Fraction(x_1))
            nx_2 = get_frac(Fraction(x_2))
        else:
            d, e = get_frac_nor(-b, 2 * a)
            m, n, p = get_sqrt_nor(Delta, 2 * a)
            if d == 0:
                nx_1 = ptbh_view(0, -m, n, p)
                nx_2 = ptbh_view(0, m, n, p)
            else:
                w = int(e * p / math.gcd(e, p))
                x = int(d * w / e)
                y = int(m * w / p)
                z = n
                nx_1 = ptbh_view(x, -y, z, w)
                nx_2 = ptbh_view(x, y, z, w)
    return (
     nx_1, nx_2)


def Calc_view_bachai(x, y, z, w):
    return float((x + y * math.sqrt(z)) / w)


def Calc_DCT_bac_ba(a, b, c):
    x_1, x_2 = Solve_ptbh(3 * a, 2 * b, c)
    return (
     x_1, x_2)


def Calc_CT_bac_ba(a, b, c, d):

    def ham_f(x):
        y = a * x * x * x + b * x * x + c * x + d
        return y

    Delta = b * b - 3 * a * c
    x1 = (-1 * sign(a) * b - math.sqrt(Delta)) / 3 / sign(a) / a
    x2 = (-1 * sign(a) * b + math.sqrt(Delta)) / 3 / sign(a) / a
    y1 = ham_f(x1)
    y2 = ham_f(x2)
    xi = -b / 3 / a
    yi = ham_f(xi)
    x_1, x_2 = Solve_ptbh(3 * a, 2 * b, c)
    if 'sqrt' in x_1:
        u = (6 * a * c - 2 * b ** 2) / 9 / a
        v = (9 * a * d - b * c) / 9 / a
        A1, A2 = get_tu_mau_phanso(yi)
        u1, u2 = get_tu_mau_phanso(u)
        d1, d2 = get_tu_mau_phanso(Delta)
        a1, a2 = get_tu_mau_phanso(a)
        B1, D, B2 = get_sqrt_nor((u1 * a2) ** 2 * d1 * d2, u2 * 3 * a1 * d2)
        W = int(A2 * B2 / math.gcd(A2, B2))
        X = int(A1 * W / A2)
        Y = int(B1 * W / B2)
        if a > 0:
            y_1 = ptbh_view(X, Y, D, W)
            y_2 = ptbh_view(X, -Y, D, W)
        else:
            y_1 = ptbh_view(X, -Y, D, W)
            y_2 = ptbh_view(X, Y, D, W)
    else:
        y_1 = get_frac(y1)
        y_2 = get_frac(y2)
    return (
     x_1, x_2, y_1, y_2)


def Calc_CT_hai_mot(a, b, c, m, n):

    def ham_f(x):
        y = (a * x * x + b * x + c) / (m * x + n)
        return y

    A = a * m
    B = a * n
    C = b * n - c * m
    Delta = B ** 2 - A * C
    x1 = (-1 * sign(A) * B - math.sqrt(Delta)) / sign(A) / A
    x2 = (-1 * sign(A) * B + math.sqrt(Delta)) / sign(A) / A
    y1 = ham_f(x1)
    y2 = ham_f(x2)
    x_1, x_2 = Solve_ptbh(a * m, 2 * a * n, b * n - c * m)
    if 'sqrt' in x_1:
        A1, A2 = get_tu_mau_phanso((-2 * a * n + b * m) / m ** 2)
        B1, D, B2 = get_sqrt_nor(4 * a ** 2 * Delta, a * m * m)
        W = int(A2 * B2 / math.gcd(A2, B2))
        X = int(A1 * W / A2)
        Y = int(B1 * W / B2)
        if a * m > 0:
            y_1 = ptbh_view(X, -Y, D, W)
            y_2 = ptbh_view(X, Y, D, W)
        else:
            y_1 = ptbh_view(X, Y, D, W)
            y_2 = ptbh_view(X, -Y, D, W)
    else:
        y_1 = get_frac(y1)
        y_2 = get_frac(y2)
    return (
     x_1, x_2, y_1, y_2)