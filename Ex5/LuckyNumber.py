import math

def opFile(filename):
    file = open(filename, encoding='utf-8')
    dataNumber = []

    for i in file:
        listData = i.rstrip().split(' ')
        for j in listData:
            if (j.isdigit()):
                dataNumber.append(int(j))
    file.close()
    return dataNumber

def isPrime(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i == 0):
            return False
    
    return True

def sumNumber(number):
    sums = 0
    
    while (number > 0):
        num1 = number % 10
        sums += num1
        number = number // 10
    
    return sums

def luckyNumber(dataNumber):
    luckyNumber = []
    for number in dataNumber:
        if (isPrime(number) == True):
            temp = sumNumber(number)
            if (temp % 5 == 0):
                luckyNumber = number

    return luckyNumber

def findLuckyNumber(filename):
    dataNumber = opFile(filename)
    return luckyNumber(dataNumber)

filename = './Ex5/text/test4.txt'
print(findLuckyNumber(filename))