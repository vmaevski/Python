# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("220717_HW_S04_Task06_.txt", "r") as file:
    data = file.read().split()
    averageSalary = 0
    for i in range(len(data)):
        if i % 2:
            averageSalary += int(data[i])
            if int(data[i]) < 20000:
                print(f"У сотудника {data[i-1]} оклад меньше 20тр")
    averageSalary /= len(data) / 2
    print(f"Средний оклад = {averageSalary}")

    l
