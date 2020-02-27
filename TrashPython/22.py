n = int(input())

a = []*n
x = 1
v = 0
p = 0
for i in range(n):
    print(v)
    p = v
    v = v + x
    x = p
