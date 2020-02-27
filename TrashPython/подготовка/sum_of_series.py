eps = float(input('введите точность eps: '))
s = 4
t = 4
n = 0
while abs(t) > eps:
    t *= -(2*n+1)/(2*n+3)
    n += 1
    s += t
print('{:.9f}'.format(s))
