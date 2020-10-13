import math

number1 = float(input())
number2 = float(input())
number3 = float(input())

def isTriangle(a, b, c):
    if(abs(b - c) < a < (b + c)):
        return True
    return False

def perimeterAcreage(a, b, c):
    if(isTriangle(a, b, c) == False):
        print('INVALID')
    else:
        cv = a + b + c
        p = 1/2 * cv
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('S = ', s, 'C = ', cv)

perimeterAcreage(number1, number2, number3)