import random

n = int(input()) # stolb
m = int(input()) # stroka

a = [[random.randrange(0,9) for i in range(n)] for j in range(m)]
b = [[random.randrange(0,9) for i in range(n)] for j in range(m)]
print('--------Матрица А --------')
for z in a:
    print(z)
print()
print('--------Матрица B --------')
for v in b:
    print(v)
print()
for i in range(m):
    for j in range(n):
        a[i][j] = a[i][j]- b[i][j]
print('--------Матрица C --------')
for z in a:
    print(z)
print()
