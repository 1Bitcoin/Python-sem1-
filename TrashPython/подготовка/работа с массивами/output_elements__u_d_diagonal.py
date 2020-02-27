from random import randint
'''
вывод элементов на главной диагонали и под ней

вывод элементов на главной диагонали и над ней
'''

N = 5

a = [[randint(0, 9) for j in range(N)] for i in range(N)]

print('исходная матрица')
for row in a:
    print(row)

for i in range(N):
    for j in range(0, i+1):
        print('{:<5}'.format(a[i][j]), end='')
    print()
print()

for i in range(N):
    print(end=' '*5*i)
    for j in range(i, N):
        print('{:<5}'.format(a[i][j]), end='')
    print()
print()
