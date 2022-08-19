from tkinter import *
from google_currency import convert  
import requests
import json


# функция Конвертировать

def get_currency():
    cur1 = var1.get()
    cur2 = var2.get()
    sum = cost.get()
    data = json.loads(convert(cur1, cur2, float(sum)))
    result = data['amount']
    exchange_rate = round(float(result)/float(sum),4)
    root.geometry("285x300")
    Label(root, text=f"{sum} {cur1}\nпо курсу {exchange_rate}:\n{result} {cur2}", font="arial 15").place(x=70, y=215)


# Окно:
root = Tk()
root.geometry("285x225")
root.wm_attributes('-alpha', 0.9)
root.resizable(1, 1)
root.title("Конвертер валют")

Label(root, text="Конвертер валют",
      font="arial 12 bold").pack()

currency_list = ['Выберите валюту', 'USD', 'JPY', 'RUB', 'EUR', 'GBP', 'CNH']
var1 = StringVar(root)
var1.set(currency_list[0])
var2 = StringVar(root)
var2.set(currency_list[0])
cost = StringVar(root)

Label(root, text="Ковертировать из:", font="arial 10 bold").place(x=15, y=35)
OptionMenu(root, var1, *currency_list).place(x=140, y=30)

Label(root, text="Ковертировать в:", font="arial 10 bold").place(x=15, y=85)
OptionMenu(root, var2, *currency_list).place(x=140, y=80)

Label(root, text="Ковертировать сумму:", font="arial 10 bold").place(x=15, y=135)
Entry(root, width=15, textvariable=cost).place(x=170, y=135)

# кнопка Конвертировать
Button(root, text="Конвертировать", font="arial 15 bold", bg="green", padx=2, command=get_currency).place(x=60, y=170)


root.mainloop()