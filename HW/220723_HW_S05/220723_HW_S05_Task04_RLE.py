#4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def strInCode(s):
    s_out = ''
    index = 0
    this_is_the_end = 0
    for i in range(0, len(s)):
        i = index
        count = 1
        if this_is_the_end == 1:
            break
        if i == len(s) - 1:
            s_out += str(count) + str(s[i])
            break
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                count += 1
                if j == len(s) - 1:
                    this_is_the_end = 1
                    s_out += str(count) + str(s[j])
            elif s[i] != s[j]:
                s_out += str(count) + str(s[i])
                index = j
                break
    return s_out

def codeInStr(s):
    len_s = len(s)
    s_out =''
    el = ''
    list = []
    for i in range(len_s):
        if s[i].isdigit():
            el += s[i]
            if not(s[i+1].isdigit()):
                list.append(int(el))
        else:
            for j in range(int(el)):
                s_out += s[i]
                el = ''
    return s_out

s = "wwwwwwwwwbbbwwwwwwwwwwwwwwwwwwwwwwwwbwwwwwwwwwwwwww"
with open('220723_HW_S05_Task04_RLE_Code.txt', 'w', encoding='utf-8') as file:
    file.write(strInCode(s))
with open('220723_HW_S05_Task04_RLE_Code.txt', 'r') as file:
    code = file.read()
with open('220723_HW_S05_Task04_RLE_Str.txt', 'w', encoding='utf-8') as file:
    file.write(codeInStr(code))