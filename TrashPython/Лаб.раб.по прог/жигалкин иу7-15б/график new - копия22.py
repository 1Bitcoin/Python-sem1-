# Программа для построения графика функции и вывода таблицы значений функций.
# Жигалкин Дима ИУ7-15Б

x = float(input('Введите начальное значение x: '))
xk = float(input('Введите конечное значение xk: '))
step = float(input('Введите шаг: '))


# Проверка ввода.
if xk < x and step > 0:
    print('Неверные исходные данные')
else:
    
    from math import pi, sin, ceil
    
    xcop = x
    ymin = ymax = x ** 2 - sin(pi * x)
    

          

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
    while xcop <= xk:
        
        y2 = xcop ** 2 - sin(pi * xcop)
        m = round(((y2 - ymin) / (ymax - ymin)) * 70)
        if (ymax > 0 and ymin < 0):
            
            if(y2 < 0):
                st = ' '*(m * round((abs(ymin) - abs(ymin - y2)))) + '|' + ' ' + \
                     ' '*(m * round(abs(ymin - y2))) + '*' 
                print('{:^8.2g}'.format(xcop), st)
            else:
                
                st = round(ymin * m)*' ' + ' ' + '|' + ' '*m  + '*'
                print('{:^8.2g}'.format(xcop), st) 
        else:
            
            
            st = ' ' * m + '*'
            print('{:^8.2g}'.format(xcop), st)
            
        xcop = xcop + step
    
