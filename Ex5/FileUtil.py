
def sort(data):
    listData = data.split(' ')
    listDataNumber = []
    check = 0

    for i in listData:
        listDataNumber.append(int(i))

    for k in listDataNumber:
        for i in range(0, len(listDataNumber) - 1):
            if (listDataNumber[i] == 0 and listDataNumber[i + 1] != 0):
                temp = listDataNumber[i + 1]
                listDataNumber[i + 1] = listDataNumber[i]
                listDataNumber[i] = temp
        
    return listDataNumber


def zeroMove(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return sort(data)

fileName = './Ex5/text/test3.txt'
print(zeroMove(fileName))

# 0 1 0 3 12 0 0 1
# 1 0 3 12 0 0 1 0 

# 1 0 0 3 12
# 1 0 3 0 12
# 1 0 3 12 0