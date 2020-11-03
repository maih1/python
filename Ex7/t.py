def com (x):
    return x[1], x[0]

t = [('a', 20), ('s', 4), ('s', 3), ('e', 3), ('a', 20)]
sets = set(t)
m = list(sets)
m.sort(key=com, reverse=True)
# print(sets)
print(m)