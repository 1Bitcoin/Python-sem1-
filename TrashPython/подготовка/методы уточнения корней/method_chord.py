from math import cos, atan, sin
'''
метод хорд
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


x0 = x1 = 2
b = 5

fb = f(b)

eps = 1e-7

while not (abs(f(x1)) < eps):
    t = x1
    x1 = x0 - f(x0)*(b-x0)/(fb-f(x0))
    x0 = t
    
print('ans = {:.9f}'.format(x1))
