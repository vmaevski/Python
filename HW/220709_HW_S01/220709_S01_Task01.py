# По двум заданным числам проверить является ли одно квадратом другого
a = int(input("Введите число a = "))
b = int(input("Введите число b = "))
if a**2 == b:
    print(f"Число {b} является квадратом числа {a}.")
elif b**2 == a:
    print(f"Число {a} является квадратом числа {b}.")
else:
    print(f"Числа НЕ являются квадратом другого.")
