import random


# Раздел 4

# Общие функции

def generateList(n: int):
    res = list()
    for i in range(n):
        res.append(random.random())
    return res


def fileReadToWriteWork(readFileName: str = 'infile', writeFileName: str = ''):
    data = list()
    if writeFileName != '':
        f1 = open(writeFileName, 'w')
    inf = open(readFileName, 'r')
    for line in inf:
        if 'f1' in locals():
            f1.write(line.strip() + '\n')
            continue
        data.append(line.strip())
    if 'f1' in locals():
        f1.close()
    inf.close()
    return data


def fileWrite(data: list, filename='outfile.txt', typeWrite: str = 'w'):
    f = open(filename, typeWrite)
    for number in data:
        f.write(str(number) + '\n')
    return data


def checkListForMinMax(data: list):
    min = data[0]
    indMin = 0
    max = data[0]
    indMax = 0
    for ind, val in enumerate(data):
        if val < min:
            min = val
            indMin = ind
        if val > max:
            max = val
            indMax = ind
        continue
    print('Min val: ' + str(min) + ' Ind: ' + str(indMin))
    print('Max val: ' + str(max) + ' Ind: ' + str(indMax))
    data[indMin], data[indMax] = data[indMax], data[indMin]
    return data


def directSort(data: list, i: int = 0):
    while i < len(data) - 1:
        m = i
        j = i + 1
        while j < len(data):
            if data[j] < data[m]:
                m = j
            j += 1
        data[i], data[m] = data[m], data[i]
        i += 1
    return data


def includeSort(data: list, i: int = 1):
    for ind, val in enumerate(data):
        tempVal = data[i]
        tempInd = i
        while (tempInd > 0) and (data[tempInd - 1] > tempVal):
            data[tempInd] = data[tempInd - 1]
            tempInd -= 1
        data[tempInd] = tempVal
    i += 1
    return data


# 4.1

# N = 10
# arr = generateList(N)
# fileWrite(arr)
# arr = fileReadToWriteWork('outfile.txt')
# print(arr)
# arr = checkListForMinMax(arr)
# print(arr)
# fileWrite(arr, 'outfile.txt', 'a+')

# 4.2

# fileReadToWriteWork('infile.txt', 'f1.txt')
# fileReadToWriteWork('f1.txt', 'outfile.txt')

# 4.3

# N = 5
# arr = generateList(N)
# fileWrite(arr, 'algorithm.txt')
# print(arr)
# arr = directSort(arr)
# print(arr)
# fileWrite(arr, 'algorithm.txt', 'a+')

# 4.4

# arr = list([44, 55, 12, 42, 94, 18, 0.6, 67])
# print(arr)
# arr = includeSort(arr, 2)
# print(arr)
