eps = float(input('eps '))
x = float(input('x '))
t = 1
y = 1
n = 0
while abs(t) > eps:
    n += 1
    t *= ((x) / n)
    y += t
print('x ', x, 'y ', y)
