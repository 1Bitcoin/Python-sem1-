'''
задача сформировать массив размером N*N
пример для  N = 5

1   2   3   4   5
12  13  14  6   6
11  15  7   14  7
10  8   13  15  8
9   12  11  10  9
'''

N = int(input('введите N: '))
a = [[0 for j in range(N)] for i in range(N)]
i, j = 0, 0
c = 1
while a[i][j] == 0:
    while j < N:
        if a[i][j] == 0:
            a[i][j] = c
            c += 1
            j += 1
        else:
            break
    j -= 2
    i += 1
    while i < N and j > -1:
        if a[i][j] == 0:
            a[i][j] = c
            c += 1
            i += 1
            j -= 1
        else:
            break
    j += 1
    i -= 2
    while a[i][j] == 0:
        a[i][j] = c
        c += 1
        i -= 1
    
    j += 1
    i += 1

c = N + 1
i, j = 1, N-1

while a[i][j] == 0:
    while i < N:
        if a[i][j] == 0:
            a[i][j] = c
            c += 1
            i += 1
        else:
            break
    i -= 1
    j -= 1

    while a[i][j] == 0:
        a[i][j] = c
        c += 1
        j -= 1
    j += 2
    i -= 1
    
    while a[i][j] == 0:
        a[i][j] = c
        c += 1
        i -= 1
        j += 1
    j -= 1
    i += 2

for row in a:
    print(''.join(['{:<5}'.format(x) for x in row]))
    
