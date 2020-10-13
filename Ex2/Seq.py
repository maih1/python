import math

def isAlt(a):
    for index in (0, len(a) - 2):
        if(a[index] == 0):
            return False
        else:
            if (a[index] * a[index + 1] < 0):
                continue
            else:
                return False
    
    return True


def isGrow(a):
    for index in range(0, len(a) - 2):
        if (a[index] > a[index + 1]):
            return False
    
    return True


def isMulti(a):
    for index in range(0, len(a) - 2):
        if (a[index + 2] / a[index + 1] == a[index + 1] / a[index]):
            return True
    
    return False


def isAdd(a):
    for index in range(0, len(a) - 2):
        if (a[index + 2] - a[index + 1] == a[index + 1] - a[index]):
            return True
    
    return False

list = []
n = int(input())    #input length list

for index in range(0, n):
    list.append(int(input()))   #input value index list

print(isAlt(list))
print(isGrow(list))
print(isMulti(list))
print(isAdd(list))
