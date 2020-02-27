# Программа вычисляет суммы цифр всех чисел массива.
# Жигалкин Дима. ИУ7-15Б.
from sys import exit

x = list(input('Введите числа массива:').split())
s = 0
for z in x:
    if not z.isdigit():
        print('Надо число')
        exit()
# Перебор всех чисел массива и вычисление суммы.
d = len(x)
for i in range(0, d):
    
    if x[i] > 0:
        
        
       
       
        s = s + int(z % 10)
        z = int(z / 10)
    i = i + 1
print('Сумма цифр всех чисел: ', s)

