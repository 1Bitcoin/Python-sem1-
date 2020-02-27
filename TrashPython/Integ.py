# Интегрирование м-м средних прямоугольников
# Интегрирование м-м "3/8"

from math import sin, cos
#from check import check

def y(x):
    return sin(x)

def IntRec(a, b, n):
    h = (b - a)/n
    s = 0
    x1 = a
    x2 = a + h
    for i in range(n):
        s += y((x1 + x2)/2)*h
        x1 += h
        x2 += h
    return s

def Int3(a, b, n):
    sm1 = 0
    sm2 = 0
    h = (b - a)/n
    x1 = a
    for i in range(1, n):
        if i % 3:
            sm2 += y(x1)
            x1 += h
        else:
            sm1 += y(x1)
            x1 += h
    s = 3*h*(y(a) + y(b) + 3*sm2 + 2*sm1)/8
    return s

tableTop =  '┌' + '─'*20 + '┬' + '─'*20 + '┬' + '─'*20 + '┐'
tableMid =  '├' + '─'*20 + '┼' + '─'*20 + '┼' + '─'*20 + '┤'
tableBot =  '└' + '─'*20 + '┴' + '─'*20 + '┴' + '─'*20 + '┘' 
metod = '{:^20}'
metodArg =  '{:^6g}'
razb = '{:^20}'
razbArg =  'n{0} = {1}'
znach = '{:.10g}'

a, b = map(int, input('Введите отрезок интегрирования: ').split())
n1, n2 = map(int, input('Введите кол-во разбиений: ').split())
eps = float(input('Введите точность: '))

absInt = cos(a) - cos(b)
res1_1 = IntRec(a, b, n1)
res1_2 = IntRec(a, b, n2)
res2_1 = Int3(a, b, n1)
res2_2 = Int3(a, b, n2)

print(tableTop)
print('│'+ metod.format('Метод/разбиение') + '│' + razb.format(razbArg.format(1, n1))
      + '│' + razb.format(razbArg.format(2, n2)) + '│')
print(tableMid)
print('│'+ metod.format('Средние прям-ки') + '│' + razb.format(znach.format(res1_1))
      + '│' + razb.format(znach.format(res1_2)) + '│')
print(tableMid)
print('│'+ metod.format('3/8') + '│' + razb.format(znach.format(res2_1))
      + '│' + razb.format(znach.format(res2_2)) + '│')
print(tableBot)

print()

if(abs(absInt - res1_1) > abs(absInt - res2_1)):
    n = 1
    sOld = 0
    sNew = IntRec(a,b,n)
    while abs(sOld - sNew) > eps:
        n *= 10
        sOld = sNew
        sNew = IntRec(a,b,n)
else:
    n = 1
    sOld = 0
    sNew = Int3(a,b,n)
    while abs(sOld - sNew) > eps:
        n *= 10
        sOld = sNew
        sNew = Int3(a,b,n) 

print('Точное значение интеграла функции:', '{:.10g}'.format(absInt))
print()
print('Абсолютная погрешность, м-м средних прям-ов, разбиение = {}: '.format(n1), '{:.10g}'.format((res1_1 - absInt)))
print('Абсолютная погрешность, м. левых прям-ков, разбиение = {}: '.format(n2), '{:.10g}'.format(abs(res1_2 - absInt)))
print('Абсолютная погрешность, м-м 3/8, разбиение = {}: '.format(n1), '{:.10g}'.format(abs(res2_1 - absInt)))
print('Абсолютная погрешность, м-м 3/8, разбиение = {}: '.format(n2), '{:.10g}'.format(abs(res2_2 - absInt)))
print()
print('Интеграл, вычисленный с указанной точностью: ', '{:.10g}'.format(sNew))
print('Абсолютная погрешность: ', '{:.10g}'.format(abs(absInt-sNew)))
if absInt != 0:
    print('Относительная погрешность: ', '{:.10g}'.format(abs(absInt-sNew)/absInt))
else:
    print('Невозможно вычислить относительную погрешность')
