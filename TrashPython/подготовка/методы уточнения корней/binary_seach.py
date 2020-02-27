from math import cos, atan, sin
'''
метод половинного деления
'''

def f(x):
    '''
вьетнамский флешбек

нули
x ~ - 11.0011109024118...
x ~ ± 7.86499587471730...
x ~ ± 4.74359618362999...
x ~ ± 1.79103397776014...
x = 0
    '''
    return cos(x) * atan(x)+ sin(x)/(1+x**2)


a = 1
b = 3

eps = 1e-7
m = (a+b)/2
while not (abs(f(m)) < eps):
    m = (a+b)/2
    if f(a)*f(m) < 0:
        b = m
    else:
        a = m
print('ans = {:.6f}'.format(m))
