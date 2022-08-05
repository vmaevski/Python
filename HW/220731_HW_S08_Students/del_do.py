from numpy import arange
from pandas import Index
import del_input


def imp_file_to_list(file_name):
    temp_list = []
    with open(file_name, "r") as file:
        data = file.read()
        list = data.split("\n")
        for i in range(len(list)):
            temp_list.append(list[i].split(";"))
        return temp_list


def do():
    index = -1
    s = ""
    file_name = del_input.get_file_name()
    if file_name == "220731_Students.txt":
        data = input("Введите фамилию ученика для удаления: ")
    else:
        data = input("Введите номер кабинета для удаления: ")
    list = imp_file_to_list(file_name)
    for i in range(len(list[1])):
        if data == list[0][i]:
            index = i
    if index > -1:
        if input(f"Удалить элемент {data}? (y/n) ") == "y":
            for i in range(len(list)):
                list[i].pop(index)
    else:
        print(f"Значение {data} не найдено.")
    for i in range(len(list)):
        s += ("" if i == 0 else "\n") + ";".join(list[i])

    with open(file_name, "w") as file:
        file.write(s)
