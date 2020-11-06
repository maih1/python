t = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2]
ct = [0, 5, 1, 1, 0, 5, 2, 1]

def length(t):
    if len(t) > 0:
        count = 2

        for i in range(len(t) - 1):
            if t[i] != t[i + 1]:
                count += 2
        
        return count
    else:
        return 0

# print(length(t))
    
def compress(t):
    ct = []
    
    return ct

print(compress(t))

def lengthInverse(ct):
    length = 0

    for i in range(len(ct)):
        if i % 2 != 0:
            length += ct[i]
    return length
    
def decompress(ct):
    result = []

    for i in range(0, len(ct)):
        if i % 2 != 0:
            for j in range(ct[i]):
                result.append(ct[i - 1])
    
    return result
ct = [0, 5, 1, 1, 0, 5]
# print(lengthInverse(ct))
# print(decompress(ct))