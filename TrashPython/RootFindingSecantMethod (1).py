'''
Program finds roots of the equation with the given accuracy on the segment

Every root is found with the Secant Method and limited with the number of 
iterations

After calculation all the results are put together in a table with the 
counted (where it is possible) and the number of error (where it had stopped 
automatically)

From this range of points the graph of function will be built
(with the extremum's)
'''
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

from numpy import arange
from math import pow, cos, sin, pi
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview


# Parameters
root_height = '400'
root_width = '800'

# Colors
#48b8f0 - blue/main
#0d13a8 - darker blue/outline
#f0f030 - yellow/additional/processing
#4ac23a - green/ready
bg_color = 'white'

# Root window and frames settings
root = Tk()
root.geometry(root_width + 'x' + root_height)
root.title('Secant method of root finding')
root.resizable(width = False, height = False)
root.configure(bg =  bg_color)

inputFrame = Frame(root, width = int(root_width) // 2,\
height = int(root_height) // 2, bg = bg_color)
inputFrame.pack(side = 'top')

textFrame = Frame(root, width = int(root_width) // 2,
height=int(root_height) // 2, bg = bg_color)
textFrame.pack(side = 'bottom')

# Fonts
font_main = 'Candara 15'

# UI
segment = Entry(inputFrame, font = font_main, bg =  bg_color)
segmentLabel = Label(inputFrame, text = 'Enter segment starting and\
 ending point separated by space', font = font_main, bg =  bg_color)
step = Entry(inputFrame, font = font_main, bg =  bg_color)
stepLabel = Label(inputFrame, text = 'Enter step', font = font_main, bg =  bg_color)
numberOfIterations = Entry(inputFrame, font = font_main, bg =  bg_color)
numberOfIterationsLabel = Label(inputFrame, text = 'Enter number of iterations'
                                , font = font_main, bg =  bg_color)
accuracy = Entry(inputFrame, font = font_main, bg =  bg_color)
accuracyLabel = Label(inputFrame, text = 'Enter accuracy', font = font_main, bg =  bg_color)
button = Button(inputFrame, text = 'Apply', font= font_main)
button2 = Button(inputFrame, text = 'Clear All', font= font_main)

segment.grid(row = 0, column = 1)
segmentLabel.grid(row = 0, column = 0, sticky = 'W')
step.grid(row = 1, column = 1)
stepLabel.grid(row = 1, column = 0, sticky = 'W')
numberOfIterations.grid(row = 2, column = 1)
numberOfIterationsLabel.grid(row = 2, column = 0, sticky = 'W')
accuracy.grid(row = 3, column = 1)
accuracyLabel.grid(row = 3, column = 0, sticky = 'W')
button.grid(row = 4, column = 0, sticky = 'W')
button2.grid(row = 4, column = 1, sticky = 'W')

tv = Treeview(textFrame)
tv['columns'] = ('Segment', 'Found value', 'Function value', 'Number of iterations', 'Error code')
tv.heading("#0", text='Number of root', anchor='w')
tv.column("#0", anchor="w")
tv.heading('Segment', text='Segment')
tv.column('Segment', anchor='center', width=100)
tv.heading('Found value', text='Found value')
tv.column('Found value', anchor='center', width=100)
tv.heading('Function value', text='Function value')
tv.column('Function value', anchor='center', width=100)
tv.heading('Number of iterations', text='Number of iterations')
tv.column('Number of iterations', anchor='center', width=100)
tv.heading('Error code', text='Error code')
tv.column('Error code', anchor='center', width=100)
'''
tv.insert('', 'end', text="First", values=('0', '0', '0'))
'''
tv.grid(sticky = (N,S,W,E))

f = lambda x: sin(x)

def secant(function, a, b, N, eps):
    f0 = function(a)
    f1 = function(b)
    x0 = a
    x1 = b
    counter = 0
    
    while abs(x1- x0) > eps:
        
        if counter > N:
            return '909'
        
        x2 = (x0 * f1 - x1 * f0) / (f1 - f0)
        
        x0, x1 = x1, x2
        f0, f1 = f1, function(x2)
        counter += 1
    
    if x2 < a or x2 > b:
        return '808'     
    return x2, counter

def tableOfRoots(start, stop, step, iternum, eps):
    a = start
    iter = 0
    prev = 0
    for i in range(int((stop - start) / step)):
        try:
            current, iter = secant(f, a, a + step, iternum, eps)
        except:
            current = secant(f, a, a + step, iternum, eps)
        if current == '909' or current == '808':
            tv.insert('', 'end', text = str(i + 1), values=('-', '-', '-', '-', current))
        elif prev == current:
            tv.insert('', 'end', text = str(i + 1), values=('-', '-', '-', '-', '707'))
        else:
            tv.insert('', 'end', text = str(i + 1), values=('[{: 3g} ;{: 3g}]'.format(a, a + step), '{:g}'.format(current), '{: .4e}'.format(f(current)), '{:g}'.format(iter), '-'))
        a += step
        prev = current

def check(event):
    mistake = False
    restrict = ' -0123456789'
    ready = 4

    inside = segment.get()
    if inside != '':
        for char in inside:
            if char not in restrict:
                mistake = True
        try:
            inside = inside.split()
            if len(inside) > 2 or inside[0][0] == '0' or inside[1][0] == '0'\
               or  '-' in inside[0][1:] or  '-' in inside[1][1:] or inside[0] == inside[1]:
                mistake = True
        except:
            mistake = True
    else:
        mistake = True

    if mistake:
        segment.delete(0, END)
        mistake = False
        ready -= 1

    inside = step.get()
    if inside != '':
        for char in inside:
            if char not in (restrict + '.'):
                mistake = True
        if '-' in inside[1:]:
            mistake = True
    else:
        mistake = True

    if mistake:
        step.delete(0, END)
        mistake = False
        ready -= 1

    inside = numberOfIterations.get()
    if inside != '':
        for char in inside:
            if char not in restrict:
                mistake = True
        if inside[0] == '0' or '-' in inside:
            mistake = True
    else:
        mistake = True

    if mistake:
        numberOfIterations.delete(0, END)
        mistake = False
        ready -= 1

    inside = accuracy.get()
    if inside != '':
        for char in inside:
            if char not in (restrict + '.'):
                mistake = True
        if '-' in inside or float(inside) > 1:
            mistake = True
    else:
        mistake = True

    if mistake:
        accuracy.delete(0, END)
        mistake = False
        ready -= 1

    if ready == 4:
        return 1
    else:
        return 0

def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    return l

def findExtremums(function, start, stop, step):
    minX = start
    maxX = start
    x = start + step
    for i in range(int((stop - start) / step)):
        if function(x) < function(minX):
            minX = x
        elif function(x) > function(maxX):
            maxX = x
        x += step
    return minX, maxX
    
def drawGraph(event):
        plt.close("all")
        # Graph properties
        if check("<Button-1>"):
            base = [float(x) for x in segment.get().split()]
            xmin, xmax = base[0], base[1]
            dx = float(accuracy.get())
            ddx = float(step.get())
                
            xList = arange(xmin, xmax, dx)
            yList = [f(x) for x in xList]
                
            names = tv.get_children()
            pointsX = []
            pointsY = []       
            for i in names:
                if tv.item(i)["values"][1] != '-':
                    pointsX.append(float(tv.item(i)["values"][1]))
                    pointsY.append(float(tv.item(i)["values"][2]))
                        
            for i in range(len(pointsX)):
                plt.plot(pointsX[i], pointsY[i], 'r', marker = 'o')
            
            minx, maxx = findExtremums(f, xmin, xmax, float(step.get()))
            x = xmin
            cur = 0
                
            for i in range(int((xmax - xmin) / ddx)):
                cur = f(x)
                if cur == f(minx) or cur == f(maxx):
                    plt.plot(x, cur, 'b', marker = 'o')
                x += ddx
                    
                
            plt.plot(xList, yList, 'g')
            newline([xmin, 0], [xmax, 0])
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()

#            messagebox.showwarning('Careful!', 'Data has been changed')
          
def start(event):
    if check("<Button-1>"):
        for i in tv.get_children():
            tv.delete(i)
        
        start, stop = segment.get().split()
        start, stop = float(start), float(stop)
        sh = float(step.get())
        iternum = int(numberOfIterations.get())
        eps = float(accuracy.get())
        
        tableOfRoots(start, stop, sh, iternum, eps)

        button1 = Button(inputFrame, text = 'Show graph', font= font_main)
        button1.grid(row = 4, column = 1, sticky = 'E')
        
        button1.bind("<Button-1>", drawGraph)
    else:
        messagebox.showerror('Error', 'Fields empty')
    
def exit_app():
    root.destroy()
    
def about_program():  
    text = '''
Program finds roots of the equation with the given accuracy on the segment

Every root is found with the Secant Method and limited with the number of 
iterations

After calculation all the results are put together in a table with the 
counted (where it is possible) and the number of error (where it had stopped 
automatically)

From this range of points the graph of function will be built
(with the extremum's)

~~ made with Python module tkinter ~~
'''
    window = Toplevel(root, bg = bg_color)
    info = Label(window, text = text, justify = LEFT, bg = bg_color, font = font_main)
    info.pack()

def about_author():
    text = '''
Evsigneev Timofey
MGTU
IU7-24B, 2019
''' 
    window = Toplevel(root, bg = bg_color)
    info = Label(window, text = text, justify = LEFT, bg = bg_color, font = font_main)
    info.pack()

def error_codes():
    text = '''
707 - more than one root in a segment
808 - left the borders of a local segment
909 - accuracy not reached
''' 
    window = Toplevel(root, bg = bg_color)
    info = Label(window, text = text, justify = LEFT, bg = bg_color, font = font_main)
    info.pack()
    
def clear_all(event):
    try:
        button2.pack_forget()
    except:
        pass
    finally:
        for i in tv.get_children():
                tv.delete(i)
        segment.delete(0, END)
        step.delete(0, END)
        numberOfIterations.delete(0, END)
        accuracy.delete(0, END)
        plt.close("all")

# Binds
segment.bind("<Leave>", check)
step.bind("<Leave>", check)
numberOfIterations.bind("<Leave>", check)
accuracy.bind("<Leave>", check)
segment.bind("<Tab>", check)
step.bind("<Tab>", check)
numberOfIterations.bind("<Tab>", check)
button.bind("<Button-1>", start)
button2.bind("<Button-1>", clear_all)
accuracy.bind("<Tab>", check)

# Menu settings
mainMenu = Menu(root)
root.configure(menu = mainMenu)

first_item = Menu(mainMenu, tearoff = 0) #tearoff - Doesn't allow to tear off commands
mainMenu.add_cascade(label = 'File', menu = first_item)
first_item.add_command(label = 'Exit', command = exit_app)

second_item = Menu(mainMenu, tearoff = 0)
mainMenu.add_cascade(label = 'About', menu = second_item)
second_item.add_command(label = 'Author', command = about_author)
second_item.add_command(label = 'Program', command = about_program)
second_item.add_command(label = 'Error codes', command = error_codes)

root.mainloop()