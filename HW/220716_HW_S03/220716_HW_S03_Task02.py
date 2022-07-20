# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def multOfPairs(list):
    listRes = []
    if len(list) % 2 == 0:
        iter = len(list) // 2
    else:
        iter = len(list) // 2 + 1
    for i in range(0, iter):
        listRes.append(list[i] * list[-i - 1])
        print(f"{list[i]} x {list[-i-1]} = {list[i]*list[-i-1]}")
    return listRes


list = [2, 3, 4, 5, 6]
print(list)
print(multOfPairs(list))
print()
list = [2, 3, 5, 6]
print(list)
print(multOfPairs(list))
