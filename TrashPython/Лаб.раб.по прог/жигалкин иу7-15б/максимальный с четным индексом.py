# Программа находит максимальный элемент с четным индексом.
# Жигалкин Дима. ИУ7-15Б.
from sys import exit

x = input('Введите числа массива:').split()

for z in x:
    if (z.lstrip('-').replace('.','',1).isdigit()) == False:
        print('Надо число')
        exit()
        
maxel = x[0]
d = len(x)
i = 0
# Проходим по четным индексам и ищем максимальное число среди них.
for i in range(0, d, 2):
    
    if x[i] > maxel:
        maxel = x[i]
    

print('Максимальное число с четным индексом: ', maxel)

