# Напишите программу, которая определит позицию второго 
# вхождения строки в списке, либо сообщит, что её нет.

def posSecIn(list, a):
    count = 0
    for i in list:
        if a in i:
            count += 1
            if count == 2:
                return list.index(i)
    if count == 0:
        return -1        
    else:
        print(f'Ко-во обнаруженных вхождений = {count}')    
                


a = 'qwer'
list = ['qwe', 'lkj', '123', '23qwert', '23']
posSecIn(list, a)
# print(f'Позиция второго вхождения = {posSecIn(list, a)}')

# время записи 1:39