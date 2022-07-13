# Реализуйте алгоритм перемешивания списка.
# *** Алгоритм генерирования случайного числа реализован 
# в функции myRandomInt(min, max) через привязку к микросекундам текущего времени.
# Алгоритм перемешивания randomMixList(list) использует полученные таким способом случайные числа

import datetime


def myRandomInt(min, max):  # возвращает случайное целое число N, min <= N <= max
    return min + round((max - min) * datetime.datetime.now().microsecond / 1000000)


def randomMixList(list):
    mixList = []
    while len(list) > 0:
        randomI = myRandomInt(0, len(list) - 1)
        mixList.append(list[randomI])
        list.pop(randomI)
    return mixList


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(randomMixList(list))
