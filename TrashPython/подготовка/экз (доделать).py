import random
m = n = random.randrange(4, 7)
matr = [[random.randrange(-5, 5) for x in range(n)] for j in range(m)]
print('Исходная матрица')
for row in matr:
    print(''.join(['{:< 5}'.format(x) for x in row]))

summ = 0
maxsumm = 0
num = n
diag = None
for i in range(n - 2):
    num -= 1
    for j in range(m - 1 - i):
        if matr[m - 2 - j - i][j] < 0:
            summ += matr[m - 2 - j - i][j]
    summ = abs(summ)
    if summ > maxsumm:
        maxsumm = summ
        diag = num

for i in range(n):
    if matr[m - i - 1][i] < 0:
        summ += matr[m - i - 1][i]
summ = abs(summ)
if summ > maxsumm:
    maxsumm = summ
    diag = n

nums = m
for i in range(n - 2):
    nums += 1
    for j in range(m - 1 - i):
        if matr[m - j - 1][1 + i + j] < 0:
            summ += matr[m - j - 1][1 + i + j]
    summ = abs(summ)
    if summ > maxsumm:
        maxsumm = summ
        diag = nums
print()
if diag == None:
    print('Все эелементы на диагоналях оказались положительны')
else:
    print('Номер диагонали: ', diag)

ask = 0
ask_ab = 0
string = None
for i in range(n):
    for j in range(n):
        if matr[i][j] == 0:
            ask += 1
    if ask > ask_ab:
        ask_ab = ask
        string = i
print('Матрица без строки с наиб. кол-вом нулей (удаляется последняя строка, если кол-во нулей равно кол-ву нулей в других строках)')

check = -1
for row in matr:
    check += 1
    if check != string:
        print(''.join(['{:< 5}'.format(x) for x in row]))













            
            
