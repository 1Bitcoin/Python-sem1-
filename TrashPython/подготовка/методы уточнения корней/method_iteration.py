from math import cos, atan, sin
'''
метод итераций
'''

def f(x):
    '''
f(x) = 0
изначальное уравнение
    '''
    return x**k - a

def fi(x):
    '''
преобразованое f(x)
в вид
x = fi(x)
получено добавлением к обеим частям выражения (k-1)x**k
и последующем выражением x
x = x**k - a + x
    '''
    return (a + (k-1)*x**k)/(k*x**(k-1))

# степень √
k = 2.8

# число из которого извлекается корень
a = 2.2

x0 = x1 = 2

eps = 1e-7

while not (abs(f(x1)) < eps):
    x1, x0 = fi(x0), x1
    
print('ans = {:.9f}'.format(x1))
