'''
метод симпсона
приближения параболами
'''

def f(x):
    return x*x
a = 0
b = 2
n = 2*5 # обязательна кратность двум

h = (b - a) / n

s = f(a) + f(b)

for i in range(1, n):
    x = a + h*i
    if i % 2:
        s += 4 * f(x)
    else:
        s += 2 * f(x)
print(s * h / 3)
