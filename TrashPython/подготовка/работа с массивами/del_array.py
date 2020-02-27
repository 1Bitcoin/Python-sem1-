from random import randint
'''
удаление столбца без del
удаление строки без del
'''

N = randint(2, 10)
M = randint(2, 10)
print('матрица {}x{}'.format(N, M))
a = [[randint(0, 9) for j in range(M)] for i in range(N)]

for row in a:
    print(row)
print()

i_del = randint(0, N-1)

j_del = randint(0, M-1)

print('индекс удаляемой строки:', i_del)

for j in range(M):
    for i in range(i_del, N-1):
        a[i][j] = a[i+1][j]
N -= 1
del a[N]

for row in a:
    print(row)
print()



print('индекс удаляемого столбца:', j_del)
M -= 1
for i in range(N):
    for j in range(j_del, M):
        a[i][j] = a[i][j+1]
    del a[i][M]

for row in a:
    print(row)
print()
