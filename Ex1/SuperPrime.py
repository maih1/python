import math

number = int(input())

def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i) == 0:
            return False
    
    return True

def isPrimeSuper(n):
    if(isPrime(n) == False):
        return False
    else:
        while n > 0:
            if(isPrime(n) == False):
                return False
            else:
                n = n // 10
            print(n)
    
    return True
    
print(isPrime(number))
print(isPrimeSuper(number))

