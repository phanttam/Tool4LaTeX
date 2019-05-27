# coding=utf-8
# def_mix.py
import re, os, sys, csv, codecs, time
from datetime import datetime, timedelta
from urllib.request import urlopen
import math, argparse, subprocess, signal, shutil, errno, unicodedata, webbrowser
from random import *
from fractions import Fraction
from decimal import Decimal
from def_calculation import *
from def_utilities import *
from src_reg import *
from def_bbt import *
from def_id import *
from def_convert import *
from def_ban_quyen import *
from def_matrix import *
from def_convert import *

def Random_Mix_ListEX(List, So_cau, So_de, option):
    List_new = []
    List_de = []
    if option[1] == 0:
        for i in range(0, So_de):
            index = sample((range(0, len(List))), k=So_cau)
            for j in index:
                List_new.append(List[j])

            List_de.append(List_new)
            List_new = []

    if option[1] == 1:
        for i in range(0, So_de):
            for j in range(0, So_cau):
                List_new.append(List[j])

            List_de.append(List_new)
            List_new = []

    return List_de


def Random_List_DA(n, option):
    List = []
    Sum = [
     0, 0, 0, 0]
    if 1 == 1:
        if option[0] == 'B':
            for i in range(0, n):
                List.append('1')

        else:
            if option[0] == 'A':
                for i in range(0, n):
                    a = sample([1, 2, 3, 4], k=1)
                    Sum[(a[0] - 1)] += 1
                    List.append(str(a[0]))

            else:
                if option[0] == 'C':
                    Max = int((n + 3) / 4)
                    PA = [1, 2, 3, 4]
                    for i in range(0, n):
                        a = sample(PA, k=1)
                        Sum[(a[0] - 1)] += 1
                        List.append(str(a[0]))
                        for j in range(1, 5):
                            if Sum[(j - 1)] == Max:
                                Sum[j - 1] = 'Max'
                                index = PA.index(j)
                                PA.pop(index)

                else:
                    if option[0] == 'D':
                        for i in range(0, n):
                            List.append('0')

    return List


def Random_GetListEX_FromFile(filename):
    List = []
    data = codecs.open(filename, 'r', 'utf-8')
    Found = False
    block = ''
    for line in data:
        if 'begin{ex}' in line:
            Found = True
        if Found:
            block += line
        if 'end{ex}' in line:
            Found = False
            List.append(block)
            block = ''
                       
    return List


def Random_Mix_Phuongan(List_pa, num):
    List_pa_new = [
     0, '', '', '', '']
    if int(num) == 0:
        List_pa_new = List_pa
    else:
        List_pa_new = [
         0, '', '', '', '']
        PA_new = [1, 2, 3, 4]
        PA_old = [1, 2, 3, 4]
        PA_old.pop(List_pa[0] - 1)
        List_pa_new[0] = num
        List_pa_new[num] = List_pa[List_pa[0]]
        Mix_sai = sample([List_pa[PA_old[0]], List_pa[PA_old[1]], List_pa[PA_old[2]]], k=3)
        PA_new.pop(num - 1)
        j = 0
        for i in PA_new:
            List_pa_new[i] = Mix_sai[j]
            j += 1

    return List_pa_new


def Random_CreatDe_One_EX(List, option):
    List_new = []
    n = len(List)
    List_DA = Random_List_DA(n, option)
    i = 0
    for element in List:
        Cau = Conv_GetCau_fromBlock(element)
        num = int(List_DA[i])
        List_pa = Cau[1]
        List_pa_new = Random_Mix_Phuongan(List_pa, num)
        i += 1
        Cau[1] = List_pa_new
        block = Conv_Form_to_EX(Cau)
        List_new.append(block)

    return List_new


def Random_Made_Auto(So_de):
    List = []
    
    for i in range(0, So_de):
        a1 = randint(0, 9)
        a2 = randint(0, 9)
        a3 = randint(0, 9)
        Made = str(a1) + str(a2) + str(a3)
        while Made in List:
            a1 = randint(0, 9)
            a2 = randint(0, 9)
            a3 = randint(0, 9)
            Made = str(a1) + str(a2) + str(a3)
        List.append(Made)

    return List


def Random_Made_First(So_de):
    List = []
    
    for i in range(1, So_de + 1):
        a2 = randint(0, 9)
        a3 = randint(0, 9)
        Made = str(1) + str(a2) + str(a3)
        while Made in List:
            if len(str(i)) == 1:
                a2 = randint(0, 9)
                a3 = randint(0, 9)
                Made = str(i) + str(a2) + str(a3)
            elif len(str(i)) == 2:
                a3 = randint(0, 9)
                Made = str(i) + str(a3)
            else:
                Made = str(i)

        List.append(Made)

    return List


def Random_Made_Last(So_de):
    List = []
    
    for i in range(1, So_de + 1):
        a1 = randint(0, 9)
        a2 = randint(0, 9)
        Made = str(a1) + str(a2) + str(1)
        while Made in List:
            if len(str(i)) == 1:
                a2 = randint(0, 9)
                a3 = randint(0, 9)
                Made = str(a2) + str(a3) + str(i)
            elif len(str(i)) == 2:
                a3 = randint(0, 9)
                Made = str(a3) + str(i)
            else:
                Made = str(i)

        List.append(Made)

    return List


def Random_Made_Cont(Made, So_de):
    List = []
    for i in range(0, So_de):
        Made_t = int(Made) + i
        if len(str(Made_t)) == 1:
            Made_n = '00' + str(Made_t)
        else:
            if len(str(Made_t)) == 2:
                Made_n = '0' + str(Made_t)
            else:
                if len(str(Made_t)) == 4:
                    Made_n = str(Made_t)[1:]
                else:
                    Made_n = str(Made_t)
        List.append(Made_n)

    return List


def Random_Made_List(List, n):
    if len(List) >= n:
        List = List[:n]
    else:
        m = n - len(List)
        List_n = Random_Made_Auto(m)
        List += List_n
    return List