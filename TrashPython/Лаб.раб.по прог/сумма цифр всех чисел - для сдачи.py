# Программа вычисляет суммы цифр всех положительных чисел массива.
# Жигалкин Дима. ИУ7-15Б.
from sys import exit

a = list(map(int,input('Введите элементы массива:').split()))
d = len(a)
s = 0

if d != 0:
    
    # Перебор всех чисел массива и вычисление суммы цифр.
    for i in range(0, d):
        while a[i] > 0:
            s += a[i] % 10
            a[i] = a[i] // 10
else:
    print('Список пуст!')
    exit()
        
print('Сумма цифр всех чисел: ', s)

