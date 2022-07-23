# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


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
