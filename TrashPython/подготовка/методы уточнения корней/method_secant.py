from math import cos, atan, sin
'''
метод секщих
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

x0 = 1
x1 = 3

eps = 1e-7

x2 = x0
while not (abs(f(x2)) < eps):
    x2, x1, x0 = x1 - f(x1) * (x1-x0)/(f(x1)-f(x0)), x2, x1
print('ans = {:.9f}'.format(x2))
