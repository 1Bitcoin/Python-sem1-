eps = float(input('Введите точность: '))
k = int(input('Введите количество итераций: '))

print()

print('{:^15}'.format('Номер итерации') + '{:^25}'.format('Текущий член ряда') \
      + '{:^25}'.format('Текущее значение суммы'))
print()

y = 0
t = 1
n = 0
while (abs(t) > eps) and (n < k):
    t = 4 * ((-1) ** n) * (1/(2 * n + 1))
    n = n + 1
    y = y + t
    print('{:^15}'.format(n) + '{:^25.8g}'.format(t) \
          + '{:^25.8g}'.format(y))


