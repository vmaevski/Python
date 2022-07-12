# * Найти факториал числа
n = int(input('Задайте число: '))
if n < 0:
    print('Задайте положительное число!')
else:    
    factorial = 1
    for i in range(2, n + 1):
        factorial = factorial * i
    print(f'Факториал числа {n} = {factorial}')