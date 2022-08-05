def get_file_name():
    s = ""
    a = input(
        'Удалить элемент справочника "Ученики" - нажмите "1"\nУдалить элемент справочника "Кабинеты" - нажмите "2"\n'
    )
    if a == "1":
        s = "220731_Students.txt"
    elif a == "2":
        s = "220731_Cabinets.txt"
    return s
