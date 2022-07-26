# 2) Задача: предложить улучшения кода для уже решённых задач с помощью использования
# **лямбд, filter, map, zip, enumerate, list comprehension

# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

li = [1, 2, 3, 5, 1, 5, 3, 10]
# Вариант 1:
nonRepeating = list(
    li[i] for i in range(len(li)) if not ((li[i] in li[:i]) or (li[i] in li[i + 1 :]))
)
print(f"v1: {li} => {nonRepeating}")
# Вариант 2:
nonRepeatingFilter = list(
    filter(lambda i: not ((i in li[: li.index(i)]) or (i in li[li.index(i) + 1 :])), li)
)
print(f"v2: {li} => {nonRepeatingFilter}")


# Найти сумму чисел списка стоящих на нечетной позиции
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = 6
dictionary = dict(enumerate([3 * i + 1 for i in range(1, n + 1)], 1))
print(f"{n = }: {dictionary}")
