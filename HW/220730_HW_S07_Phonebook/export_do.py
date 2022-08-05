def my_base_to_list():
    temp_list = []
    with open("220730_my_base.txt", "r") as file:
        data = file.read()
        list = data.split(";")
        for i in range(len(list)):
            temp_list.append(list[i].split(","))
        return temp_list


def list_to_exp_file(temp_list, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(len(temp_list)):
            for j in range(len(temp_list[i])):
                file.write(temp_list[i][j])
                if j < len(temp_list[i])-1:
                    file.write("\n")
            if i != len(temp_list)-1:
                file.write("\n\n")


def export(file_name):
    temp_list = my_base_to_list()
    list_to_exp_file(temp_list, file_name)
