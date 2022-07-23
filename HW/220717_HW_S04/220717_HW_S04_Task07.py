# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.


with open('220717_test.txt', 'r') as file:
        read_file = file.read() 
        list = read_file.split()
        for i in range(1, len(list)):
            if int(list[i]) != int(list[i-1]) + 1:
                print(f'Пропущено число {int(list[i-1]) + 1}')
            
