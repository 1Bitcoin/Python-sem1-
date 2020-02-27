import random
x = [int(i) for i in input('Введите значения через пробел ').split()]
print(x)
N = len(x)
u = 0
flag = 0

r = []
minel= maxel = x[1] 

for z in x: 
    if minel >= z: 
        minel = z 
    if maxel <= z: 
        maxel = z 

print(minel, maxel)

for i in range(N):
    if x[i] == minel:
        r += [flag]
    flag += 1
print(r)
for t in r:
    j = t
    print(j)
    x.append(maxel)
    while N > j+1+u:
        x[N], x[N-1] = x[N-1], x[N]
        N -= 1
    
    u += 1
    N = len(x)
print(x) 

    

        
        


