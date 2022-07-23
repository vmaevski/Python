# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def simpleMultipliers(n):
    simpleNumbers = []
    for i in range(2, n):
        for j in range(2, i + 1):
            if (i % j == 0) and (i != j):
                break
            if i == j:
                simpleNumbers.append(j)
    list = []
    for i in simpleNumbers:
        if n % i == 0:
            list.append(i)
    return list


n = 1463
print(f"Список простых множителей числа {n} -> {simpleMultipliers(n)}")
n = 66
print(f"Список простых множителей числа {n} -> {simpleMultipliers(n)}")
n = 6441
print(f"Список простых множителей числа {n} -> {simpleMultipliers(n)}")
