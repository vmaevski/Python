def imp_file_to_list(file_name):
    temp_list = []
    with open(file_name, "r") as file:
        data = file.read()
        list = data.split("\n")
        for i in range(len(list)):
            temp_list.append(list[i].split(";"))
        return temp_list


def report():
    cab_list = imp_file_to_list("220731_Cabinets.txt")
    stu_list = imp_file_to_list("220731_Students.txt")
    for i in range(1, len(cab_list[0])):
        print(f"\nКабинет №{cab_list[0][i]}\n\t Ученики:")
        class_list = (cab_list[3][i]).split()
        for j in range(len(class_list)):
            _class = class_list[j]
            print(f"\tКласс {_class}")
            for k in range(1, len(stu_list[4])):
                if stu_list[4][k] == _class:
                    print(
                        f"- {stu_list[0][k]} {stu_list[1][k]}: ряд {stu_list[5][k]}, парта{stu_list[6][k]}, вариант{stu_list[7][k]}"
                    )
