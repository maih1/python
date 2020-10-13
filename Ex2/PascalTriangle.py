def calculation (n, k):
    if (k == 0) or (k == n):
        return 1
    elif (k == 1):
        return n
    else:
        return (calculation(n - 1, k - 1) + calculation(n - 1, k))

def pascal(m):
    for i in range(0, m + 1):
        for j in range(0, i + 1):
            pascal = calculation(i, j)
            print(pascal, end = ' ')
        print()

m = int(input())
pascal(m)