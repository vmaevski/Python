# * * * * * * * * * * * * * * УСКОРЕННАЯ ОБРАБОТКА ДАННЫХ
# **************************  lambda
# def sum(x, y):
#     return x + y

# sum = lambda x, y: x+y

# def calc(f, a, b):
# #     print(f(a, b))

# # calc(sum, 4, 5)
# calc(lambda x, y: x+y, 4, 5)


# **************************  List Comprehension
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list)

# Задача: В файле хранятся числа, нужно выбрать чётные
# и составить список триад (число, его квадрат, его куб)
# Пример:
#  1 2 3 5 8 15 23 38
# Получить: [(2, 4, 8), (8, 64, 512), (38, 1444, 54872)]

# Моё решение:
# def f(x, y):
#     return x**y

# with open('220719_L_03.txt', 'r') as file:
#     listNums = file.read().split()
# list= [(int(i), f(int(i), 2), f(int(i), 3)) for i in listNums if int(i)%2 == 0]
# print(list)

# Решение из лекции:
# file = open('220719_L_03.txt', 'r')
# data = file.read() + ' '
# file.close()
# listNumbers = []
# while data != '':
#     spacePos = data.index(' ')
#     listNumbers.append(int(data[:spacePos]))
#     data = data[spacePos+1:]
# list= []
# for i in listNumbers:
#     if not i %2:
#         list.append([i, i**2, i**3])
# print(list)
#
# Решние из лекции через lambda:
# def select(f, col):
#     return [f(x) for x in col]

# def sort(f, col):
#     return(x for x in col if f(x))

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = sort(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2, x**3), res)
# print(res)
# **************************  Функция map
# map() - применяет функцию к каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами
# li = [x for x in range(1, 20)]
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int,  input().split()))
# print(data)

# def select(f, col):
#     return [f(x) for x in col]

# def sort(f, col):
#     return(x for x in col if f(x))

# data = '1 2 3 5 8 15 23 38'.split()
# res = list(map(int, data))
# res = sort(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2, x**3), res))
# print(res)
# **************************  Функция filter()
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объетами, для которых функция вернула True.
# data = [x for x in range(1, 10)]
# # list = list(filter(lambda x: x%2==0, data))
# list = list(filter(lambda x: not x%2, data))
# print(data)
# print(list)

# def sort(f, col):
#     return(x for x in col if f(x))

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2, x**3), res))
# print(res)

# **************************  Функция zip()
#  применяется к наборы итерируемых объектов и
#  возвращает итератор с кортежами из элементов входных данных
#  zip([1, 2, 3], [о, д, т], [f, s, t])
#  => [(1, о, f), (2, д, o), (3, т, t)]
# users = ["user1", "user2", "user3", "user4", "user5"]
# ids = [10, 20, 30, 40, 50]
# data = list(zip(ids, users))
# print(data)
# **************************  Функция enumerate()
# применяется к итерируемому объекту и возвращает
# итератор с кортежами, первыми элементами которых выступают нумерующие числа
# users = ["user1", "user2", "user3", "user4", "user5"]
# data = list(enumerate(users))
# print(data)


# 36:00
