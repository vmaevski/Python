# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def diffFract(list):
    min = list[0] - int(list[0])
    max = list[0] - int(list[0])
    for i in list:
        fract = i - int(i)
        if fract != 0:  # считаем, что если дробная часть = 0, то её нет.
            if min > fract:
                min = fract
            if max < fract:
                max = fract
    return max - min


list = [1.1, 1.2, 3.1, 5, 10.01]
print(f"{list} => {round(diffFract(list), 2)}")
