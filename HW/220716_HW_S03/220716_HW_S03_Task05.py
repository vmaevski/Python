# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def negaFibonacci(k):
    list = [1, 0, 1]
    for i in range(2, k + 1):
        start = list[1] - list[0]
        end = list[-1] + list[-2]
        list.insert(0, start)
        list.append(end)
    return list


k = 8
print(negaFibonacci(k))
