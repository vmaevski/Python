import random


from tkinter.filedialog import Open

#                               a - дозаписать, w - записать, r - чтение
                              # v
# with open('220717_test.txt', 'a', encoding='utf-8') as file:
#      file.write('Hello, world')
#      file.writelines(['how are you?\n', 'i am fine\n'])

# Так лучше не делать:
# file = open('220717_test.txt', 'a', encoding='utf-8')     
# file.write('Hello') # файл остаётся открытым
# file.close()

# n = 5
# spisok = list(range(n+1))
# with open('220717_test.txt', 'w') as file:
#     for i in spisok:
#         file.write(f'{str(i)}\n')
# with open('220717_test.txt', 'r') as file:
#     len = len(file.readlines())
#     file.seek(0)
#     for i in range(len):
#         print(f'{i = }')
#         a= file.readline()
#         print(a)

# with open('220717_test.txt', 'r') as file:
#     for i in file:
#         print(i)

# Строки - в список:
# with open('220717_test.txt', 'r') as file:
#     read_file = file.read()
#     list_of_rows = read_file.split()
# print(list_of_rows) 

# list_of_rows = list(map(int, list_of_rows))
# print(list_of_rows)    



# 01.  Создать программно файл. Записать в файл все числа от 0 до числа, заданного пользователем.
# a = int(input('Задайте число:'))
# with open('220717_S04_Task01.txt', 'w', encoding='utf-8') as file:
#         for i in range(0, a+1):
#             file.write(f'{i} ')
# # Прочитаем и выведем на печать содержимое файла:
# with open('220717_S04_Task01.txt', 'r') as file:        
#     a = file.read()    
#     print(a)

# 02. Задать список из N элементов, заполненных числами [-N, N]
# Найти произведение элементов на указанных позициях
# Позиции хранятся в файле txt в одной строке одно число.

def createList(n):
    list = [-n]
    for i in range(-n + 1, n + 1):
        list.append(list[-1] + 1)
    while len(list) > n:
        list.pop(random.randint(0, len(list) - 1))  # удалем элемент со случайным индексом, пока длина списка не будет равна n
    return list

def multiplicationNumbers(list, fileName):
    result = 1    
    with open(fileName, 'r') as file:
        read_file = file.read() 
        positions = read_file.split()
        print(positions)
        for i in positions:
            result *= list[int(i)]
    return result


with open('220717_Position.txt', 'w') as file:
    indices = input('Введите числа через пробел: ')
    indices = indices.split(' ')
    for el in indices:
        file.write(f'{el}\n')
n = 5
list = createList(n)
print(list)
print(multiplicationNumbers(list, '220717_Position.txt'))

# 03. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.


# with open('220717_test.txt', 'r') as file:
#         read_file = file.read() 
#         list = read_file.split()
#         print(list)
#         for i in range(1, len(list)):
#             if int(list[i]) != int(list[i-1]) + 1:
#                 print(f'Пропущено число {int(list[i-1]) + 1}')
            

    # 1:49
