import math

n = int(input())

# def sort(a, b, c):

def isPytago(n):
    if (n < 3):
        return False
    
    for i in range(1, n - 1):
        for j in range(i, n):
            a = i*i + j*j
            for k in range(j + 1, n + 1):
                if(a == k*k):
                    print("(", i, ", ", j, ", ", k, ")", sep='')

isPytago(n)
