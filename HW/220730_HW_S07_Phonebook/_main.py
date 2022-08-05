import print_controller
import find_controller
import add_controller
import del_controller
import export_controller
import import_controller

a = int(
    input(
        "Задайте действие:\n\
        1 - вывод всех контактов\n\
        2 - поиск контакта по имени\n\
        3 - добавить новый контакт\n\
        4 - удалить контакт\n\
        5 - экспортировать справочник\n\
        6 - ипортировать справочник\n"
    )
)
if a == 1:
    print_controller.do()
elif a == 2:
    find_controller.do()
elif a == 3:
    add_controller.do()    
elif a == 4:
    del_controller.do()    
elif a == 5:
    export_controller.do()
elif a == 6: 
    import_controller.do()        
else:
    print('Действие не выбрано...')    

