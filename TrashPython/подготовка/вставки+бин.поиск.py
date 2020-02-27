import random

a = [7,5,9,0,2,3,3,4,5,6,7,8,9,-33,5,1000,4,6,-5,]

for i in range(1, len(a)):
    key = a[i]
    low, up = 0, i
    while up > low:
        middle = (low+up) // 2
        if a[middle] < key:
            low = middle + 1
        else:
            up = middle
    a[:] = a[:low] + [key] + a[low:i] + a[i + 1:]

print(a)
