# Жигалкин Дима. ИУ7-15Б
# Данная программа предназначена для вычисления суммы бесконечного ряда с
# точностью eps. Также, она строит таблицу значений с заданным шагом.

eps = float(input('Введите точность: '))
step = int(input('Введите шаг: '))
x = float(input('Введите значение x: '))
r = int(input('Введите кол-во итераций: '))
t_list = []
y_list = []
n_list = []
print()

from math import factorial

# Строим таблицу.
print('{:^15}'.format('Номер итерации') + '{:^25}'.format('Текущий член ряда') \
      + '{:^25}'.format('Текущее значение суммы'))
print()

n = 0
t = 1
y = 0

while n < r and abs(t) > eps:
        n = n + 1
        n_list.append(n)
        t = (((-1) ** n)*(2 * x) ** (2 * n)) / (factorial(2 * n))
        t_list.append(t)
        y += t
        y_list.append(y)

for i in range(0, len(n_list), step):
    
    
    print('{:^15.7g}'.format(i + 1), '{:^2}'.format('|'), '{:^15.7g}'.format(t_list[i]),\
        '{:^8}'.format('|'), '{:^10.7g}'.format(y_list[i]))

# Выводим причину, по которой цикл окончил работу.
if n >= r:                                         
    print('Привышено максимальное число итераций')
elif abs(t)<=eps:
    print('Ряд сошелся')
