# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
def del_text(text, del_str):
    list = text.split()
    # print(list)
    output_str = ''
    for i in range(len(list)):
        if not(del_str in list[i]):
            if output_str != '':
                output_str += ' '
            output_str += list[i]
    return output_str
text = 'абв долрдлор абa абв абв ждотджотабв '
del_str = 'абв'
print(del_text(text, del_str))
