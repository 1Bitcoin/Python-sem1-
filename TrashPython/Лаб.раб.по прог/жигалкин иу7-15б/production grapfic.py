# Программа для построения графика функции и вывода таблицы значений функций.
# Жигалкин Дима. ИУ7-15Б.
from math import pi, sin
    
x = float(input('Введите начальное значение x: '))
xk = float(input('Введите конечное значение xk: '))
step = float(input('Введите шаг: '))   

xcop = x
ymin = ymax = x ** 2 - sin(pi * x)

# Строим таблицу.
print('{:^8}'.format('x') + '{:^15}'.format('y1') + \
          '{:^25}'.format('y2') + '{:^15}'.format('y3'))

# Заполянем таблицу.
while x <= xk: 
    y1 = x ** 3 - 6.5 * x ** 2 - 31.3 * x + 2.32
    y2 = x ** 2 - sin(pi * x)
    y3 = y1 ** 2 - y2 ** 2
    
    print('{:^8.2g}'.format(x), '{:^2}'.format('|'), '{:<11.2g}'.format(y1),\
          '{:^8}'.format('|'), '{:<8.2g}'.format(y2), '{:^8}'.format('|'), \
          '{:<8.2g}'.format(y3))
        
    # Ищем максимальное и минимальное значения ф-ции.
    if y2 > ymax:
        ymax = y2
    if y2 < ymin:
        ymin = y2
            
    x = x + step

# Строим график и линию.
print()
print('        {:8g} {:>60}'.format(ymin, ymax))
print()
while xcop <= xk:
    
    m = round((xcop ** 2 - sin(pi * xcop) - ymin) / (ymax - ymin) * 70)
    
    print('{:8g}'.format(round(xcop, 10)), sep='',end=' ')
    
    i = 0
    
    if round(xcop, 10) != 0:
        while i <= 70:
            if i == m:
                print('*', end = '')
            elif i == round((-ymin) / (ymax-ymin) * 70):
                print('|', end = '')
            else:
                print(' ', end=  '')
            i += 1
    else:
        
        while i <= 70:
            if i == m:
                print('*', end = '')
            elif i == round((-ymin) / (ymax-ymin) * 70):
                print('|', end = '')
            else:
                print('-', end = '')
            i += 1
            
    print(sep='')
    xcop += step
    
