from random import randint
'''
**удалить побочную диагональ
двумя способами (сдвиг нижней влево, сдвиг нижней вверх)
1)
1 2 3    1 2
4 5 6 -> 4 6
7 8 9    8 9

2)
1 2 3    1 2 6
4 5 6 -> 4 8 9
7 8 9    
'''
def shift_left(m):
    a = [x[:] for x in m]
    for i in range(N):
        for j in range(N-1-i, N-1):
            a[i][j] = a[i][j+1]
        del a[i][N-1]
    return a


def shift_up(m):
    a = [x[:] for x in m]
    for j in range(N):
        for i in range(N-1-j, N-1):
            a[i][j] = a[i+1][j]   
    del a[N-1]
    
    return a

N = 3
m = [[randint(0, 9) for j in range(N)] for i in range(N)]

for row in m:
    print(row)
print()

for row in shift_left(m):
    print(row)
print()

for row in shift_up(m):
    print(row)
