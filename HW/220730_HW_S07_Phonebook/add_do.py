def do(list):
    with open('220730_my_base.txt', 'a', encoding="utf-8") as file:
        file.write(f";{','.join(list)}")
    print(f'Добвлена запись {" ".join(list)}')    