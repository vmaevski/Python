# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа определять количество вхождений одной строки в другую.


def strFor(st1, st2):
    t = 0
    for i in range(len(st1) - len(st2) + 1):
        if st1[i : i + len(st2)] == st2:
            t += 1
    return t

def strFind(st1, st2):
    t = 0
    position = 0
    while (True):
        position = st1.find(st2, position)
        if position == -1:
            break
        else:
            # position += len(st2)
            position += 1
            t += 1
    return t            

def strCount(st1, st2):
    return st1.count(st2)



# st1 = "!Привет, мир, привет!"
# st2 = "вет"
st1 = "jjjj"
st2 = "jj"

print(strFor(st1, st2))
print(strFind(st1, st2))
print(strCount(st1, st2))