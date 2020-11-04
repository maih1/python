import math

def sparseForm(t):
    tspr = []
    dc = dict()

    for i in range(len(t)):
        if t[i] != 0:
            dc.update({i : t[i]})
    
    tspr.append(len(t))
    tspr.append(dc)

    spr = tuple(tspr)

    return spr
    
def revert(spr):
    tspr = []
    for i in range(spr[0]):
        if i in spr[1]:
            tspr.append(spr[1][i])
        else:
            tspr.append(0)
    
    return tspr

def dot(spr1, spr2):
    u = revert(spr1)
    v = revert(spr2)

    tvh = 0

    for i in range(spr1[0]):
        tvh += u[i] * v[i]

    return tvh

def sqrt(spr1):
    u = revert(spr1)

    sqrt = 0

    for i in range(spr1[0]):
        sqrt += pow(u[i], 2)

    return math.sqrt(sqrt)

def getCosinSim(spr1, spr2):

    return dot(spr1, spr2) / (sqrt(spr1) * sqrt(spr2))

t = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 9, 0, 0, 8, 0, 0, 6, 0, 0, 7, 5, 1, 0, 0, 2, 8, 0 ,0, 0, 0, 0 ,5, 1]
print(t)
print(sparseForm(t))
a = sparseForm(t)
print(revert(a))
s1 = [0, 1, 3, 0, 4]
s2 = [1, 0, 4, 4, 0]
sp1 = sparseForm(s1)
sp2 = sparseForm(s2)
print(dot(sp1, sp2))
print(getCosinSim(sp1, sp2))
