from random import randint
'''
умножение многочлена на многочлен
'''
def print_polynom(lst_koef):
    # print(lst_koef)
    len_lst_koef = len(lst_koef)
    s = ['']*len_lst_koef
    st = 0
    for i in range(len_lst_koef-1, -1, -1):
        k = lst_koef[i]
        t = x = ''
        if k > 0:
            t = ' + ' + str(k)
        if k < 0:
            t = ' - ' + str(k)
        if k == 1 and st:
            t = t.replace('1', '')
        if t:
            if  st > 0:
                x = 'x'
            if st > 1:
                x += '**' + str(st)
            s[i] = t+x
        st += 1
    s[0] = s[0][1:]
    if '+' in s[0]:
        s[0] = s[0][2:]
    s = ''.join(s)
    if s:
        print(s)
    else:
        print(0)
    print()


N = randint(1, 9)
M = randint(1, 9)

# коэфиценты первого многочлена
a = [randint(0, 9) for i in range(N)]
b = [randint(0, 9) for i in range(M)]

print_polynom(a)

print_polynom(b)

c = [0]*(N+M-1)
for i in range(N):
    for j in range(M):
        c[i+j] += a[i] * b[j]

print_polynom(c)
