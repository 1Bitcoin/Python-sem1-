from random import randint
'''
транспонирование матрицы
'''

N = randint(2, 10)
M = randint(2, 10)
print('матрица {}x{}'.format(N, M))
a = [[randint(0, 9) for j in range(M)] for i in range(N)]

for row in a:
    print(row)
print()

at = [[0]*N for i in range(M)]

for i in range(N):
    for j in range(M):
        at[j][i] = a[i][j]

for row in at:
    print(row)
print()
