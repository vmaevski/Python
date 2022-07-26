# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
#         *Пример:*
#         1+2*3 => 7;
#         (1+2)*3 => 9;

# print('2'.isdigit())

# def calc(s):
#     count = ''
#     digit = []
#     for char in s:
#         if char.isdigit():
#             count += char
#         else:
#             digit.append(int(count))

#             count = ''
#     digit.append(int(count))
#     print(digit)


def calc(s):
    count = ""
    digit = []
    for i in range(len(s)):
        if s[i].isdigit():
            count += s[i]
        else:
            digit.append(int(count))
            digit.append(s[i])
            count = ""
    digit.append(int(count))

    return digit
def decision(my_list):
    while len(my_list) > 1:
        if '*' in my_list:
            i = my_list.index('*')
            res = my_list[i-1] * my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        elif '/' in my_list:
            i = my_list.index('/')
            res = my_list[i-1] / my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        elif '+' in my_list:
            i = my_list.index('+')
            res = my_list[i-1] + my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        elif '-' in my_list:
            i = my_list.index('-')
            res = my_list[i-1] - my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
    return res
s = '24/3-5*3-3'
my_list = calc(s)
print(calc(s))
print(decision(my_list))


# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
def nonRepeatingElements(list):
    outputList = []
    for i in range(0, len(list)):
        if i == 0:
            if not (list[i] in list[i + 1 :]):
                outputList.append(list[i])
        elif i == len(list) - 1:
            if not (list[i] in list[:i]):
                outputList.append(list[i])
        else:
            if not ((list[i] in list[:i]) or (list[i] in list[i + 1 :])):
                outputList.append(list[i])
    return outputList


list = [1, 3, 8, 20, 15, 20, 8, 1]
print(
    f"Список неповторяющихся чисел последовательности {list} -> {nonRepeatingElements(list)}"
)
list = [1, 2, 3, 5, 1, 5, 3, 10]
print(
    f"Список неповторяющихся чисел последовательности {list} -> {nonRepeatingElements(list)}"
)
