# coding=utf-8
# def_utilities.py
import re, os, sys, csv, codecs, time, math, argparse, subprocess, signal, shutil, errno, unicodedata
from fractions import Fraction
from decimal import Decimal

def openfile(path):
    try:
        if hasattr(os, 'startfile'):
            os.startfile(path)
        else:
            path=path.replace('\\','/')
            if sys.platform == 'linux':
                subprocess.call(['xdg-open', path])
            elif sys.platform == 'darwin':
                subprocess.call(['open', path])
    except Exception as er:
        return 'Error'
        
def PdfLaTeX(path, filename, block):
    path_0 = os.getcwd()
    if hasattr(os, 'startfile'):
        cwd = os.getcwd() + '\\'+path+'\\'
    else:
        cwd = os.getcwd() + '/'+path+'/'
    os.chdir(cwd)
    if hasattr(os, 'startfile'):
        path_1 = os.getcwd() + '\\' + path + '\\'
    else:
        path_1 = os.getcwd() + '/' + path + '/'
    with codecs.open(filename + '.tex', 'w', 'utf-8') as (f):
        f.write(block)
    try:
        cmd = [
         'pdflatex', '-interaction', 'nonstopmode', filename + '.tex']
        proc = subprocess.Popen(cmd)
        proc.communicate()
        retcode = proc.returncode
        if not retcode == 0:
            os.unlink(filename + '.pdf')
        raise ValueError(('Error {} executing command: {}').format(retcode, (' ').join(cmd)))
    except Exception as err:
        i = 0

    os.unlink(filename + '.log')
    os.unlink(filename + '.aux')
    try:
        shutil.copy2(cwd + filename + '.pdf', path_1 + filename + '.pdf')
    except Exception as err:
        i = 0

    os.chdir(path_0)


def List_creat(s):
    s = s.replace('', '')
    l = s.split(',')
    return l


def Time_convert(t):
    hour, p = divmod(t, 3600)
    minute, second = divmod(p, 30)
    return (
     hour, minute, second)


def strip_accents(string, accents=('COMBINING ACUTE ACCENT', 'COMBINING GRAVE ACCENT', 'COMBINING TILDE')):
    string = string.replace('Đ', 'D')
    string = string.replace('đ', 'd')
    string = string.replace(' ', '')
    accents = set(map(unicodedata.lookup, accents))
    chars = [c for c in unicodedata.normalize('NFD', string) if c not in accents]
    filename = unicodedata.normalize('NFC', ('').join(chars))
    filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore')
    return filename