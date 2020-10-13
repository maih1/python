import os

def keyName(tuples):
    kn = tuples[0]
    # print(keyName)
    return kn

def sorts(lists):
    sortNameFile = sorted(lists, key=keyName)
    return sortNameFile

def searchInFiles(x, path):
    listPath = os.listdir(path)
    lists = []
    
    string = ''
    
    for i in listPath:
        pathFile = path + '/' + i
        file = open(pathFile, encoding='utf-8')
        tuples = tuple()
        tempList = list(tuples)
        
        tempList.append(pathFile)

        for j in file:
            if ((x in j) == True):
                tempList.append(j)

            if(len(tempList) == 2):

                tuples = tuple(tempList)
        
                lists.append(tuples)
                file.close()
                break

    return sorts(lists)

path = './Ex5/text'
x = "danh sách"

print(searchInFiles(x, path))   