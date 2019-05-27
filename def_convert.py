# coding=utf-8
# def_convert.py
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

def Conv_que2ex_de(filename):
    block_cau = codecs.open(filename, 'r', 'utf-8').read()
    block_cau = Conv_chuanhoa(block_cau)
    block_cau = re.sub('\\s*\\{\\\\dung\\{(.*?)\\}\\}\\s*\\n', '\\r\\n{\\\\True \\1}', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\{\\\\sai\\{(.*?)\\}\\}\\s*\\n', '\\r\\n{\\1}', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\{question\\}', '{ex}', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\datcot\\[4\\]\\\\bonpa', '\\n\\\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\datcot\\[2\\]\\\\bonpa', '\\n\\\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\datcot\\\\bonpa', '\\n\\\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\begin{sol}A\\\\end{sol}', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\begin{sol}B\\\\end{sol}', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\begin{sol}C\\\\end{sol}', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\begin{sol}D\\\\end{sol}', '', block_cau, re.DOTALL)
    return block_cau


def Conv_que2ex(filename):
    block_cau = codecs.open(filename, 'r', 'utf-8').read()
    block_cau = Conv_chuanhoa(block_cau)
    block_cau = re.sub('\\{\\\\dung\\{(.*?)\\}\\}\\s*\\n', '\\r\\n{\\\\True \\1}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\{\\\\sai\\{(.*?)\\}\\}\\s*\\n', '\\r\\n{\\1}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\{\\\\dung\\{(.*?)\\}\\s*\\}\\s*\\n', '\\r\\n{\\\\True \\1}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\{\\\\sai\\{(.*?)\\}\\s*\\}\\s*\\n', '\\r\\n{\\1}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\{question\\}', '{ex}', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\datcot\\[4\\]\\\\bonpa', '\\n\\\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\datcot\\[2\\]\\\\bonpa', '\\n\\\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\datcot\\\\bonpa', '\\n\\\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\begin{sol}A\\\\end{sol}', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\begin{sol}B\\\\end{sol}', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\begin{sol}C\\\\end{sol}', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\begin{sol}D\\\\end{sol}', '', block_cau, re.DOTALL)
    return block_cau


def Conv_dethi2ex_cau(ID_de):
    block = '\\begin{ex}%[' + ID_de[1][2:-1] + ']%[' + ID_de[0].replace('maID', '') + ']\n' + ID_de[2][0:-1] + '\n\\choice\n'
    dungA = '{'
    dungB = '{'
    dungC = '{'
    dungD = '{'
    if ID_de[3] == '1':
        dungA = '{\\True '
    else:
        if ID_de[3] == '2':
            dungB = '{\\True '
        else:
            if ID_de[3] == '3':
                dungC = '{\\True '
            else:
                if ID_de[3] == '4':
                    dungD = '{\\True '
    pa_A = dungA + ID_de[4] + '}'
    pa_B = dungB + ID_de[5] + '}'
    pa_C = dungC + ID_de[6] + '}'
    pa_D = dungD + ID_de[7] + '}'
    block += pa_A + '\n' + pa_B + '\n' + pa_C + '\n' + pa_D + '\n' + '\\loigiai{\n' + ID_de[9] + '\n}\n\\end{ex}\n'
    return block


def Conv_dethi2ex(filename):
    block_cau = codecs.open(filename, 'r', 'utf-8').read()
    de_full = re.findall('baitracnghiem\\{(.*?)\\}\\{(.*?)\n(.*?)\n\\}\\{\\\\bonpa\\{(.*?)\\}\\s*\\{(.*?)\\}\\s*\\{(.*?)\\}\\s*\\{(.*?)\\}\\s*\\{(.*?)\\}\\s*}{(.*?)\r\n(.*?)\r\n}', block_cau, re.DOTALL)
    block = ''
    for cauhoi in de_full:
        block += Conv_dethi2ex_cau(cauhoi)

    return block


def Conv_chuanhoa(block):
    block = re.sub('  ', ' ', block)
    block = re.sub('\\t', '', block)
    block = re.sub('\\r', '\\r\\n', block, re.DOTALL)
    block = re.sub('\\n', '\\r\\n', block, re.DOTALL)
    block = re.sub('\\s*\\r\\n}', '}', block, re.DOTALL)
    block = re.sub('\\s*\\r\\n}}', '}}', block, re.DOTALL)
    return block


def Conv_ex2ques_get_cau(filename):
    block_cau = codecs.open(filename, 'r', 'utf-8').read()
    block = ''
    de_full = re.findall('\\\\begin{ex}(.*?)\\r\\n(.*?)\\\\loigiai(.*?)\\\\end{ex}', block_cau, re.DOTALL)
    for block_cau in de_full:
        block += Conv_ex2ques_cau(block_cau)

    return block


