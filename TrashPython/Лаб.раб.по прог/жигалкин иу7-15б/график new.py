# Программа для построения графика функции и вывода таблицы значений функций.
# Жигалкин Дима ИУ7-15Б

x = float(input('Введите начальное значение x: '))
xk = float(input('Введите конечное значение xk: '))
step = float(input('Введите шаг: '))


# Проверка ввода.
if xk < x and step > 0:
    print('Неверные исходные данные')
else:
    
    from math import pi, sin
    
    xcop = x
    ymin = ymax = x ** 3 - 6.5 * x ** 2 - 31.3 * x + 2.32
    

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
        if y1 > ymax:
            ymax = y1
        if y1 < ymin:
            ymin = y1
        x = x + step

    # Строим вертикальную линию, если есть пересечение оси х.
                                                         
    if ymin <= 0 and ymax >= 0:
        m0 = round((y1-ymin)/(ymax-ymin) * 70)
        line = ' ' * m0 + '*'  + '|'
        

    # Выводим график функции.
    print()
    print('{:^8}'.format('x'), '{:<2.4g}'.format(ymin), '{:^85.4g}'.format(ymax))
    while xcop <= xk:
        y1 = xcop ** 3 - 6.5 * xcop ** 2 - 31.3 * xcop + 2.32
        m = round((y1 - ymin)/(ymax - ymin) * 70)
        if ymin <= 0 and ymax >= 0:
            print('{:^8.2g}'.format(xcop),line, ' ' * m + '*')
        else:
            print('{:^8.2g}'.format(xcop), ' ' * m + '*')
        xcop = xcop + step
