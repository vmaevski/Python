# Задайте список. Напишите программу, которая определит,
# присутствует ли в данном списке строк некое число.

# 12 -> ['ads12', '12', 'asd', '87'] -> 'asd12', '12'

def outNum(list, a):
    # listOut = []
    print(f'{a} -> {list} -> ', end=' ')
    for i in list:
        if str(a) in i:
            # listOut.append(i)
            print(f"'{i}'", end = ' ')
    # return listOut



list = ["ads12", "12", "asd", "87"]
a = 12
# print(outNum(list, a))
outNum(list, a)


