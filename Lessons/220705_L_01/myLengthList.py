from copy import copy


def myLengthList(list):
    if list == []:
        return 0
    else:
        list.pop()
        return 1 + myLengthList(list)

def sum(list):
    if list == []:
        return 0
    else:
        s = list[0]
        list.pop(0)
        return s + sum(list)

def maximal(listIn, max):
    list = listIn.copy()
    if list == []:
        return 'List empty'
    elif len(list) == 1:
        if max < list[0]:
            max = list[0]
        return max
    else:
        list.pop(0)
        if max < list[0]:
            max = list[0]
        return maximal(list, max)
        

list = [1, 2, 10, 3, 4, 2]
print(maximal(list, -10000000000000000000000000))
print(list)