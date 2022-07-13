# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81
def printSequenceStr(n):
    value = 1
    str = '1, '
    for i in range(1, n):
        value *= -3
        str += (f'{value}, ')
    print(str)   

def printSequenceList(n):
    list = [1]
    while len(list) < n:
        list.append(list[-1] * -3)
    print(list)

def printSequenceFor(n):
    value = 1
    print(value, end=' ')
    for i in range(1, n):
        value *= -3
        print(value, end=' ')

n = int(input('Задайте число N: '))
printSequenceStr(n)
printSequenceList(n)
printSequenceFor(n)