def Conv_ex2ques_cau(block_cau):
    block = '\\begin{question}' + block_cau[0]
    chuan_hoa = Conv_chuan_pa(block_cau[1])
    block += re.sub('\\s*\\\\choice\\s*{(.*?)}\\s*{(.*?)}\\s*{(.*?)}\\s*{(.*?)}\\s*', '\\n\\\\datcot\\\\bonpa\\r{\\\\sai{\\1}}\\r{\\\\sai{\\2}}\\r{\\\\sai{\\3}}\\r{\\\\sai{\\4}}\\r', chuan_hoa, re.DOTALL)
    block += '\\loigiai' + block_cau[2] + '\\end{question}\n'
    block = block.replace('{\\sai{\\True ', '{\\dung{')
    block = block.replace('{\\sai{\\True', '{\\dung{')
    block = block.replace('\\\\loigiai{', '\\loigiai{\r\n')
    block = block.replace('\\\\loigiai{\\r\\n\\r\\n', '\\loigiai{\r\n')
    block = block.replace('\\r\\n\\\\choice', '\\choice')
    return block


def Conv_ques2ex_get_cau(filename):
    block_cau = codecs.open(filename, 'r', 'utf-8').read()
    block_cau = re.sub('\\s*\\\\begin{sol}(.*?)\\\\end{sol}', '', block_cau, re.DOTALL)
    block_cau = re.sub('}\\r\\n\\\\end{question}', '\\r\\n}\\r\\n\\\\end{question}', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\\r\\n}\\r\\n\\\\end{question}', '\\r\\n}\\r\\n\\\\end{question}', block_cau, re.DOTALL)
    block_cau = re.sub('%01}{', '', block_cau, re.DOTALL)
    block = ''
    de_full = re.findall('\\\\begin{question}(.*?)\\r\\n(.*?)\\\\loigiai(.*?)\\\\end{question}', block_cau, re.DOTALL)
    for block_cau in de_full:
        block += Conv_ques2ex_cau(block_cau)

    block = block.replace('\\r}\\r\\n\\\\loigiai{', '}\r\n\\loigiai{\r\n')
    block = block.replace('\\r}\\r\\n\\\\loigiai{', '}\r\n\\loigiai{\r\n')
    return block


def Conv_ques2ex_cau(block_cau):
    block = '\\begin{ex}' + block_cau[0]
    block += re.sub('\\s*\\\\bonpa\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*', '\\n\\\\choice\\r\\1\\r\\2\\r\\3\\r\\4\\r', block_cau[1], re.DOTALL)
    block += '\\loigiai' + block_cau[2] + '\\end{ex}\n'
    block = block.replace('\\sai{', '{')
    block = block.replace('\\dung{', '{\\True ')
    block = block.replace('\\\\loigiai{', '\\loigiai{\r\n')
    block = block.replace('\\r}\\r\\n\\\\loigiai{', '}\r\n\\loigiai{\r\n')
    block = block.replace('\\r}\\r\\n\\\\loigiai{', '}\r\n\\loigiai{\r\n')
    block = block.replace('\\\\loigiai{\\r\\n\\r\\n', '\\loigiai{\r\n')
    block = re.sub('\\\\datcot\\[[2-4]\\]', '', block, re.DOTALL)
    block = re.sub('\\\\datcot', '', block, re.DOTALL)
    block = re.sub('\\s*\\\\begin{sol}(.*?)\\\\end{sol}', '', block, re.DOTALL)
    block = re.sub('\\r\\n\\{\\{(.*?)\\}\\}\\r\\n', '\\r\\n{\\1}\\r\\n', block, re.DOTALL)
    return block


def Conv_ques2ex_adv(filename):
    block_cau = codecs.open(filename, 'r', 'utf-8').read()
    de_full = re.findall('\\\\begin{question}(.*?)\\r\\n(.*?)\\\\loigiai(.*?)\\\\end{question}', block_cau, re.DOTALL)
    for block_cau in de_full:
        block += Conv_ques2ex_adv_cau(block_cau)

    return de_full


def Conv_ques2ex_adv_cau(block_cau):
    block_cau = block_cau.replace('\\{', '\\ngoactron')
    block = '\\begin{ex}' + block_cau[0].replace('%01}{', '')
    block += re.sub('\\s*\\\\choice\\s*{(.*?)}\\s*{(.*?)}\\s*{(.*?)}\\s*{(.*?)}\\s*', '\\n\\\\datcot\\\\bonpa\\r{\\\\sai{\\1}}\\r{\\\\sai{\\2}}\\r{\\\\sai{\\3}}\\r{\\\\sai{\\4}}\\r', block_cau[1], re.DOTALL)
    block += '\\loigiai' + block_cau[2] + '\\end{ex}\n'
    block = block.replace('\\ngoactron', '\\{')
    return block


