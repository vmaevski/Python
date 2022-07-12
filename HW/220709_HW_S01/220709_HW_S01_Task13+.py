# * найти наибольший простой делитель числа
a = int(input("Задайте положительное число: "))
if a < 0:
    a = -a
divider = a    
for i in range(2, a):
    if a % i == 0:
        divider = int(a / i)
        divPrime = 1 # предполагаем, что делитель - простое число
        for j in range(2, divider): # проверяем, простое ли число делитель
            if divider % j == 0:
                divPrime = 0 # выяснилось, что делитель - Не простое число
                break 
        if divPrime == 1: # подтвердилось, что делитель - простое число
            break 
if divider == a:
    print('Заданное число является простым.')        
else:    
    print(f'Наибольший простой делитель числа {a} = {divider}')        






# str = f"Число {a} является простым."
# if a > 3:
#     for i in range(2, a):
#         if a % i == 0:
#             str = f"Число {a} НЕ является простым."
#             break
# print(str)
