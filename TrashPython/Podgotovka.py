from random import random

def print_matrix():
    for i in range(m):
        for j in range(n):
            print(A[i][j], end=' ')
        print()
    print()


# setting
n = 5
m = 6
i_elem = 3
i_column = 2
i_row = 1

# -----------------------------------------------------------------------------
A = [int(random()*10) for _ in range(n)]

print('дан маcсив {}'.format(n))
print(A)

# удаление элемента
n -= 1
for i in range(i_elem, n):
    A[i] = A[i+1]


print('del elem with index = {}'.format(i_elem))
for i in range(n):
    print(A[i], end=' ')
print('\n')
# -----------------------------------------------------------------------------





# -----------------------------------------------------------------------------
A = [[int(random()*10) for _ in range(n)] for i in range(m)]

print('дана матрица: {}x{}'.format(n, m))
for r in A:
    print(r)
print()  

# удаление элемента
n -= 1
for i in range(m):
    for j in range(i_column, n):
        A[i][j] = A[i][j+1]

print('\ndel column with index = {}'.format(i_column))
print_matrix()
# -----------------------------------------------------------------------------





# тут две версии поэтому скопирнём массив
t = A[:]
# -----------------------------------------------------------------------------
# используя возможность питона (список = другому списку)

# удаление 
m -= 1
for i in range(i_row, m):
    A[i] = A[i+1]

print('\ndel row v1 with index = {}'.format(i_row))
print_matrix()
# -----------------------------------------------------------------------------





# -----------------------------------------------------------------------------
# тоже самое, но по хардкору (для самых древних языков)
A = t

# удаление строки
# m -= 1    сделали уже
for i in range(i_row, m):
    for j in range(n):
        A[i][j] = A[i+1][j]

print('\ndel row v2 with index = {}'.format(i_row))
print_matrix()
# -----------------------------------------------------------------------------
