import print_controller
import add_do
import report
import del_do

a = int(input('Выберите действие:\n1 - Вывести список учеников или кабинетов\n2 - Отчет о рассадке учеников в кабинетах\n3 - Добавить ученика или кабинет\n4 - Удалить ученика или кабинет\n'))

if a == 1:
   print_controller.print()
elif a == 2:
    report.report()
elif a == 3:
    add_do.data_in_file()
elif a == 4:
    del_do.do()    