# Заммена на '#' всех строк и столбцов, где есть цифра.
# Жигалкин Дима. ИУ7-15Б
from sys import exit
L = int(input('Количество строк: ')) #string
M = int(input('Длина строк: ')) #solb

a = [ [ k for k in (input())] for p in range(L)]
for r in a:
    if len(r) != M:
        print('bad')
        exit()



for b in a:
    print(b)
print()
    
for i in range(L):
    for j in range(M):
        if (a[i][j]).isdigit():
            stolb = j
            stroka = i
            for h in range(L):
                if a[h][stolb].isdigit() == False:
                    a[h][stolb] = '#'
            for y in range(M):
                if a[stroka][y].isdigit() == False:
                    a[stroka][y] = '#'
for i in range(L):
    for j in range(M):
        if (a[i][j]).isdigit():
            a[i][j] = '#'



for b in a:
    print(b)
    
