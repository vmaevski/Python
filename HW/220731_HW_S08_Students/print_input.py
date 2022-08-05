def get_file_name():
    s = ""
    a = input(
        'Напечатать таблицу "Ученики" - нажмите "1"\nНапечатать таблицу "Кабинеты" - нажмите "2"\n'
    )
    if a == "1":
        s = "220731_Students.txt"
    elif a == "2":
        s = "220731_Cabinets.txt"
    return s
