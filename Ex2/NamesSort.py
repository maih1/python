# -*- coding: utf-8 -*-
import locale

locale.setlocale(locale.LC_ALL, 'vi_VN')

def inputList():
    names = []
    
    while ('' not in names):
        names.append(input())

    del names[len(names) - 1]

    return names
    
    # while True:
    #     name = input().strip()
    #     if not name:

    #     names.append(name)
    # return names

def getName(s):
    temp = s.split(' ')

    fname = temp[len(temp) - 1]

    lname = ''
    count = 0
    for i in range(0, len(temp)):
        if count > 0:
            if count > 1:
                lname += ' '
            lname += temp[i]
        
        count += 1

    # lname =  ''
    # fname = ''

    # tokens = s.split(' ')

    # if len(tokens) > 0:
    #     fname = tokens[len(tokens) - 1]
    #     lname = ' '.join([tokens[i] for i in range(0, len(tokens) - 1)])

    # return (lname, fname)

def compare (name):
    lname, fname = getName(names)
    return locale.strxfrm(fname), locale.strxfrm(lname)

def sortNamesList(names):
    namesSorted = sorted(names, key = compare)
    return namesSorted

names = inputList()
sort = sortNamesList(names)

for i in sort:
    print(i)