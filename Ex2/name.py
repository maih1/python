# -*- coding: utf-8 -*-
import locale

locale.setlocale(locale.LC_ALL, 'vi_VN')

def inputList():
    names = []
    
    while ('' not in names):
        names.append(input())

    del names[len(names) - 1]

    return names
    
def getName(s):
    
    lname =  ''
    fname = ''

    tokens = s.split(' ')

    if len(tokens) > 0:
        fname = tokens[len(tokens) - 1]
        lname = ' '.join([tokens[i] for i in range(0, len(tokens) - 1)])

    return (lname, fname)

def keyName (names):
    lname, fname = getName(names)
    return locale.strxfrm(fname), locale.strxfrm(lname)

def sortNamesList(names):
    namesSorted = sorted(names, key = keyName)
    return namesSorted