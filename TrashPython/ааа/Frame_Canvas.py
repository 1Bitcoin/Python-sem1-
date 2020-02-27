import tkinter as tk
import numpy as np
from logic import Point, Line, seach_points


class Frame_Canvas(tk.Canvas):
    def __init__(self, parent, handler_change_sets, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.decor_handler_change_sets(handler_change_sets)

        self.set_points = set()
        self.set_lines = set()


        self.points = dict()
        self.lines = dict()

        self.line_answer = None

        self.radius_point = 2
        self.width_straight = 2


    def create_straight(self, line, **kwargs):
        k = line.k
        b = line.b

        if k != 'inf':
            x = np.arange(0, self.winfo_width(), 1)

            y = k*x + b

            temp_x = []
            temp_y = []
            for i in range(len(y)):
                if 0 <= y[i] <= self.winfo_height():
                    temp_x.append(x[i])
                    temp_y.append(y[i])
            x, y = temp_x, temp_y

            if len(x) < 2 and len(y) < 2:
                return

            p1 = Point(x[0], y[0])
            p2 = Point(x[-1], y[-1])

        else:
            p1 = Point(b, 0)
            p2 = Point(b, self.winfo_height())

        return self.create_line(p1.x, p1.y, p2.x, p2.y, **kwargs)

    def create_point(self, x, y, **kwargs):
        return self.create_rectangle(
            x - self.radius_point,
            y - self.radius_point,
            x + self.radius_point,
            y + self.radius_point,
            **kwargs
        )

    '''
    def add_line(self, new_line, redraw=False, **kwargs):
        if not redraw:
            self.clear_answer()

        if new_line not in self.set_lines:
            self.set_lines.add(new_line)
            self.handler_change_sets()

        self.lines[new_line] = self.create_straight(
            new_line,
            width=self.width_straight,
            tag='line',
            **kwargs
        )
        '''

    def add_point(self, new_point):
        # self.handler_get_answer()
        self.clear_answer()

        self.redraw()

        self.set_points.add(new_point)
        self.handler_change_sets()

        self.points[new_point] = self.create_point(
            new_point.x, new_point.y, fill='black')

    def add_circle(self, data, redraw=False, **kwargs):
        if not redraw:
            self.clear_answer()

        if data not in self.set_lines:
            self.set_lines.add(data)
            self.handler_change_sets()
        
        p, r = data

        self.create_oval(p.x - r, p.y - r, p.x + r, p.y + r, tag='circle')
        



    def redraw(self, event=None):
        self.clear_lines()

        for data in self.set_lines:
            p, r = data
            self.create_oval(p.x - r, p.y - r, p.x + r, p.y + r, tag='circle')

        self.draw_answer(self.line_answer)


    def draw_answer(self, answer):
        if answer:
            self.clear_answer()
            self.line_answer = answer

            self.create_straight(answer, tag='answer', fill='red', width=self.width_straight)


    def decor_handler_change_sets(self, handler):
        self.handler_change_sets = lambda: handler(
            self.set_points, self.set_lines, self.line_answer)


    def get_answer(self):
        data = self._get_ans()
        self.draw_answer(data)
        self.line_answer = data
    

    def clear_lines(self):
        self.delete('circle')


    def clear_answer(self):
        if self.line_answer:
            self.delete('answer')
            self.line_answer = None

        
    def clear(self):
        self.set_lines = set()
        self.set_points = set()
        self.handler_change_sets()
        self.delete(tk.ALL)


    def _get_ans(self):
        temp = seach_points(self.set_points, self.set_lines)
        if temp:
            return Line(temp[0], temp[1])
        else:
            return None


if __name__ == "__main__":
    root = tk.Tk()

    t = Frame_Canvas(root, lambda a, b, c: print(a, b, c, sep='\n'))
    t.pack(expand=True, fill=tk.BOTH)

    tk.Button(root, command=lambda: t.get_answer()).pack()

    t.bind("<Button-2>", lambda x: t.clear())

    root.mainloop()
