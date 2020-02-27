import random
import copy
m =6 # строки
n =6 # стобцы
a = [[random.randrange(0,10) for i in range (n)] for j in range(m)]

x = []
z = 0
s = 0
f = 0
d = copy.deepcopy(a)


for i in range(m):
    minel = d[i][0]
    s = i
    f = 0
    for j in range(n):
        if minel >= d[i][j]:
            minel = d[i][j]
            s = i
            f = j
    d[i][z], d[s][f] = d[s][f], d[i][z]
    z += 1
for h in a:
    q = 0
    for u in h:
        if u == 0:
            q += 1
    x.append(q)
    
for i in range(m):
    print(a[i], ' ', d[i], '  ', x[i])



