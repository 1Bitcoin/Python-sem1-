eps = float(input('Введите точность: '))
step = float(input('Введите шаг: '))
x = float(input('Введите значение x: '))
r = int(input('Введите кол-во итераций: '))

from math import factorial

n = 0

# Строим таблицу.
print('{:^8}'.format('№ итерации') + '{:^15}'.format('t') + \
          '{:^25}'.format('S'))

i = 1
t = (-(2 * x) ** (2 * i)) / (factorial(2 * i))
y = 0

for i in range(1, r + 1):
    if abs(t) > eps:
        n = n + 1
        t = (-(2 * x) ** (2 * i)) / (factorial(2 * i))
        y = y + t
        
        print('{:^8.2g}'.format(i), '{:^2}'.format('|'), '{:^15.2g}'.format(t),\
          '{:^8}'.format('|'), '{:^10.2g}'.format(y))
    else:
        print('Сумма ряда за указанное число итерация не может быть вычислена')
        break
    
    



