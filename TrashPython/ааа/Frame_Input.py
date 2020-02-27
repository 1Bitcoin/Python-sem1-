import tkinter as tk
import tkinter.scrolledtext as tkscrolled

from logic import Point, Line

import tkinter as tk
from tkinter.messagebox import showerror
class Ask_User(tk.Toplevel):
    def __init__(self, parent, handler_desroy, cnf={}, **kwargs):
        super().__init__(parent, cnf={}, **kwargs)
        
        self.handler_desroy = handler_desroy
        
        self.grab_set()
        self.focus_get()
    
    def init_button(self, **kwargs):
        btn = tk.Button(self, text='Ok!', command=self._destroy, **kwargs)
        return btn

    def get_data(self):
        return None

    def _destroy(self):
        data = self.get_data()
        if data:
            self.handler_desroy(data)
            self.destroy()
        else:
            showerror("Error!", "Некорректные данные!")
    


class Ask_New_Circle(Ask_User):
    def __init__(self, parent, handler_desroy, cnf={}, **kwargs):
        super().__init__(parent, handler_desroy, cnf={}, **kwargs)

        self.title('Ввод данных')

        tk.Label(self, 
            text='Введите координаты первой точки',
            font = ("Times New Roman", 16)
        ).grid(row=0, columnspan=2, padx=10, pady=5)

        tk.Label(self, text='x1:', font=("Times New Roman", 16)).grid(row=1, column=0, pady=5)
        tk.Label(self, text='y1:', font=("Times New Roman", 16)).grid(row=2, column=0, pady=5)

        self.text_x1 = tk.StringVar()
        self.entry_x1 = tk.Entry(self, textvariable=self.text_x1, font = ("Times New Roman", 16))
        self.entry_x1.grid(row=1, column=1, padx=10, pady=5)

        self.text_y1 = tk.StringVar()
        self.entry_y1 = tk.Entry(self, textvariable=self.text_y1, font = ("Times New Roman", 16))
        self.entry_y1.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, 
            text='Введите радиус окружности',
            font = ("Times New Roman", 16)
        ).grid(row=3, columnspan=2, padx=10, pady=5)

        tk.Label(self, text='R:', font=("Times New Roman", 16)).grid(row=4, column=0, pady=5)

        self.text_x2 = tk.StringVar()
        self.entry_x2 = tk.Entry(self, textvariable=self.text_x2, font = ("Times New Roman", 16))
        self.entry_x2.grid(row=4, column=1, padx=10, pady=5)

        self.init_button(
            height=1, 
            font = ("Times New Roman", 16)
        ).grid(row=5, columnspan=2, padx=10, pady=5)

        self.columnconfigure(1, weight=1)

        self.resizable(False, False)
    
    def get_data(self):
        try:
            x1 = int(self.text_x1.get())
            y1 = int(self.text_y1.get())
            r = int(self.text_x2.get())
            return  (Point(x1, y1), r)
            
        except:
            return None

class Ask_New_Point(Ask_User):
    def __init__(self, parent, handler_desroy, cnf={}, **kwargs):
        super().__init__(parent, handler_desroy, cnf={}, **kwargs)

        self.title('Ввод данных')

        tk.Label(self, 
            text='Введите координаты точки',
            font = ("Times New Roman", 16)
        ).grid(row=0, columnspan=2, padx=10, pady=5)

        tk.Label(self, text='x:', font=("Times New Roman", 16)).grid(row=1, column=0, pady=5)
        tk.Label(self, text='y:', font=("Times New Roman", 16)).grid(row=2, column=0, pady=5)

        self.text_x = tk.StringVar()
        self.entry_x = tk.Entry(self, textvariable=self.text_x, font = ("Times New Roman", 16))
        self.entry_x.grid(row=1, column=1, padx=10, pady=5)

        self.text_y = tk.StringVar()
        self.entry_y = tk.Entry(self, textvariable=self.text_y, font = ("Times New Roman", 16))
        self.entry_y.grid(row=2, column=1, padx=10, pady=5)

        self.init_button(
            height=1, 
            font = ("Times New Roman", 16)
        ).grid(row=3, columnspan=2, padx=10, pady=5)

        self.columnconfigure(1, weight=1)

        self.resizable(False, False)
    
    def get_data(self):
        try:
            x = int(self.text_x.get())
            y = int(self.text_y.get())
            return  Point(x, y)
            
        except:
            return None


class Frame_Input(tk.Frame):
    def __init__(self, parent, cnf={}, **kwargs):
        super().__init__(parent, cnf={}, **kwargs)

        self['width'] = 350
        
        self.create_header("Множество А", "Добавить значение", self.add_set_point)

        self.text_setA = tkscrolled.ScrolledText(
            self, 
            height=1, 
            width= 25,
            wrap='word',
            )

        self.text_setA.pack(fill=tk.BOTH, padx=5, pady=10, expand=1)

        self.create_header("Множество B", "Добавить значение", self.add_set_line)

        self.text_setB = tkscrolled.ScrolledText(self,
            height=1,
            width= 25,
            wrap='word')
        
        self.text_setB.pack(fill=tk.BOTH, padx=5, pady=10, expand=1)

        self.text_setA['state'] = tk.DISABLED
        self.text_setB['state'] = tk.DISABLED


    def create_header(self, text, text_btn, command):
        frame = tk.Frame(self, bg = self['bg'])
        label = tk.Label(frame, text=text, padx=20, pady=5, font=("Times New Roman", 10), bg = self['bg'])
        label.pack(side=tk.LEFT)

        tk.Button(frame, text = text_btn, command = command).pack(side=tk.RIGHT, padx=10, pady=15)
        
        frame.pack()

    def set_handler(self, draw_answer, clear):
        frame = tk.Frame(self, bg=self['bg'])
        self.btn_get_answer = tk.Button(frame, text='Найти!', command=draw_answer)
        
        self.btn_get_answer.pack(side=tk.LEFT, padx=20)

        self.btn_clear = tk.Button(frame, text='Удалить Всё!', command=clear)
        self.btn_clear.pack(side=tk.RIGHT, padx=20)

        frame.pack(fill = tk.X, pady=15)

    def add_set_point(self):
        print('add_point')
        Ask_New_Point(self, self.add_points)
    
    def add_set_line(self):
        print('add_circle')
        Ask_New_Circle(self, self.add_line)


    def add_points(self, add_points):
        self.add_points = add_points
    
    def add_line(self, add_line):
        self.add_line = add_line


    def handler_change_set(self, setA, setB, answer):
        self.text_setA['state'] = tk.NORMAL
        self.text_setB['state'] = tk.NORMAL

        self.text_setA.delete('1.0', tk.END)
        self.text_setB.delete('1.0', tk.END)

        self.text_setA.insert('1.0', '\n'.join(map(str, setA)) + '\n')
        self.text_setB.insert('1.0', '\n'.join(map(str, setB)) + '\n')

        self.text_setA['state'] = tk.DISABLED
        self.text_setB['state'] = tk.DISABLED


if __name__ == "__main__":
    root = tk.Tk()

    t = Frame_Input(root, bg='red')

    t.pack(side=tk.RIGHT, fill=tk.Y)

    root.mainloop()
