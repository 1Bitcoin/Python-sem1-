import numpy as np
from itertools import combinations

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.x == other.x and self.y == other.y

    
    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'Point({self.x}, {self.y})'


class Line():
    ''' Ax + By + C = 0 '''
    def __init__(self, point_a: Point, point_b: Point):
        self.A = point_a.y - point_b.y
        self.B = point_b.x - point_a.x
        self.C = point_a.x * point_b.y - point_b.x * point_a.y

        self.k = self._getK()

        self.b = self._getB()
    
    def is_parallel(self, other):
        if type(self) != type(other):
            return False
        return self.k == other.k
    
    def _getK(self):
        k = 'inf'
        if self.B:
            k = - self.A / self.B
        return k
    
    def _getB(self):
        if self.B:
            return - self.C / self.B
        else:
            return -self.C / self.A

    def __eq__(self, other):
        return (self.k == other.k and
                self.b == other.b)

    def __hash__(self):
        return hash((self.k, self.b))


    def __repr__(self):
        return f'Line {self.A}x + {self.B}y + {self.C} = 0'

    def __str__(self):
        return f'{self.A:+}x{self.B:+}y{self.C:+} = 0'

'''
def create_data(setB):
    dict_data = dict()
    for data in setB:
        key = line.k

        if key in dict_data:
            dict_data[key] += 1
        else:
            dict_data[key] = 1
    return dict_data
'''

def seach_points(setA, setB):
    # dict_data = create_data(setB)
    max_count = 0
    answer_points = []

    max_count = 0

    for points in combinations(setA, 2):
        line  = Line(points[0], points[1])

        count = 0
        k = line.k
        if k == 'inf':
            for data in setB:
                center, r = data
                if (line.b - center.x)**2 < r**2:
                    count += 1
        else:
            for data in setB:
                center, r = data
                c = (line.b - center.y)
                if (c * k - center.x)**2 - (1+k **2) * (center.x**2 + c**2 - r**2) > 0:
                    count += 1

        if count > max_count:
            max_count = count
            answer_points = points
    return answer_points

 
