def how_to_output():
    answer = input('Хотите вывести справочник в терминал? (y/n): ')
    if answer == 'y':
        return 1
    else:
        print('Другие способы вывода справочника находятся в разработке...')
        return 0