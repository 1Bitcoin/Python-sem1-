a = [1,2,6,6,6,6,6,4,7,5,6,6,7,8,4,5,6]

dell = 6
print(a)
for j in range(len(a)):
    for i in range(len(a)-1):
        if  a[i] == dell:
            a[i], a[i+1] = a[i+1], a[i]
i = 0
while a[i] != dell:
    print(a[i], end = ' ')
    i += 1
