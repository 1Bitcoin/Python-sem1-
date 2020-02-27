from random import random

n = 6 #stolb
m = 6 #stroki

A = [[int(random()*10) for j in range(n)] for i in range(m)]

for r in A:
    print(r)

for j in range(n):
    k = 0
    
    for i in range(m):
        if A[i][j] % 2 == 0:
            k += 1

    if k > 3:
        
        n -= 1
        for i in range(m):
            for k in range(j, n):
                A[i][k] = A[i][k+1]
            
print()

for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
print()


i_max = 0
j_max = 0

for i in range(m):
    for j in range(n):
        if A[i][j] > A[i_max][j_max]:
            i_max, j_max = i, j

# пузырёк
for j in range(n-1):
    for k in range(n-2, j-1, -1):
        if A[i_max][k] > A[i_max][k+1]:
            A[i_max][k], A[i_max][k+1] = A[i_max][k+1], A[i_max][k]

for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
print()
