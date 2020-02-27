# x*x - 36 0x
x = float(input('Введите начальное значение x: '))
xk = float(input('Введите конечное значение xk: '))
step = float(input('Введите шаг: '))   

xcop = x
ymin = ymax = x ** 2 - 36

while x <= xk:
    y1 = x * x -36
    if y1 > ymax:
        ymax = y1
    if y1 < ymin:
        ymin = y1
            
    x += step

print()

while xcop <= xk:
    
    m = round((xcop ** 2 - 36 - ymin) / (ymax - ymin) * 70)
    
    print('{:8g}'.format(round(xcop, 10)), sep='',end=' ')
    
    i = 0
    
    if round(xcop, 10) != 0:
        while i <= 70:
            if i == m:
                print('*', end = '')
            elif i == round((-ymin) / (ymax - ymin) * 70):
                print('|', end = '')
            else:
                print(' ', end=  '')
            i += 1
    else:
        
        while i <= 70:
            if i == m:
                print('*', end = '')
            elif i == round((-ymin) / (ymax - ymin) * 70):
                print('|', end = '')
            else:
                print('-', end = '')
            i += 1
            
    print(sep='')
    xcop += step
    
        
    
