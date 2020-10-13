import math

def uv (u, v):
    sumUV = 0
    
    for i in range(0, len(u)):
        sumUV += u[i] * v[i]
    
    return sumUV

def length(u):
    length = 0

    for i in u:
        length += i * i
    
    return math.sqrt(pow(length, 2))

def cosineb2v(u, v):

    return uv(u, v) / (length(u) * length(v))

# u = (1, 2)
# v = (3, 4)

# print(uv(u, v))
# print(cosineb2v(v, v))
