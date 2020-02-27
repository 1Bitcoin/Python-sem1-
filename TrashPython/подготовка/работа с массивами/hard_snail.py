def print_matrix(m):
    for row in m:
        print(''.join(['{:<5}'.format(x) for x in row]))
    print()

def snail_clockwise(a, i, j, q):
    i, j, q = right(a, i, j, q)
    i += 1
    j -= 1
    
    i, j, q = down(a, i, j, q)
    i -= 1
    j -= 1
    
    i, j, q = left(a, i, j, q)
    i -= 1
    j += 1
    
    i, j, q = up(a, i, j, q)
    i += 1
    j += 1

    return i, j, q

def snail_counterclockwise(a, i, j, q):
    i, j, q = down(a, i, j, q)
    i -= 1
    j += 1
    
    i, j, q = right(a, i, j, q)
    i -= 1
    j -= 1
    
    i, j, q = up(a, i, j, q)
    i += 1
    j -= 1
    
    i, j, q = left(a, i, j, q)
    i += 1
    j += 1
    return i, j, q

def up(a, i, j, q):
    while a[i][j] == 0:
        a[i][j] = q
        q += 1
        i -= 1
    return i, j, q


def down(a, i, j, q):
    while a[i][j] == 0:
        a[i][j] = q
        q += 1
        i += 1
    return i, j, q


def left(a, i, j, q):
    while a[i][j] == 0:
        a[i][j] = q
        q += 1
        j -= 1
    return i, j, q

def right(a, i, j, q):
    while a[i][j] == 0:
        a[i][j] = q
        q += 1
        j += 1
    return i, j, q

n = 4 # n > 1

M = 2*n
N = 4*n

a = [[0]*M for i in range(N)]

h = 0
i = j = 0
q = 1


while a[i][j] == 0 and M - 2*h > 0:
    while j < M-h:
        a[i][j] = q
        q += 1
        j += 1
    j -= 1
    i += 1

    while i < M-h:
        a[i][j] = q
        q += 1
        i += 1
    i -= 1
    j -= 1

    while j > h:
        a[i][j] = q
        q += 1
        j -= 1

    j += 1
    i -= 1
   
    while i > h+1:
        a[i][j] = q
        q += 1
        i -= 1
    i += 1
    j += 1
    
    h += 2

if a[i+1][j] != 0:
    a[i][j] = q
    i -= 1
    a[i][j] = q + 1
    a[i][j-1] = q + 2
    q += 3 
j -= 2

need = True
while need:
    i, j, q = down(a, i, j, q)
    i -= 1
    j += 1
    
    i, j, q = right(a, i, j, q)
    i -= 1
    j -= 1
        
    i, j, q = up(a, i, j, q)
    i += 1
    j -= 1
    
    while j > -1:
        if a[i][j] == 0:
            a[i][j] = q
            q += 1
            j -= 1
        else:
            break
    else:
        need = False
    j += 1
    i += 1
    need &= a[i][j] == 0

while i < N:
    a[i][j] = q
    q += 1
    i += 1
i -= 1
j += 1

while j < M:
    a[i][j] = q
    q += 1
    j += 1
j -= 1
i -= 1


i, j, q = up(a, i, j, q)
i += 1
j -= 1

i, j, q = left(a, i, j, q)
i += 1
j += 1

while a[i][j] == 0:
    i, j, q = snail_clockwise(a, i, j, q)
    if a[i][j] == 0:
        i, j, q = snail_counterclockwise(a, i, j, q)

print_matrix(a)
   


