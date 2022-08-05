import add_input
import print_do


def data_in_file():
    s = ""
    d = add_input.get_data()
    file_name = d["file_name"]
    del d["file_name"]
    d_in = print_do.my_base_to_dict(file_name)
    for k, v in d.items():
        d_in[k].append(v)
    count = 0
    for k, v in d_in.items():
        s += ("" if count == 0 else "\n") + k + ";" + ";".join(v)
        count += 1
    with open(file_name, "w") as file:
        file.write(s)
