def my_base_to_list():
    temp_list = []
    with open("220730_my_base.txt", "r") as file:
        data = file.read()
        list = data.split(";")
        for i in range(len(list)):
            temp_list.append(list[i].split(","))
        return temp_list

def find(name):
    s = ''
    count = 0
    list = my_base_to_list()
    for i in range(len(list)):
        if name in list[i][1]:
            count += 1
            s += str(count) + '. ' + ' '.join(list[i]) + '\n'
    if s == '':
        print('Ничего не найдено ( ...')
    else:
        s = 'Вот, что нашлось:\n' + s
        print(s)    
            