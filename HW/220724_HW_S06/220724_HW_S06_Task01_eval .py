# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     (1+2)*3 => 9;


def str_in_list(s):
    str = ""
    list = []
    is_num = 0
    for i in range(len(s)):
        if s[i].isdigit() or ((i == 0 or s[i - 1] == "(") and (s[i] == "-")):
            str += s[i]
            is_num = 1
        else:
            if is_num == 1:
                list.append(int(str))
            list.append(s[i])
            str = ""
            is_num = 0
    if is_num == 1:
        list.append(int(str))

    return list


def calc_with_hooks(s):
    while "(" in s:
        if "(" in s:
            index_hook_open = s.index("(")
        if ")" in s:
            index_hook_close = s.index(")")
        res = calc(s[index_hook_open + 1 : index_hook_close])
        for i in range(1, index_hook_close + 1 - index_hook_open):
            s.pop(index_hook_close - i)
        s[index_hook_open] = res
    return calc(s)


def calc(expression):
    while len(expression) > 1:
        if "*" in expression or "/" in expression:
            if "*" in expression and "/" in expression:
                if expression.index("*") < expression.index("*"):
                    i = expression.index("*")
                    res = expression[i - 1] * expression[i + 1]
                else:
                    i = expression.index("/")
                    res = expression[i - 1] / expression[i + 1]
            elif "*" in expression:
                i = expression.index("*")
                res = expression[i - 1] * expression[i + 1]
            else:
                i = expression.index("/")
                res = expression[i - 1] / expression[i + 1]
        elif "+" in expression or "-" in expression:
            if "+" in expression and "-" in expression:
                if expression.index("+") < expression.index("-"):
                    i = expression.index("+")
                    res = expression[i - 1] + expression[i + 1]
                else:
                    i = expression.index("-")
                    res = expression[i - 1] - expression[i + 1]
            elif "+" in expression:
                i = expression.index("+")
                res = expression[i - 1] + expression[i + 1]
            else:
                i = expression.index("-")
                res = expression[i - 1] - expression[i + 1]
        expression[i - 1] = res
        expression.pop(i + 1)
        expression.pop(i)
    return res


s = "2+2"
print(f"{s} = {calc_with_hooks(str_in_list(s))}")
s = "(1+2)*3"
print(f"{s} = {calc_with_hooks(str_in_list(s))}")
s = "(-24/3-5)*(3-4+5)"
print(f"{s} = {calc_with_hooks(str_in_list(s))}")
s = "(-24/3-5)*(3-4)+5"
print(f"{s} = {calc_with_hooks(str_in_list(s))}")
