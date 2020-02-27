import random
n = int(input('vvod n '))
a = [[random.randrange(0,1) for i in range(n)] for j in range(n)]
for p in a:
    print(p)
x = 0    
r = 0
buff = 0
q = 0

while 90 > q:
    
    for i in range(n-r*(n//2)):
        buff += 1
        a[x][i+x] = buff
        q += 1
    x += 1


    for j in range(1, n-r*(n//2)):
        buff += 1
        a[j+r][n-j-1-2*r] = buff
        q += 1

    for p in range(1,n-1-r*(n//2)):
        buff += 1
        a[n-p-1-2*r][r] = buff
        q += 1
        
    r += 1
    

print()
for p in a:
    print(p)

