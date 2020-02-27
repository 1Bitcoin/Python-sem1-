# Программа для удаления строк с первым символом, отличным от маленькой латин.
# буквы и их сортировка по первой букве по алфавиту.
# Жигалкин Дима ИУ7-15
from sys import exit

# Удаление строки
def dell(matr):
    srt = []
    for x in matr:
        if 'a' <= x[0] <= 'z':
            srt.append(x)
    bubble(srt)
    return srt

# Cортируем строки
def bubble(a):
    n = len(a)
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            if a[i][0] < a[j][0]:
                a[i], a[j] = a[j], a[i]
                
d1 = int(input('Введите длину строки '))
d2 = int(input('Введите количество строк '))

matr = []
for i in range(d2):
    matr.append(input())
    if len(matr[i]) != d1:
        print('bad')
        exit()

for r in matr:
    print(r)
print()

for r in dell(matr):
    print(r)
print()

