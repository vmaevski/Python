# # Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def polynom(k):
    polynom = ""
    coefficientList = []
    for i in range(0, k + 1):
        pow = k - i
        coefficient = random.randint(0, 100)
        if pow == k:
            polynom += str(coefficient) + "x^" + str(pow)
        elif pow == 1:
            if coefficient != 0:
                polynom += " + " + str(coefficient) + "x"
        elif pow == 0:
            if coefficient != 0:
                polynom += " + " + str(coefficient)
        else:
            if coefficient != 0:
                polynom += " + " + str(coefficient) + "x^" + str(pow)
    polynom += " = 0"
    return polynom


k = 3
with open("220717_HW_S04_Task04.txt", "w", encoding="utf-8") as file:
    file.write(polynom(k))
