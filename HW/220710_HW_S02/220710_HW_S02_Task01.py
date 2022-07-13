# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# def sumDigit(a: float):
def sumDigit(a):
    string = str(a)
    result = 0

    for i in range(len(string)):
        if string[i].isdigit() == 1:
            result += int(string[i])
    return result


a = 6782
print(f"{a} -> {sumDigit(a)}")
a = 0.56
print(f"{a} -> {sumDigit(a)}")
