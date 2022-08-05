import pandas as pd


def my_base_to_dict(file_name):
    d = {}
    with open(file_name, "r") as file:
        s = file.read()
        s = s.split("\n")
        for i in range(len(s)):
            s[i] = s[i].split(";")
            if " " in s[i][1:]:
                d[s[i][0]] = list(s[i][1:].split(" "))
            else:
                d[s[i][0]] = s[i][1:]
    return d


def do(file_name):
    d = my_base_to_dict(file_name)
    df = pd.DataFrame(data=d)
    print(df)
