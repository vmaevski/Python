def get_data():
    file_name = get_file_name()
    with open(file_name, "r") as file:
        s = file.read()
        s = s.split("\n")
        len_s = len(s)
    print("Внесите данные нового элемента:  ")
    d = {}
    d["file_name"] = file_name
    good = 1
    save = 0
    while good:
        for i in range(len_s):
            a = s[i].split(";")
            if len_s == 4 and a[0] == "class":
                d[a[0]] = input(f'Заполните через пробел поле "{a[0]}": ')
            else:
                d[a[0]] = input(f'Заполните поле "{a[0]}": ')
            save = 1
        if save == 1:
            s_d = " ".join(d.values())
            a = input(f"Вы внесли данные нового элемента': \n{s_d}\nСохранить? (y/n)")
        if a == "y":
            good = 0
            return d
        elif a == "n":
            a = input(f"Заполнить ещё раз? (y - Да / n - отмена)")
            good = 0 if a == "n" else 1
            if good == 0:
                print(f"Добавление нового элемента отменено.")


def get_file_name():
    file_name = ""
    a = input(
        'Добавить новый элемент в таблицу "Ученики" - нажмите "1"\nДобавить новый элемент в таблицу "Кабинеты" - нажмите "2"\n'
    )
    if a == "1":
        file_name = "220731_Students.txt"
    elif a == "2":
        file_name = "220731_Cabinets.txt"
    return file_name
