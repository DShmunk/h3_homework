from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# для добычи корня
import math

root = Tk()
root.title("Calculator")

# сотворение ввода
calc_entry = Entry(root, width = 44)
calc_entry.grid(row=0, column=0, columnspan=4, sticky=N+S+W+E)

# сотворение кнопок
bttn_list = [
"(", ")", "√2", "/",
"7", "8", "9", "*",
"4", "5", "6", "-",
"1", "2", "3", "+",
"C", "0", ".", "=",
 ]
# присвоение кнопкам места и действий
r = 1
c = 0
for i in bttn_list:
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd, width=12).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

# функционал калькулятора
def calc(key):
    if key == "=":
# проверка на начало ввода текста (ибо не мышью единой) + немного обезопасить eval
        str1 = "0123456789.-+*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
# расчет при помощи ф-ии eval
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
# если навводили непонятного
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
#очищение поля ввода
    elif key == "C":
        calc_entry.delete(0, END)
# скобки
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
# корень
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
# после ввода "=" очистить поле
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

root.mainloop()