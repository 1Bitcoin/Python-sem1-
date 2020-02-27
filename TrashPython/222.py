import random
n = int(input()) #stroki
m = int(input())
k = 0
s = 0
p = 0
a = [[random.randrange(0,9) for i in range(m)] for i in range(n)]
for z in a:
    print(z)
print()
for i in range(m):
    for j in range(n):
        if a[j][i] % 2 == 0:
            k += 1
    p = k
    k = 0
    if p >= 3:
        k = 0
        print(i)
        if i != m - 1:
            s = s + 1
            for q in range(i, m-1):               
                for t in range(n):
                    a[t][q] = a[t][q+1]
                    i = 0
                        

for z in a:
    print(z)
print()
print(s)

        
