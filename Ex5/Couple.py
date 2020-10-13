def opFile(filename):
    file = open(filename, encoding='utf-8')
    data = file.read().rstrip().split()
    file.close()

    return data

def reverse(s):
    return s[::-1]

def checkCouple(data):
    tupleCouple = tuple()
    listCouple = list(tupleCouple)

    for i in range(0, len(data) - 1):
        check = reverse(data[i])
        for j in range(i + 1, len(data)):
            if ((data[i] != data[j]) and (check == data[j])):
                listCouple.append(data[i])
                listCouple.append(data[j])
    
    listCouple.sort()

    tupleCouple = tuple(listCouple)

    return tupleCouple

def findCouple(filename):
    data = opFile(filename)
    tupleCouple = checkCouple(data)

    return tupleCouple

filename = './Ex5/text/w.txt'
# data = opFile(filename)
print(findCouple(filename))