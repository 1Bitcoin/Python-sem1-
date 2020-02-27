from random import randint
'''
отсортировать массив по спирали
Пример
3 8 2       1 2 3
7 9 1  ->   8 9 4
4 5 6       7 6 5
'''

def print_matrix(m):
    for row in m:
        print(''.join(['{:<5}'.format(x) for x in row]))
    print()

def comb_sort(m):
    len_m = len(m)
    gap = int(len_m/1.247)
    while gap:
        swap = 0

        for i in range(len_m - gap):
            j = i + gap
            if m[i] > m[j]:
                m[i], m[j] = m[j], m[i]
        
        gap = int(gap/1.247) or swap
    return m

N = 5
a = [[randint(0, 9) for j in range(N)] for i in range(N)]

print_matrix(a)

less, equal, more = [], [], []

x = a[N//2][N//2]
for i in range(N):
    for j in range(N):
        if a[i][j] < x:
            less.append(a[i][j])
        elif a[i][j] == x:
            equal.append(a[i][j])
        else:
            more.append(a[i][j])

print(less, equal, more)
m = comb_sort(less) + equal + comb_sort(more)

print(m)

ans = [[None]*N for i in range(N)]
i, j = 0, 0
q = 0
while ans[i][j] == None:
    while j < N:
        if ans[i][j] == None:
            ans[i][j] = m[q]
            q +=1
            j += 1
        else:
            break
    j -= 1
    i += 1
    
    while i < N:
        if ans[i][j] == None:
            ans[i][j] = m[q]
            q += 1
            i += 1
        else:
            break
    
    i -= 1
    j -= 1
    while j > -1:
        if ans[i][j] == None:
            ans[i][j] = m[q]
            q += 1
            j -= 1
        else:
            break
    i -= 1
    j += 1

    while ans[i][j] == None:
        ans[i][j] = m[q]
        q += 1
        i -= 1
        
    i += 1
    j += 1


print_matrix(ans)

