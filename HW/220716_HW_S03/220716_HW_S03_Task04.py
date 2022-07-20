# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def fromDecToBin(b):
    a = b
    res = ""
    while True:
        if a > 0:
            res = str(a % 2) + res
            a //= 2
        else:
            return res


a = 45
print(f"{a} -> {fromDecToBin(a)}")
a = 3
print(f"{a} -> {fromDecToBin(a)}")
a = 2
print(f"{a} -> {fromDecToBin(a)}")
