import random
n = 5
matrix = [['.' for x in range(n)] for p in range(n)]
    
for i in range(n):
    matrix[i][i] = '#'
print()
    
# stolb row

for i in range(n):
    matrix[n - i - 1][i] = '#'
matrix[n // 2][n// 2] = '$'

for elem in range(n):
    if elem !=  n // 2:
        matrix[n//2][elem] = '@'


for i in range(n):
    for j in range(n):
        if j != n - 1:
            print(matrix[j][i], end = '  ')
        else:
            print(matrix[j][i])
        
