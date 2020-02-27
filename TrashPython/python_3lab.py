# TODO
# Tkinter
# Возможные ошибочные ситуации (потестировать)
# Интегрировать график в ткинтер (факультатив)

# Подключаем библиотеки
import matplotlib.pyplot as plt
import pylab
from matplotlib import mlab
from tkinter import * # на будущее
from numpy import arange
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb
from math import sin

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
   
def about_program():  
    text = '''
Коды ошибок в программе

Code Error 0: OK

Code Error 1: Метод разошелся

Code Error 2: Деление на ноль

Code Error 3: Достигнуто максимальное количество итераций

'''  
    window = Toplevel(root)
    info = Label(window, text = text, justify = LEFT)
    info.pack()
    
root = tk.Tk()
#a = ['123', '456', '45676576', '411ww56', '45q23236', '456dfhgdfhfgh']

root.geometry('600x400')
mainMenu = Menu(root)
root.configure(menu = mainMenu)

table = Table(root, headings=('#', '[x_i, x_i+1]', '~x', 'f(~x)',
                              'Кол-во итераций', 'Code error'))

third_item = Menu(mainMenu, tearoff = 0)
mainMenu.add_cascade(label = 'About', menu = third_item)
third_item.add_command(label = 'Help', command = about_program)

def display_full_name():
    roots = []
    global flag
    flag = 0
    window = tk.Toplevel(root)
    window.destroy()
    global dx
    dx = float(entryh.get())
    global xmin
    xmin = float(entry1.get())
    global xmax 
    xmax = float(entry2.get())
    global eps
    eps = float(entry3.get())
    global maxIterations
    maxIterations = int(entry4.get())
    
    def func (x):
        #return x ** 3 - 9 * x + 1
        #return x ** 2 - 4
        return sin(x)

    def findX (y, arrayX, arrayY):
        for i in range(len(arrayY)):
            if y == arrayY[i]:
                count = i
                return arrayX[count]
            
    # Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
    xlist = mlab.frange (xmin, xmax, dx /100)
    
    # Вычислим значение функции в заданных точках
    ylist = [func (x) for x in xlist]
    
    # Прямая у = 0
    y0list = [0 for x in xlist]
    
    # Минимум и максимум функции на заданном отрезке
    yMaxP = max(ylist)
    xMaxP = findX(yMaxP, xlist, ylist)
    
    yMinP = min(ylist)
    xMinP = findX(yMinP, xlist, ylist)
    
    # Рисуем график и прямую
    pylab.plot (xlist, ylist)
    pylab.plot (xlist, y0list)
    
    # Ставим точки
    plt.scatter (xMaxP, yMaxP, color='green', s=40, marker='o')
    plt.scatter (xMinP, yMinP, color='red', s=40, marker='o')
    
    # Показываем окно с графиков
    pylab.show()
    
    # Проверка
    def warning(xmin, xmax, ans, N, array, tryMax, tryMin):
        global flag
        flag = 0
        print('trymax = ', tryMax, 'trymin = ', tryMin)
        if tryMin <= round(ans, 1) <= tryMax:
            print('N = ', N, 'x1 = ', ans)
            if round(abs(func(round(ans, 1))), 1) != 0.0:
                array.append('')
                array.append('{:.4}'.format(''))
                array.append(N)
                array.append('0')
                flag = 1
                print('bad')
            else:
                print('все ок error 0')
                if ans not in roots:
                    array.append('{:.4}'.format(ans))
                    roots.append(round(ans, 4))
                    array.append('{:.1}'.format(func(ans)))
                    array.append(N)
                    array.append('0')
                    flag = 0
                else:
                    flag = 1
                    
            #else:
                    #flag = 1  
                
        elif func(tryMin) * func(tryMax) <= 0 and tryMin <= round(ans, 1) <= tryMax:
            print('Корень есть, но метод разошелся')
            print(ans)
            array.append('-')
            array.append('-')
            array.append('-')
            array.append('1')
            roots.append('1')
            flag = 0
            
            
        else:
            print('xmin = ', tryMin, 'xmax = ', tryMax)
            print('Метод разошелся error 1')
            print(ans)

            flag = 2
    
    def sec(xmin, xmax, eps, maxIterations, array, tryMax, tryMin):
        global flag
        flag = 0
        flagError = 0
        x0 = xmax
        x1 = xmax + eps + 0.00001
        N = 0
        print(x1 - x0)
        while abs(x1 - x0) >= eps:
             if abs(func(x1) - func(x0)) > 1e-12:
                 if N < maxIterations:
                     x1, x0 = x1 - (x1 - x0) * func(x1) / (func(x1) - func(x0)), x1
                     N += 1
                 else:
                     print('Достигнуто максимальное количество итераций. error 3')
                     flagError = 1
                     array.append('')
                     array.append('')
                     array.append(N)
                     array.append('3')
                     flag = 4
                     break
             else:
                 print('Деление на ноль. error 2')
                 array.append('')
                 array.append('')
                 array.append(N)
                 array.append('2')
                 flagError = 1
                 flag = 3
                 break
             
        if flagError == 0:
            warning(xmin, xmax, x1, N, array, tryMax, tryMin)

    
    g = []
    number = 1
    # Проходим по элементарному отрезку
    for i in arange(xmin, xmax, dx):
        if i + dx <= xmax:
            print(flag)
            a = []
            k = 0
            a.append(number)
            print('\n', round(i + k * dx, 4), ' ', round(i + (k + 1) * dx, 4))
            gg = str(round(i + k * dx, 4))
            bgg = str(round(i + (k + 1) * dx, 4))
            buf = '[', gg, ';', bgg, ']'
            a.append(buf)
            sec(i + k * dx, (i + k * dx), eps, maxIterations, a, i + (k + 1) * dx, i + k * dx)
            if flag == 0:
                g.append(a)
                number += 1
            flag = 0
        else:
            print(flag)
            a = []
            k = 0
            a.append(number)
            print('\n', round(i + k * dx, 4), ' ', round(xmax, 4))
            gg = str(round(i + k * dx, 4))
            bgg = str(round(xmax, 4))
            buf = '[', gg, ';', bgg, ']'
            a.append(buf)
            sec(i + k * dx, xmax, eps, maxIterations, a, xmax, i + k * dx )
            if flag == 0:
                g.append(a)
                number += 1
            flag = 0
    if len(roots) == 0 and func(xmin) * func(xmax) > 0:
        ag = []
        ag.append('')
        bufff = '[', xmin, ';', xmax, ']'
        ag.append(bufff)
        ag.append('-')
        ag.append('-')
        ag.append('-')
        ag.append('нет корней')
        g.append(ag)
    elif func(xmin) * func(xmax) < 0 and len(roots) == 0:
        ag = []
        ag.append('')
        bufff = '[', xmin, ';', xmax, ']'
        ag.append(bufff)
        ag.append('-')
        ag.append('-')
        ag.append('-')
        ag.append('метод разошелся')
        g.append(ag)
        
        
        
    window = tk.Toplevel(root)
    table = Table(window, headings=('#', '[x_i, x_i+1]', '~x', 'f(~x)', 
                                    'Кол-во итераций', 'Code error'), rows=(g))
    table.pack(expand=tk.YES, fill=tk.BOTH)

entry1 = Entry()
entry1.place(x = 120, y = 230)

entry2 = Entry()
entry2.place(x = 120, y = 260)

entry3 = Entry()
entry3.place(x = 400, y = 230)

entry4 = Entry()
entry4.place(x = 450, y = 260)

entryh = Entry()
entryh.place(x = 120, y = 290)

Button(text="Click Me", command=display_full_name).pack()
label = Label(height=3)
label.pack()

inputTag = Label(text = "Selection from: ", font = ('Kernel', 10))
inputTag.place(x = 0, y = 230)

inputTag1 = Label(text = "Selection to: ", font = ('Kernel', 10))
inputTag1.place(x = 0, y = 260)

inputTag2 = Label(text = "Input eps: ", font = ('Kernel', 10))
inputTag2.place(x = 300, y = 230)

inputTag3 = Label(text = "Input max iterat.: ", font = ('Kernel', 10))
inputTag3.place(x = 300, y = 260)

inputTag4 = Label(text = "Input h: ", font = ('Kernel', 10))
inputTag4.place(x = 0, y = 290)

root.mainloop()