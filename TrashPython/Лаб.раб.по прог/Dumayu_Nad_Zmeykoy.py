import random

# Заводим матрицу и выводим ее.
n = 6 # столбцы
m = 6 # строки

A = []
a = [[random.randrange(0,10) for y in range(n)] for x in range(m)]

print('----------Исходная матрица----------')
for i in range(m):
    print('    ', a[i])


k = 0 
while k < (n // 2):
    for i in range(n-1-2*k):
        A.append(a[k][i+k])

    for j in range(n-1-2*k):
        A.append(a[j+k][n-k-1])
    
    for b in range(n-1-2*k):
        A.append(a[n-k-1][n-b-1-k])

    for z in range(n-1-2*k):
        A.append(a[n-1-z-k][k])
    k +=1
    
if n % 2 !=0:
    A.append(a[n//2][n//2])
print(A)

