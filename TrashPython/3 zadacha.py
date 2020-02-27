n = int(input('vvod n '))
a = [[0 for i in range(n)] for j in range(n)]

for p in a:
    print(p)
y = 0
x = 1
s = (n*n-n)//2+n

while s > x:
    j = n
    while j > 0:
        a[y][n-j] = x
        j -= 1
        x += 1
    y += 1
        
print()      
for p in a:
    print(p)
