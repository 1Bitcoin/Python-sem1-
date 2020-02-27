import random
n = int(input())
a = [[random.randrange(0,1) for i in range(n)] for k in range(n)]
for b in a:
    print(b)
i, j = 0,0
while k < (n*n-n)//2+n:
    while j < n-1  and b[i][j+1] == 0:
        b[i][j] = k
        k 
