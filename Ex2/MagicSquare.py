def sumRow(m, i):
    return sum(m[i])

def sumCol(m, j):
    return sum(m[i][j] for i in range(0, len(m)))

def sumdiag(m):
    lsum = 0
    rsum = 0
    n = len(m)

    for i in range(0, len(m)):
        lsum += m[i][i]
        rsum += m[i][n - i - 1]
    return lsum, rsum

def isMagicSquare(m):
    lsum, msum = sumdiag(m)

    if (lsum != msum):
        return False

    for i in range(1, len(m)):
        if (sumRow(m, 0) != sumRow(m, i)):
            return False
        
        if (sumCol(m, 0) != sumCol(m, i)):
            return False
    
    if sumRow(m, 0) != sumCol(m, 0) or sumRow(m, 0) != lsum:
        return False
    
    return True
def inputMatrix():
    m = []
    
    while True:
        s = input()

        if s:
            row = [int(e) for e in s.split('\t')]
            m.append(row)
        else:
            break
    
    return m