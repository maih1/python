import math

def mean(s): #tb
    sum = 0

    for i in s:
        sum += i

    return sum / len(s)

def variance(s): #phuong sai
    xicma = 0
    tb = mean(s)
    for i in s:
        xicma += (i - tb) * (i - tb)
    
    return (1/len(s)) * xicma

def standarddeviation(s):
    return math.sqrt(variance(s))
