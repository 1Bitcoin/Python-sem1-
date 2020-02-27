from math import cos

from iu7_basemodule import easy_check


def f(x):
    pass


# Интеграл через первообразную
def primitive(x, y):
    c = -cos(x)+cos(y)
    return c


# Интеграл без точности
def integral(x, y, n):
    result = 0
    step = (y - x) / n
    for i in range(n):
        c = x + step * (i + 0.5)
        result += f(c)
    result *= step
    return result


# Интеграл с точностью до эпсилона
def right_rectangle_method(x, y, n):
    result = 0
    step = (y - x) / n
    for i in range(n):
        if abs(integral(a, b, 2 * n) - integral(a, b, n)) < eps:
            c =
            result += f(c)
        result *= step
    return result


# Метод трех восьмых
def three_eighths_method(x, y, n):
    m = 3 * n - 1
    step = (y - x) / (3 * n)
    result = f(x) + f(y)
    for i in range(1, m):
        t = a + step * i
        if i % 3 == 0:
            result = result + 2 * f(t)
        else:
            result = result + 3 * f(t)
    result = 3 * result * step / 8
    return result


a = easy_check(input('Введите начальное значение: '))
b = easy_check(input('Введите конечное значение: '))
n1 = int(easy_check(input('Введите первое количество участков разбиения: ')))
n2 = int(easy_check(input('Введиет второе количество участков разбиения: ')))
eps = easy_check(input('Введите значение точности: '))


print(a, b, n1, n2, eps)
print(primitive(a, b))
