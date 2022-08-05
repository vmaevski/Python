def get_data():
    print('Внесите данные нового контакта:')
    good = 1
    save = 0
    while good:
        list = ['','','','']
        for i in range(len(list)):
            if i == 0:
                q = 'Фамилия: '
            elif i == 1:
                q = 'Имя: '
            elif i == 2:
                q = 'Номер: '
            else:
                q = 'Описание: '
            list[i] = input(q)
            save = 1
            if list[i] == '':
                print('Не оставляйте пустых полей.\nСначала.')
                save = 0
                break    
        if save == 1:    
            a = input(f"Вы внесли данные нового контакта: \n{' '.join(list)}\nСохранить? (y/n)")
            if a == 'y':
                good = 0
                return list 
            elif a == 'n':
                a = input(f"Заполнить ещё раз? (y - Да / n - отмена)")
                good = 0 if a == 'n' else 1
                if good == 0:
                    print(f'Добавление нового контакта отменено.')



