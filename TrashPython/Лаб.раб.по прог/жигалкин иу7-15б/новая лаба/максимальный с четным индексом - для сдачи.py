# Программа находит максимальный элемент с четным индексом.
# Жигалкин Дима. ИУ7-15Б.

x = list(map(int,input('Введите целочисленные элементы массива:').split()))
maxel = x[0]
d = len(x)
i = 0

# Проходим по четным индексам и ищем максимальное число среди них.
for i in range(0, d, 2):
    if x[i] > maxel:
        maxel = x[i]  
print('Максимальное число с четным индексом: ', maxel)

size_alpha = '0123456789'
size_arr = [[i for i in range (len(x)) if x in size_alpha]]
if len(x) == len(size_arr):
    x = int(x)
    