def Conv_Chuanfile_ques(filename):
    block_cau = codecs.open(filename, 'r', 'utf-8').read()
    block_cau = re.sub('\\r\\n\\}', '}', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\}', '}', block_cau, re.DOTALL)
    block_cau = re.sub('\\n\\}', '}', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\\\begin{sol}(.*?)\\\\end{sol}', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\%01\\}\\{', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\\\begin{ex}', '\\\\begin{ex}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\\\begin{ex}\\r\\n\\r\\n', '\\\\begin{ex}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\\\begin{ex}\\r\\n\\r\\n', '\\\\begin{ex}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('   ', ' ', block_cau, re.DOTALL)
    block_cau = re.sub('   ', ' ', block_cau, re.DOTALL)
    block_cau = re.sub('   ', ' ', block_cau, re.DOTALL)
    block_cau = re.sub('   ', ' ', block_cau, re.DOTALL)
    block_cau = re.sub('\\t', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\t', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\t', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\t', '', block_cau, re.DOTALL)
    block_cau = re.sub('\t', '', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\t', '\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\t', '\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\t', '\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\\t', '\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\\t', '\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\\t', '\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\\t', '\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\\t', '\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('  }}\\r\\n', '}}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub(' }}\\r\\n', '}}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\.}}\\r\\n', '}}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('\\. }}\\r\\n', '}}\\r\\n', block_cau, re.DOTALL)
    block_cau = re.sub('}\\r\\n\\\\end{question}', '\\r\\n}\\r\\n\\\\end{question}', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\\r\\n}\\r\\n\\\\end{question}', '\\r\\n}\\r\\n\\\\end{question}', block_cau, re.DOTALL)
    block_cau = re.sub('}\\r\\n\\\\end{ex}', '\\r\\n}\\r\\n\\\\end{ex}', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\\r\\n}\\r\\n\\\\end{ex}', '\\r\\n}\\r\\n\\\\end{ex}', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\n\\r\\n\\\\choice', '\r\n\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\r\\r\\\\choice', '\r\n\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\n\\n\\\\choice', '\r\n\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\n\\\\choice', '\r\n\\choice', block_cau, re.DOTALL)
    block_cau = re.sub('\\s*\\n\\\\bonpa', '\r\n\\choice', block_cau, re.DOTALL)
    with codecs.open(filename, 'w', 'utf-8') as (f):
        f.write(block_cau)
        f.close()


def Conv_Auto_True(filename):
    block_cau = codecs.open(filename, 'r', 'utf-8').read()
    block_cau.replace('\\n', '\\r\\n')
    block = ''
    de_full = re.findall('\\\\begin{ex}(.*?)\\r\\n(.*?)\\\\loigiai\\{(.*?)\\}\\r\\n\\\\end{ex}', block_cau, re.DOTALL)
    for block_cau in de_full:
        block += Conv_Auto_True_Block(block_cau)

    return block


def Conv_Auto_True_Block(block_cau):
    block = '\\begin{ex}' + block_cau[0] + '\n'
    Chon_True = ['Chọn ', 'Chọn phương án', 'Chọn đáp án']
    for Chon in Chon_True:
        if Chon in block_cau[2]:
            if Chon + 'A' in block_cau[2]:
                block += re.sub('\\s*\\\\choice\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*', '\\n\\\\choice\\r\\n{\\\\True \\1}\\r\\n{\\2}\\r\\n{\\3}\\r\\n{\\4}\\r\\n', block_cau[1], re.DOTALL)
                block += '\\loigiai{' + re.sub(Chon + 'A.' + '(.*?)\\r\\n', '', block_cau[2], re.DOTALL) + '\r\n}\r\n\\end{ex}\n'
            elif Chon + 'B' in block_cau[2]:
                block += re.sub('\\s*\\\\choice\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*', '\\n\\\\choice\\r\\n{\\1}\\r\\n{\\\\True \\2}\\r\\n{\\3}\\r\\n{\\4}\\r\\n', block_cau[1], re.DOTALL)
                block += '\\loigiai{' + re.sub(Chon + 'B.' + '(.*?)\\r\\n', '', block_cau[2], re.DOTALL) + '\r\n}\r\n\\end{ex}\n'
            elif Chon + 'C' in block_cau[2]:
                block += re.sub('\\s*\\\\choice\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*', '\\n\\\\choice\\r\\n{\\1}\\r\\n{\\2}\\r\\n{\\\\True \\3}\\r\\n{\\4}\\r\\n', block_cau[1], re.DOTALL)
                block += '\\loigiai{' + re.sub(Chon + 'C.' + '(.*?)\\r\\n', '', block_cau[2], re.DOTALL) + '\r\n}\r\n\\end{ex}\n'
            elif Chon + 'D' in block_cau[2]:
                block += re.sub('\\s*\\\\choice\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*\\{(.*?)\\}\\s*\\r\\n\\s*', '\\n\\\\choice\\r\\n{\\1}\\r\\n{\\2}\\r\\n{\\3}\\r\\n{\\\\True \\4}\\r\\n', block_cau[1], re.DOTALL)
                block += '\\loigiai{' + re.sub(Chon + 'D.' + '(.*?)\\r\\n', '', block_cau[2], re.DOTALL) + '\r\n}\r\n\\end{ex}\n'
            else:
                block += block_cau[1]

    return block.replace('\r\n\r\n}', '\r\n}')


