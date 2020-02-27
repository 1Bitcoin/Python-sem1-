# Программа находит максимальный элемент с четным индексом.
# Жигалкин Дима. ИУ7-15Б.
from sys import exit

x = input('Введите числа массива:').split()

for z in x:
    if (z.lstrip('-').replace('.','').isdigit()) == False:
        print('Плохой ввод')
        exit()
        
d = len(x)

if d !=0:
    # Проходим по четным индексам и ищем максимальное число среди них.
    maxel = x[0]
    for i in range(0, d, 2):
        if x[i] > maxel:
            maxel = x[i]
else:
    print('Список пуст')
    exit()
print('Максимальное число с четным индексом: ', maxel)

