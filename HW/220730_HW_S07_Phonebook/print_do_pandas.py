import pandas as pd

def my_base_to_list():
    temp_list = []
    with open("220730_my_base.txt", "r") as file:
        data = file.read()
        list = data.split(";")
        for i in range(len(list)):
            temp_list.append(list[i].split(","))
        return temp_list


def print_to_terminal():
    list = my_base_to_list()
    df = pd.DataFrame(data=list)
    print(df)
