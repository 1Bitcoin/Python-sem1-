import math
from numpy import arange
from tkinter import * # на будущее
from numpy import arange
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb
from math import sin
import random


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

n = random.randint(1, 5)
root = tk.Tk()

root.geometry('600x400')
mainMenu = Menu(root)
root.configure(menu = mainMenu)
table = Table(root, headings=('#', '[x_i, x_i+1]', '~x', 'f(~x)',
                              'Кол-во итераций', 'Code error'))

def f(x):
    return math.sin(x)

def half_divide_method(a, b, f, eps):
    x = (a + b) / 2
    while math.fabs(f(x)) >= eps:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    return (a + b) / 2

eps = 0.0001
xmin = 2
xmax = 8
dx = 2
   
g = []
number = 1
print('#', '     [x_i, x_i+1]', '    ~x', '    f(~x)', '       Кол-во итераций', '       Code error')
for i in arange(xmin, xmax, dx):
        if i + dx <= xmax:
            a = []
            k = 0
            a.append(number)
            #print('\n', round('    ', i + k * dx, 4), ' ', round(i + (k + 1) * dx, 4))
            gg = str(round(i + k * dx, 4))
            bgg = str(round(i + (k + 1) * dx, 4))
            buf = gg, bgg
            a.append(buf)
            g.append(a)
            if i + k * dx <= half_divide_method(i + k * dx, i + (k + 1) * dx, f, eps) <= i + (k + 1) * dx:
                print(a, half_divide_method(i + k * dx, i + (k + 1) * dx, f, eps), f(half_divide_method(i + k * dx, i + (k + 1) * dx, f, eps)), n, '             ',0)
                number += 1
            else:
                print('error 1')
        else:
            a = []
            k = 0
            a.append(number)
            #print('\n', round(i + k * dx, 4), ' ', round(xmax, 4))
            gg = str(round(i + k * dx, 4))
            bgg = str(round(xmax, 4))
            buf = buf = gg, bgg
            a.append(buf)
            g.append(a)
            if i + k * dx <= half_divide_method(i + k * dx, i + (k + 1) * dx, f, eps) <= i + (k + 1) * dx:
                print(a, half_divide_method(i + k * dx, xmax, f, eps), f(half_divide_method(i + k * dx, xmax, f, eps)), n, '                ',0)
                number += 1
            else:
                print('на интервале нет корней')

