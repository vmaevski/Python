from cgi import print_form
import numbers


print("Hallo, world!")

# Типы данных и переменные.
# int, float, boolean, str, list, None

a = 123
b = 1.56
Value = None
Value = 12345
print(type(a))
print(type(b))
print(type(Value))
s = "'qwert"  # обратный слеш перед ' позволяет вывести его на печать
print(s)
s = "Hallo \n world"  # обратный слеш+n - перенос на новую строку
print(s)
print(a, b, s)
print(a, "-", b, "-", s)
print("{} - {} - {}".format(a, b, s))
print("{2} - {0} - {1}".format(a, b, s))  # меняем порядок
print(f"{a} - {b} - {s}")  # "" или ''
f = True
print(f, type(f))
list = ["a", "1", "hallo"]  # список строк
print(list)
##################################### Ввод - вывод
print("Введите значение a")
a = input()
print(f"a = {a}")
print("Введите значение a")
a = int(input())
print("Введите значение b")
b = float(input())
print(a, " + ", b, " = ", a + b)
##################################### Арифметические операции
a = 1.3213215
b = 3
c = round(a * b, 3)  # округление до 3го знака
print(c)
##################################### Логические операции
# >, >=, <, ,<=, ==, !=
# not, and, or - не путать с ^, &, |
f = [1, 2, 3]
print(2 in f)  # = True, т.к 2 есть в списке f
is_odd = f[0] % 2 == 0  # проверка на чётность 0го элемента списка f
print(is_odd)
##################################### Управляющие конструкции if, if-else
a = int(input("a = "))
b = int(input("b = "))
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("a = b")
##################################### Управляющие конструкции цикл while
original = 123
inverted = 0
while original != 0:
    inverted = inverted * 10 + original % 10
    original //= 10
print(inverted)
##################################### Управляющие конструкции цикл while-else
original = 123
inverted = 0
while original != 0:
    inverted = inverted * 10 + original % 10
    original //= 10
else:
    print("Пожалуй, хватит!")
print(inverted)
##################################### Управляющие конструкции цикл for
for i in 1, 2, 3, 4:
    print(i**2)


# range
r = range(10)
for i in r:
    print(i)
# или
for i in range(1, 10, 2):  # от 1 до 10 с интервалом 2
    print(i)
for i in "qwerty":
    print(i)
##################################### Строки
text = "съешь ещё этих мягких французских булок"
print(len(text))  # 39
print("ещё" in text)  # True
print(text.isdigit())  # False
print(text.islower())  # True
print(text.replace("ещё", "ЕЩЁ"))
for c in text:
    print(c)
print(text[0])  # с
print(text[1])  # ъ
# print(text[len(text)])      # IndexError
print(text[len(text) - 1])  # к
print(text[-5])  # б
print(text[:])  # print(text)
print(text[2:5])  # ешь
print(text[len(text) - 2 :])  # ок
print(text[6:-18])  # ещё этих мягких
print(text[0 : len(text) : 6])  # сеикакл
print(text[::6])  # сеикакл
text1 = text[2:9] + text[-5] + text[:2]
print(text1)
##################################### Списки
# Списки - это пронумерованная изменяемая коллекция объектов одного типа
numbers = [1, 2, 3, 4, 5]
print(numbers)
ran = range(1, 6)        # Диапазон
print(type(ran))         # <class 'range'>
# numbers = list(ran)      # Список
print(type(numbers))     # <class 'list'>
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)    # [20, 4, 6, 8, 10]
print(numbers)  # [10, 2, 3, 4, 5]
print(f'{len(numbers)} - length')

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)            # red green blue
for e in colors:
    print(e*2)          # redred greengrenn blueblue
colors.append('gray')   # добавить в конец
print(colors)           # red green blue gray
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] # удалить элемент
print(colors)

####################### Функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))

