# Программа вычисляет данный интеграл способом трапеций
# и левых прямоугольников на отрезке [a,b].
# Также, для наименее точного из этих двух методов производится вычисление интеграла
# с заданной точностью eps, высчитывается относительная и абсолютная ошибка.
# Жигалкин Дима. ИУ7-15Б

from math import exp
from sys import exit

def trapec(f, a, b, n):
    h = float(b - a)/n
    result = 0.5*(f(a) + f(b))
    for i in range(1, n):
	    result += f(a + i*h)
    result *= h
    return result
    
def triangle(f, a, b, n):
    total = 0
    h = float(b - a)/n
    for k in range(0, n):
        total += f(a + k*h)  
    result = h * total
    return result

def perv(g, a, b):
    Itoch = g(b)-g(a)
    return Itoch

try:
    eps = float(input('Введите точность: '))
    print('Ввод отрезка интегрирования')
    a, b = map(int, input('Задайте точки отрезка [a,b]: ').split())
    n1, n2 = map(int, input('Количество итераций n1 и n2: ').split())
except ValueError:
    print('Try again')
    exit()
if a > b:
    print('Try again')
    exit()

f = lambda x: (x+4)
g = lambda x: x**2/2+4*x # Первообразная.

# Интегралы при заданных условием n.
I1 = trapec(f, a, b, n1)
I2 = trapec(f, a, b, n2)

V1 = triangle(f, a, b, n1)
V2 = triangle(f, a, b, n2)

s1='\u250C'   # Символы unicode, необходимые для рисования таблицы.
s2='\u2500'
s3='\u252C'
s4='\u2510'
s5='\u2502'
s6='\u251C'
s7='\u2534'
s8='\u2524'
s9='\u2514'
s10='\u2518'

razb =  'n{0} = {1}'

# Вывод и заполнение таблицы.
print(s1+17*s2+s3+15*s2+s3+15*s2+s4)               
print(s5+'{:^8}'.format('Метод')+'         '+s5+'{:^15}'.format(razb.format(1,n1))+s5+\
      '{:^15}'.format(razb.format(2,n2))+s5)

print(s6+17*s2+s7+15*s2+s7+15*s2+s8)
    
print(s5,'{:^8}'.format('Трапеции'),'{:>20.7f}'.format(I1),\
      '{:>15.7f}'.format(I2)+'   '+s5)
print(s5,'{:^8}'.format('Левых прямоуг.'),'{:>14.7f}'.format(V1),\
      '{:>15.7f}'.format(V2)+'   '+s5)
print(s9+49*s2+s10)

# Считаем с заданной точностью.
if abs(perv(g, a, b) - I1) > abs(perv(g, a, b) - V1):
    nx = 1
    a11 = trapec(f, a, b, nx)
    nx *= 2
    a22 = trapec(f, a, b, nx)

    while abs(a11 - a22) > eps:
        a11 = a22
        nx *= 2
        a22 = triangle(f, a, b, nx)
        
    absolute_error = abs(perv(g, a, b) - a22)
    otnos_error = (absolute_error * 100/perv(g, a, b))
    print('Менее точный метод: трапеций')
    print("Значение интеграла, вычисленное с заданной точностью eps: ", '{:>1.7f}'.format(a22))
    print('Абсолютная ошибка: ', '{:>1.7f}'.format(absolute_error))
    print('Относительная ошибка: ','{:>1.4f}'.format(otnos_error),'%')
else:
    n = 1
    a1 = triangle(f, a, b, n)
    n *= 2
    a2 = triangle(f, a, b, n)

    while abs(a1 - a2) > eps:
        a1 = a2
        n *= 2
        a2 = triangle(f, a, b, n)
        
    absolute_error = abs(perv(g, a, b) - a2)
    otnos_error = (absolute_error * 100/perv(g, a, b))
    print('Менее точный метод: левых прямоугольников')
    print("Значение интеграла, вычисленное с заданной точностью eps: ", '{:>1.7f}'.format(a2))
    print('Абсолютная ошибка: ', '{:>1.7f}'.format(absolute_error))
    print('Относительная ошибка: ','{:>1.7f}'.format(otnos_error),'%')
    