def Conv_Chuanfile_ex(filename):
    block_cau = codecs.open(filename, 'r', 'utf-8').read()
    L = []
    de_full = re.findall('\\\\begin{ex}(.*?)\\r\\n(.*?)\\\\end{ex}', block_cau, re.DOTALL)
    for block_cau in de_full:
        if '\\loigiai' in block_cau[1]:
            de_giai = re.findall('(.*?)\\r\\n\\\\loigiai\\{(.*?)\\}', block_cau[1], re.DOTALL)
            if de_giai != '[]':
                L.append((block_cau[0], de_giai[0][0], de_giai[0][1]))
            else:
                L.append((block_cau[0], block_cau[1], ''))

    block = ''
    for cau in L:
        block += '\\begin{ex}' + cau[0] + '\n'
        block += Conv_chuan_pa(block_cau[1])
        block += '\\loigiai{\r\n' + cau[2].strip() + '\r\n}\r\n\\end{ex}\n'

    return block


def Conv_chuan_pa(block_cau):
    block_cau = block_cau.replace('\\{', '\\ngoacmo')
    block_cau = block_cau.replace('\\}', '\\ngoacdong')
    s = block_cau.index('\\choice')
    block = block_cau[:s + 7]
    i = 0
    j = 1
    pa_A = ''
    pa_B = ''
    pa_C = ''
    pa_D = ''
    k = 0
    for text in block_cau[s + 7:]:
        k += 1
        if text == '{':
            i += 1
        if text == '}':
            i = i - 1
            if i == 0:
                j += 1
        if i >= 1:
            if j == 1:
                pa_A += text
        if i >= 1:
            if j == 2:
                pa_B += text
        if i >= 1:
            if j == 3:
                pa_C += text
        if i >= 1 and j == 4:
            pa_D += text
            l = k

    block += '\r\n{' + pa_A[1:] + '}\r\n{' + pa_B[1:] + '}\r\n{' + pa_C[1:] + '}\r\n{' + pa_D[1:] + '}\r\n'
    block += block_cau[s + 7 + l + 1:]
    block = block.replace('\\ngoacmo', '\\{')
    block = block.replace('\\ngoacdong', '\\}')
    block = re.sub('\\r\\n\\s*\\r\\n', '\r\n', block)
    return block


def Conv_GetCau_fromBlock(block):
    PA_chuan=[]
    Cau=re.findall(r"(.*?)\s*\\choice\n\s*{(.*?)}\n\s*{(.*?)}\n\s*{(.*?)}\n\s*{(.*?)}\n\s*(.*?)\n\\end{ex}",block,re.DOTALL)
    if '\\True' in Cau[0][1]:
        true = 1
    else:
        if '\\True' in Cau[0][2]:
            true = 2
        else:
            if '\\True' in Cau[0][3]:
                true = 3
            else:
                if '\\True' in Cau[0][4]:
                    true = 4
                else:
                    true = 0
    PA_chuan.append(Cau[0][0])
    PA_chuan.append([true, Cau[0][1], Cau[0][2], Cau[0][3], Cau[0][4]])
    PA_chuan.append(Cau[0][5] + '\n\\end{ex}\n')
    return PA_chuan


def Conv_Form_to_EX(Cau):
    block = Cau[0] + '\n\\choice\n{' + Cau[1][1] + '}\n{' + Cau[1][2] + '}\n{' + Cau[1][3] + '}\n{' + Cau[1][4] + '}\n' + Cau[2]
    return block


def Conv_GetListEX_FromFile(filename):
    List = []
    if 1 == 1:
        data = codecs.open(filename, 'r', 'utf-8')
        Found = False
        block = ''
        for line in data:
            if Found:
                block += line
                if 'end{ex}' in line:
                    Found = False
                    List.append(block)
                    block = ''
                else:
                    if 'begin{ex}' in line:
                        Found = True
                        block += line

    return List