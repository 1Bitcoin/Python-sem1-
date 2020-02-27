from sys import exit
L = int(input('input L: ')) #string
M = int(input('input M: ')) #solb

a = [ [ k for k in (input())] for p in range(L)]
for r in a:
    if len(r) > M or len(r) < M:
        print('bad')
        exit()

t = []
#Вы
for b in a:
    print(b)
print()
    
for i in range(L):
    for j in range(M):
        if (a[i][j]).isdigit():
            t.append(j)
            t.append(i)
print(t,'\n')

i = 0
while len(t) > i:
    if i % 2 == 0:
        w = t[i]
        for h in range(L):
            a[h][w] = '#'
    else:
        f = t[i]
        for y in range(M):
            a[f][y] = '#'
    i += 1

for b in a:
    print(b)
    

