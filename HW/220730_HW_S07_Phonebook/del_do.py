from operator import index
import del_input

def my_base_to_list():
    temp_list = []
    with open("220730_my_base.txt", "r") as file:
        data = file.read()
        list = data.split(";")
        for i in range(len(list)):
            temp_list.append(list[i].split(","))
        return temp_list  

def del_contact():
    list = my_base_to_list()
    index = find_index()
    if index != -1:
        list.pop(index)
        for i in range(len(list)):
            list[i] = ",".join(list[i])
        str = ";".join(list)
        with open("220730_my_base.txt", "w", encoding="utf-8") as file:
            file.write(str)   
            print('Контакт удалён.') 

def find_index():
    surname = del_input.get_surname()
    name = del_input.get_name()
    index = -1
    list = my_base_to_list()
    for i in range(len(list)):
        if list[i][0] == surname and list[i][1] == name:
            index = i
            a =input(f"Удалить контакт: {' '.join(list[i])} (y/n): ")
            if a == 'y':
                return i
            else:
                index = -1
                print("Ничего не удалено.")  
                return -1   
    if index == -1:
        print('Такой контакт не найден.') 
        return -1           