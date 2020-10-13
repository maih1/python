s = input()

list = []

for i in range(0, len(s) - 1):
    if (s.count(s[i]) != s.count(s[i + 1])):
        list.append(s.count(s[i]))

def isMax(s):
    counts = 0

    S = ''
    C = 0

    for i in range(0, len(s) - 1):
        if(max(list) == s.count(s[i]) and s.count(s[i]) != s.count(s[i + 1])):
            # print(s[i], max(list))
            counts += 1
            S = s[i]
            C = max(list)

    if (counts != 0):
        print(S, C)

isMax(s)