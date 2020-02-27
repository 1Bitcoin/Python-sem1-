import tkinter as tk
from logic import *
from Frame_Canvas import Frame_Canvas
from Frame_Input import Frame_Input

import tkinter.scrolledtext as tkscrolled


root = tk.Tk()
root.title("Защита Лабораторной работы №4")
root.minsize(800, 400)

frame_input = Frame_Input(root, bg='light gray')

frame_canvas = Frame_Canvas(root, lambda a, b, ans: frame_input.handler_change_set(a, b, ans))

frame_input.set_handler(frame_canvas.get_answer, frame_canvas.clear)
frame_input.add_points(frame_canvas.add_point)
frame_input.add_line(frame_canvas.add_circle)

frame_input.pack(side=tk.RIGHT, fill=tk.Y)
frame_canvas.pack(expand=True, fill=tk.BOTH)


root.mainloop()