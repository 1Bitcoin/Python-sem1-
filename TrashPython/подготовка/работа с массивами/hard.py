def print_matrix(m):
    for str in m:
        for el in str:
            print('{:4}'.format(el),end = ' ')
        print()


def right(count):
    global q, i, j
    for _ in range(count):
        a[i][j] = q
        q+=1
        j+=1
    j-=1


def down(count):
    global q, i, j
    for _ in range(count):
        a[i][j] = q
        q += 1
        i += 1
    i-=1


def left(count):
    global q, i, j
    for _ in range(count):
        a[i][j] = q
        q += 1
        j -= 1
    j+=1

def up(count):
    global q, i, j
    for _ in range(count):
        a[i][j] = q
        q+=1
        i-=1
    i+=1


n = int(input('Введите N: '))
k = 2*n
a = [[0]*2*n for i in range(4*n)]

q = 1
i = 0
j = 0

while k>0:
    right(k)
    k-=1
    i+=1
    down(k)
    j-=1
    k-=1
    if k == 0:
        break
    left(k)
    k-=1
    i-=1
    up(k)
    k-=1
    j+=1

k=1
if n % 2 == 0:
    up(k)
    k+=1
    i-=1
    left(k)
    k+=1
    j-=1
while k<2*n:
    down(k)
    k+=1
    i+=1
    if k == 2*n:
        break
    right(k)
    k+=1
    j+=1
    up(k)
    k+=1
    i-=1
    left(k)
    k+=1
    j-=1
k1 = k - 2
while k > n:
    right(k)
    i+=1
    down(k1)
    i+=1
    left(k)
    i-=1
    
    k1-=2
    k-=1
    if k == n:
        break
    
    right(k)
    i-=1
    up(k1)
    i-=1
    left(k)
    i+=1
    k1-=2
    k-=1
    
print_matrix(a)
