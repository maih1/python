
#Hoàn thiện hàm addNum(a, b) theo yêu cầu trong đề bài
def strNum(a):
    sa = ''
    for i in a:
        sa += str(i)
    
    return sa

def intNum(a):
    return int(strNum(a))

def addNum(a, b):
    sums = intNum(a) + intNum(b) #2034
    c = []
    
    while (sums > 0): 
        x = sums % 10
        c.append(x)
        sums = sums // 10
    
    c.reverse()
    
    return c

# a = [1, 2, 4, 5]
# b = [7, 8, 9]

# print(addNum(a, b), type(addNum(a, b)))


# cach 2

# def addNum(a):
#     sum = 0
#     a.reverse()
    
#     for i in range(0, len(a)):
#         temp = a[i] * pow(10, i)
#         sum += temp
    
#     return sum

# def sum(a, b):
#     a1 = addNum(a)
#     b1 = addNum(b)
    
#     return a1 + b1

# print(sum(a, b))