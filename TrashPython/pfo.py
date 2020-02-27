n = int(input('Размер: '))
m = [[0]*n for i in range(n)]
k = (n*n - n)//2 + n
print(k)
x = 1
i = 0
j = n - 1
m[i][j] = 1
while x < k:
    while j > 0 and m[i + 1][j - 1] == 0:
        i += 1
        j -= 1
        x += 1
        m[i][j] = x
    while j < n - 1 and m[i][j+1] == 0:
        j += 1
        x += 1
        m[i][j] = x
    while i > 0 and m[i - 1][j] == 0:
        i -= 1
        x += 1
        m[i][j] = x

for i in range(n):
    for j in range(n):
        print ("%4d" % m[i][j], end = " ")
    print()
