'''
задача сформировать массив размером N*N
пример для  N = 5

1    21   22   23   9
15   2    25   10   8
14   16   3    24   7
13   11   17   4    6
12   20   19   18   5
'''

N = 6 # int(input('введите N: '))

a = [[0]*N for i in range(N)]

c = 1
i, j = 0, 0

while i < N and j < N:
    a[i][j] = c
    c += 1
    i += 1
    j += 1

i -= 2
j -= 1

while i > -1:
    a[i][j] = c
    c += 1
    i -= 1
    
i += 2
j -= 1

while i < N and j > -1:
    if i != j:
        a[i][j] = c
        c += 1
    i += 1
    j -= 1

i -= 2
j += 1


h = 0
while a[i][j] == 0:
    while i < N and j > -1:
        if i > j + h:
            a[i][j] = c
            c += 1
            i -= 1
        else:
            break
    i += 2
    j += 1
    while i < N-h:
        if a[i][j] == 0:
            a[i][j] = c
            c += 1
        i += 1
        j += 1
        
    i -= 1
    j -= 2
    while a[i][j] == 0:
        a[i][j] = c
        c += 1
        j -= 1

    i -= 2
    j += 1
    h += 1

i, j = 0, 1
h = 0
while a[i][j] == 0:
    while a[i][j] == 0:
        a[i][j] = c
        c += 1
        j += 1
    i += 2
    j -= 1

    while a[i][j] == 0:
        a[i][j] = c
        c += 1
        i += 1

    i -= 2
    j -= 1
    while i > h:
        if a[i][j] == 0:
            a[i][j] = c
            c += 1
        i -= 1
        j -= 1

    i += 1
    j += 2
    h += 1

for row in a:
    print(''.join(['{:<5}'.format(x) for x in row]))
