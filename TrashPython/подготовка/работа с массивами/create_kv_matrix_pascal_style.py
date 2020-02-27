'''
создать за 2 цикл кв. матрицу (выше гл. диаг = *, ниже #, на диаг. @)
'''

N = 5

a = [['@']*N for i in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            a[i][j] = '#'
            a[j][i] = '*'

for row in a:
    print(row)
