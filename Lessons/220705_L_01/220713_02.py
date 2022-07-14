# # ***********************  Файлы
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для ПЕРЕзаписи данных
# w+, r+
from re import S


colors = ["red", "green", "blue"]
# data = open('file.txt', 'a')
# # data.writelines(colors) # пазделителей не будет
# data.write('Line 1123\n')
# data.write('Line 2123\n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line 111 \n')
#     data.write('line 222 \n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# **************************** Функции и модули

# import myRandom
# print(myRandom.myRandomInt(0, 10))

# import myRandom as r
# print(r.myRandomInt(0, 10))

# def new_string(symbol, count=3):
#     return symbol * count

# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))

# def concatenatio(*param):
#     s: str =""
#     for item in param:
#         s += item
#     return s

# print(concatenatio('a', 'b', 'm'))   # abm
# print(concatenatio('a', '1'))   # a1
# print(concatenatio(1, 2, 3))   # TypeError

# *******************************    Рекурсия


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# ********************************** Кортежи - неизменяемые списки
# a = (1, 2, 15, 4)
# print(a[0]) # 1
# print(a[-2]) #15

# for i in a:
#     print(i)

# t = tuple(['red', 'green', 'blue']) # список преобразовывается в кортеж
# r, g, b = t # распаковывется кортеж
# print(f'{r = }, {g = }, {b = }')

# ************************************* Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу
# dictionary = {}
# dictionary = \
#     {
#         "up": "^", 
#         "left": "<-", 
#         "down": "v", 
#         "right": "->"
#     } 
# print(dictionary)    # {'up': '^', 'left': '<-', 'down': 'v', 'right': '->'}
# print(dictionary['left']) # <-

# for k in dictionary.keys(): # кючи
#     print(k) 
# for k in dictionary.values(): # значения
#     print(k)

# ************************************** Множества 
# colors = {'red', 'green', 'blue'}
# print(type(colors)) # <class 'set'> - множество
# print(colors) # {'green', 'red', 'blue'}
# colors.add('red') # {'green', 'red', 'blue'} добавления существующего элемента не происходит
# colors.add('gray') # {'green', 'gray', 'red', 'blue'}
# colors.remove('red') # {'blue', 'gray', 'green'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# colors.clear() # set() {}
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # {1, 2, 3, 5, 8}
# u = a.union(b) # {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # {8, 2, 5}
# dab = a.difference(b) # {1, 3}
# dba = b.difference(a) # {13, 21}

# s = frozenset(a) # неизменяемое множество

# **************************************** Списки
list1 = [1, 2 ,3, 4, 5, ]
list1.pop() # удалет последний элемент [1, 2, 3, 4]
list1.pop(2) # удаляет элемент с индексом 2 [1, 2, 4]
list1.insert(2, 11) # вставляет на позицию с индексом 2 число 11 [1, 2, 11, 4]
list1.append(12) # вставляет в конец списка значение 12 [1, 2, 11, 4, 12]
print(list1)
