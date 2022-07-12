# найти максимальное из 5 чисел
r = range(5)
count = 1
for i in r:
    i = int(input(f"Введите {count}-е число: "))
    if count == 1:
        max = i
    elif max < i:
        max = i
    count += 1
print("")
print(f"Максимальное чиcло = {max}")
print("")
