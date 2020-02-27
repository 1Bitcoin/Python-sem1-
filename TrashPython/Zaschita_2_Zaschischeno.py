# Лабораторная работа №4, защита, Гришин Егор, ИУ7-25Б

from tkinter import *
from math import sqrt

def clean_canvas(event):
    for i in arr_circle:
        canvas_root.delete(i)
    arr_circle.clear()
    arr_circle_coord.clear()
    for i in arr_points:
        canvas_root.delete(i)
    arr_points.clear()
    arr_points_coord.clear()
    if line:
        canvas_root.delete(line)

def append_circle_click_start(event):
    x = event.x
    y = event.y
    arr_circle_coord.append([x, y, 0])
    arr_circle.append(canvas_root.create_oval(x, y, x, y))
    canvas_root.bind("<Motion>", draw_circle)
    canvas_root.bind("<Button-3>", append_circle_click_end)

def draw_circle(event):
    x = event.x
    y = event.y
    x_center, y_center = arr_circle_coord[-1][:2]
    radius = sqrt((x_center - x)*(x_center - x) + (y_center - y)*(y_center - y))
    arr_circle_coord[-1][2] = radius
    circle = canvas_root.create_oval(x_center - radius, y_center - radius,
                                     x_center + radius, y_center + radius)
    canvas_root.delete(arr_circle[-1])
    arr_circle[-1] = circle

def append_circle_click_end(event):
    canvas_root.bind("<Motion>", lambda event: 1+1)
    canvas_root.bind("<Button-3>", append_circle_click_start)

def append_circle(event):
    x, y = list(map(int, field_center.get().split()))
    radius = int(field_radius.get())
    arr_circle_coord.append([x, y, radius])
    circle = canvas_root.create_oval(x - radius, y - radius,
                                     x + radius, y + radius)
    arr_circle.append(circle)

def append_point_click(event):
    x = event.x
    y = event.y
    if [x, y] not in arr_points_coord:
        arr_points_coord.append([x, y])
        arr_points.append(canvas_root.create_rectangle(x - 1, y - 1,
                                                       x + 1, y + 1,
                                                       fill = 'black'))

def append_point(event):
    x, y = list(map(int, field_point.get().split()))
    arr_points_coord.append([x, y])
    point = canvas_root.create_rectangle(x - 1, y - 1, x + 1, y + 1,
                                         fill = 'black')
    arr_points.append(point)

def start_process(event):
    max_circles = 0
    nums_max = [0, 1]
    for i in range(len(arr_points_coord)):
        for j in range(i + 1, len(arr_points_coord)):
            
            a = arr_points_coord[i][1] - arr_points_coord[j][1]
            b = arr_points_coord[j][0] - arr_points_coord[i][0]
            c = (arr_points_coord[i][0] * arr_points_coord[j][1] -
                 arr_points_coord[j][0] * arr_points_coord[i][1])
            circles = 0
            for k in range(len(arr_circle_coord)):
                x, y, radius = arr_circle_coord[k]
                s = abs((a * x + b * y + c) / sqrt(a*a + b*b))
                if s - radius < 1e-5:
                    circles += 1
            if circles > max_circles:
                max_circles = circles
                nums_max = [i, j]
    global line
    x_max_first, y_max_first = arr_points_coord[nums_max[0]]
    x_max_sec, y_max_sec = arr_points_coord[nums_max[1]]
    a = y_max_first - y_max_sec
    b = x_max_sec - x_max_first
    c = x_max_first * y_max_sec - x_max_sec * y_max_first
    if b:
        x_first = -10
        y_first = -(a * x_first + c) / b
        x_sec = 700
        y_sec = -(a * x_sec + c) / b
    else:
        x_first = -c / a
        y_first = -10
        x_sec = x_first
        y_sec = 700
    print(x_first, y_first, x_sec, y_sec)
    line = canvas_root.create_line(x_first, y_first, x_sec, y_sec,
                                   fill = "black")


# Создание главного окна приложения
root = Tk()
root.title('Защита')
root.geometry('600x600')
root.resizable(width = False, height = False)

# Объявление виджетов
label_center = Label(root, text = 'Координаты центра окружности:',
                     font=("Times New Roman", 12))
field_center = Entry(root, font=("Times New Roman", 12))
label_radius = Label(root, text = 'Радиус окружности:',
                     font=("Times New Roman", 12))
field_radius = Entry(root, font=("Times New Roman", 12))

button_append_circle = Button(root, text = 'Добавить окружность',
                              font=("Times New Roman", 12))

label_point = Label(root, text = 'Координаты точки:',
                     font=("Times New Roman", 12))
field_point = Entry(root, font=("Times New Roman", 12))
button_append_point = Button(root, text = 'Добавить точку',
                            font=("Times New Roman", 12))

button_line = Button(root, text = 'Найти прямую',
                     font=("Times New Roman", 12))

canvas_root = Canvas(root, width = 600, height = 450, bg='white')

button_clean = Button(root, text = 'Очистить поле',
                     font=("Times New Roman", 12))

arr_circle = []
arr_points = []
line = 0

# Размещение виджетов
label_center.place(x = 10, y = 10)
field_center.place(x = 250, y = 10, width = 100, height = 25)
label_radius.place(x = 10, y = 40)
field_radius.place(x = 250, y = 40, width = 100, height = 25)
button_append_circle.place(x = 370, y = 17, width = 150, height = 40)
label_point.place(x = 10, y = 70)
field_point.place(x = 250, y = 70, width = 100, height = 25)
button_append_point.place(x = 370, y = 70, width = 150, height = 25)
button_line.place(x = 10, y = 100, width = 130, height = 40)
button_clean.place(x = 150, y = 100, width = 130, height = 40)
canvas_root.place(x = 0, y = 150)

# Привязка виджетов к событиям
button_append_circle.bind("<Button-1>", append_circle)
button_append_point.bind("<Button-1>", append_point)
button_line.bind("<Button-1>", start_process)
button_clean.bind("<Button-1>", clean_canvas)
canvas_root.bind("<Button-1>", append_point_click)
canvas_root.bind("<Button-3>", append_circle_click_start)

arr_points_coord = []
arr_circle_coord = []

root.mainloop()
