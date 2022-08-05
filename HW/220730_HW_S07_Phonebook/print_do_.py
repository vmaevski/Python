def my_base_to_list():
    temp_list = []
    with open("220730_my_base.txt", "r") as file:
        data = file.read()
        list = data.split(";")
        for i in range(len(list)):
            temp_list.append(list[i].split(","))
        return temp_list


def print_to_terminal():
    s = 'Фамилия\t|\tИмя\t|\tТелефон\t|\tОписание\n'
    list = my_base_to_list()
    for i in range(len(list)):
        for j in range(len(list[i])):
            s += list[i][j] + '\t|\t'
        s += '\n'
    print(s)
