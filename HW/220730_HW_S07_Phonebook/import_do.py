from ntpath import join


def imp_file_to_list(file_name):
    temp_list = []
    with open(file_name, "r") as file:
        data = file.read()
        list = data.split("\n\n")
        for i in range(len(list)):
            temp_list.append(list[i].split("\n"))
        return temp_list


def list_to_my_base(temp_list):
    for i in range(len(temp_list)):
        temp_list[i] = ",".join(temp_list[i])
    str = ";".join(temp_list)
    with open("220730_my_base.txt", "w", encoding="utf-8") as file:
        file.write(str)


def import_do(file_name):
    temp_list = imp_file_to_list(file_name)
    list_to_my_base(temp_list)
