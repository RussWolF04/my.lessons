# Алгоритм работы
# 1) Импортировать нужную библиотеку
# 2) Создаем окно
# 3) Создаем кнопки
# 4) Создаем сам калькулятор
#       а) исключаем возможность введения букв в клавиатуре
#       б) добавляем возможность счета (основная часть программы)
#       в) добавляем кнопку "очистить"

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title('Калькулятор')

# Логика калькулятора
def calc(key):
    global memory
    if key == "=":
# исключаем ввода букв
        str1 = "-+123456789.*/"
        if calc_entry.get() [0] not in str1:
            calc_entry.insert(END, "Первый символ не число!")
            messagebox.showerror("Ошибка!", "Вы ввели не число!")
# счет
        try: # создаем исключение
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Ошибка!")
            messagebox.showerror("Ошибка!", "Проверь правильность данных")

#Очистить поле;
    elif key == "C":
        calc_entry.delete(0, END)
# Смена -/+;
    elif key == "-/+":
        if "=" in calc_entry.delete():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get() [0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


# создаем все кнопки нашего калькулятора
bttn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "-/+", "=",
    "0", ".", "C", "", ""
]
r = 1 # столбец
c = 0 # строка

for i in bttn_list:
# пишем возможность нажатия на кнопки нашего калькулятора
    rel = ""
    cmd = lambda x = i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c>4:
        c=0
        r += 1

# окно вывода в калькуляторе
calc_entry = Entry(root, width = 33)
calc_entry.grid(row = 0, column = 0, columnspan = 5)

root.mainloop()







