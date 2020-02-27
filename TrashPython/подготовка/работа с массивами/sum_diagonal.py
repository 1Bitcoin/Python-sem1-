from random import randint
'''
дана целочисленнная квадратная матрица
требуется определить номер диагонали паралельной
побочной диагонали на которой abs отрицательных
элементов максимально.
после удалить строку с наибольшим количеством нулевых элементов

*нумерация диагоналей
1 2 3
0 0 4
0 0 5
'''

def sum_d(i, j):
    s = -1
    while i < N and j > -1:
        if a[i][j] < 0:
            s -= a[i][j]
        i += 1
        j -= 1
    return s

N = 5
a = [[randint(-9, 9) for j in range(N)] for i in range(N)]

max_sum = 0
ans = -1
i_del = -1
max_count_zero = 0
for j in range(N-1):
    s = sum_d(0, j)
    if s > max_sum:
        ans = j+1
        max_sum = s

for i in range(N):
    s = sum_d(i, N-1)
    if s > max_sum:
        ans = N + i
        max_sum = s
    c = 0
    for j in range(N):
        if a[i][j] == 0:
            c += 1
    if c > max_count_zero:
        max_count_zero = c
        i_del = i

if ans > -1:
    print('номер диагонали =', ans)
else:
    print('нет отрицательных элементов!')
print()

for row in a:
    print(''.join(['{:< 5}'.format(x) for x in row]))
print()

if i_del == -1:
    print('нет нулевых элементов')
else:
    for j in range(N):
        for i in range(i_del, N-1):
            a[i][j] = a[i+1][j]
    del a[N-1]
    
    for row in a:
        print(''.join(['{:< 5}'.format(x) for x in row]))
