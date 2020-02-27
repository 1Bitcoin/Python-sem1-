import random
from sys import exit
# Заводим матрицу и выводим ее.
n = int(input('размер матрицы '))
if n == 1:
    print('плохой ввод')
    exit()

m = n
A = []
stolb =0
z = -1
a = [[random.randrange(0,9) for y in range(n)] for x in range(m)]

print('----------Исходная матрица----------')
for i in range(m):
    print('    ', a[i])

print()

if n % 2 == 0:
    for i in range(n//2):
        for j in range(n):
            a[i][j], a[i + n//2][j] = a[i + n//2][j], a[i][j]

    for i in range(m):
        print('    ', a[i])
else:
    for i in range(n//2):
        for j in range(n):
            a[i][j], a[i + n//2+1][j] = a[i + n//2+1][j], a[i][j]
    for i in range(m):
        print('    ', a[i])
        
for i in range(n):
    summ = 0
    k = 0
    for j in range(m):
        summ = summ + a[j][i]
        k = k + 1
    A.append(summ//k)
print(A)


maxx = A[0]
for i in range(n):
    if maxx < A[i]:
        maxx = A[i]
print(maxx)
stolb = A.index(maxx)
print(stolb)
p = 0
if stolb != n-1:
    for i in range(n-1):
    
        a[i][stolb] = a[i][stolb+1]


    
    for r in range(stolb, m-1):
        for i in range(n):
            a[i][stolb+p] = a[i][stolb+1+p]
        p = p + 1
    
for i in range(m):
    del (a[i][n-1])
    
for i in range(m):
    print('    ', a[i])        


    
    
    

