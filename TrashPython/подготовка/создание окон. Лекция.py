from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title('Виджет checkbutton')
frame = Frame(window)

var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
var_5 = IntVar()

book_1 = Checkbutton(frame, text = 'Fortran', variable = var_1, onvalue = 1, offvalue = 0)
book_2 = Checkbutton(frame, text = 'Basic', variable = var_1, onvalue = 1, offvalue = 0)
book_3 = Checkbutton(frame, text = 'Ada', variable = var_1, onvalue = 1, offvalue = 0)
book_4 = Checkbutton(frame, text = 'Python', variable = var_1, onvalue = 1, offvalue = 0)
book_5 = Checkbutton(frame, text = 'Swift', variable = var_1, onvalue = 1, offvalue = 0)

def dialog():
    srt = 'Выбор языка'
    if var_1.get() == 1:
        str += '\n1954'
    if var_2.get() == 2:
        str += '\n1964'
    if var_3.get() == 3:
        str += '\n1983'
    if var_4.get() == 4:
        str += '\n1991'
    if var_5.get() == 5:
        str += '\n2014'
    box.showinfo('Годы создания', str)
    
btn = Button(frame, text = 'Выбор', command = dialog)
btn.pack(side = RIGHT, padx = 5)

book_1.pack(side = LEFT)
book_2.pack(side = LEFT)
book_3.pack(side = LEFT)
book_4.pack(side = LEFT)
book_5.pack(side = LEFT)

frame.pack(padx = 30, pady = 30)
window.mainloop()
