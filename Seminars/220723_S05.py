# # В файле находится N натуральных чисел, записанных через пробел.
# # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.


# with open('220717_test.txt', 'r') as file:
#         read_file = file.read()
#         list = read_file.split()
#         print(list)
#         for i in range(1, len(list)):
#             if int(list[i]) != int(list[i-1]) + 1:
#                 print(f'Пропущено число {int(list[i-1]) + 1}')


# 1. Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


# def increasing(list):
#     countMax = 0
#     iMax = 0
#     for i in range(0, len(list)-1):
#         count = 0
#         for j in range(i, len(list)-1):
#             if list[i + 1] > list[i]:
#                 count += 1
#             else:
#                 print(f'{j = }')
#                     break
#                 if countMax < count:
#                     countMax = count  
#                     iMax = i
#     print(f'{list[iMax:iMax+countMax]}, {iMax = }, {countMax = }')          


# list = [1, 5, 2, 3, 4, 6, 1, 7]
# # print(increasing(list))
# increasing(list)

# l = [1, 5, 2, 3, 4, 6, 1, 7]

# r1=[]
# for j in range(0,len(l)):
#     for i in range(j,len(l)):
#         if i ==j:
#             r1.append(l[i])
#         elif l[i]>r1[-1]:
#             r1.append(l[i])
#     print(r1)
#     r1.clear()



# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
def del_text(text, del_str):
    list = text.split()
    # print(list)
    for i in range(len(list)):
        if not(del_str in list[i]:


text = 'абв долрдлор абв абв абв ждотджотабв '
del_str = 'абв'
print(del_text(text, del_str))
