import random

n = 6 # столбцы
m = 6 # строки

A = []
sp = [[0 for y in range(n)] for x in range(m)]
a = [[random.randrange(0,10) for y in range(n)] for x in range(m)]

print('----------Исходная матрица----------')
for i in range(m):
    print('    ', a[i])

for number in range(n):
    for gg in range(n):
        A.append(a[number][gg])
        
A = (sorted(A))

print()

p = 0
k = 0 
while k < (n // 2):
    for i in range(n-1-2*k):
        sp[k][i+k] = A[p]
        p += 1

    for j in range(m-1-2*k):
        sp[j+k][n-k-1] = A[p]
        p += 1
    
    for b in range(n-1-2*k):
        sp[n-k-1][n-b-1-k] = A[p]
        p += 1

    for z in range(m-1-2*k):
        sp[n-1-z-k][k] = A[p]
        p += 1
    k +=1
    
if n % 2 !=0:
    sp[n//2][n//2] = A[p]

for i in range(m):
    print('    ', sp[i])







    

