from posixpath import split


def maxPow(list):
    if "^" in list[0]:
        maxPow = int(list[0].split("^")[1])
    elif "x" in list[0]:
        maxPow = 1
    else:
        maxPow = 0
    return maxPow


def sumLists(coeffList1, coeffList2):
    list = []
    listMin = coeffList1
    listMax = coeffList2
    if len(listMax) < len(listMin):
        (listMin, listMax) = (listMax, listMin)
    for i in range(0, len(listMax)):
        if i < len(listMin):
            list.append(listMin[i] + listMax[i])
        else:
            list.append(listMax[i])
    return list


def writeInStr(sumList):
    s = " = 0"
    for i in range(0, len(sumList)):
        if i == 0:
            if sumList[i] != 0:
                s = str(sumList[i]) + s
        elif i == 1:
            if (sumList[i] != 0) and (sumList[i - 1] != 0):
                s = str(sumList[i]) + "x + " + s
        else:
            if sumList[i] != 0:
                s = str(sumList[i]) + "x^" + str(i) + " + " + s
    return s


def extractCoeff(fileName): # функция создаёт список, в котором значения - это коэффициенты, а индексы - показатели степени
    coeffList = []
    with open(fileName, "r") as file:
        s = file.read()
        list = s.split(" + ")
        lenList = len(list)
    for j in range(0, maxPow(list) + 1):
        i = lenList - 1 - j
        if " = " in list[i]:
            if "x" in list[i]:
                coeffList.insert(0, 0)
            else:
                coeffList.insert(0, int((list[i].split(" = ")[0])))
        elif not ("^" in list[i]):
            if "x" in list[i]:
                if list[i].split("x")[0] == "":
                    coeffList.insert(1, 1)
                else:
                    coeffList.insert(1, int((list[i].split("x")[0])))
            else:
                coeffList.insert(1, 0)
        else:
            if int(list[i].split("^")[1]) != j:
                coeffList.insert(j, 0)
                lenList += 1
            else:
                if list[i].split("x")[0] == "":
                    coeffList.insert(j, 1)
                else:
                    coeffList.insert(j, int(list[i].split("x")[0]))
    return coeffList


fileName1 = "220717_HW_S04_Task05_polynom1.txt"
fileName2 = "220717_HW_S04_Task05_polynom2.txt"
coeffList1 = extractCoeff(fileName1)
coeffList2 = extractCoeff(fileName2)
sumList = sumLists(coeffList1, coeffList2)

with open("220717_HW_S04_Task05_sum_polynoms.txt", "w", encoding="utf-8") as file:
    file.write(writeInStr(sumList))
    # file.write(writeInStr(sumLists(extractCoeff(fileName1), extractCoeff(fileName2))))
