# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# *** Позиции заданы списком listPos. (Позиция = Индекс + 1)

import random


def createList(n):
    list = [-n]
    for i in range(-n + 1, n + 1):
        list.append(list[-1] + 1)
    while len(list) > n:
        list.pop(random.randint(0, len(list) - 1))  # удалем элемент со случайным индексом, пока длина списка не будет равна n
    return list


def multiplicationNumbers(list, listPos):
    result = 1
    for i in range(len(listPos)):
        result *= list[listPos[i] - 1]
    return result


n = 5
listPos = [1, 3, 5]
list = createList(n)
print(list)
print(multiplicationNumbers(list, listPos))
