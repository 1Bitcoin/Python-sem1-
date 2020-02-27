import random

def summator(a):
    summa = 0
    while a > 0:
        summa += a % 10
        a = a // 10
    return summa

def bubble_sort(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if summator(a[j - 1]) < summator(a[j]):
                a[j - 1], a[j] = a[j], a[j - 1]
    return a

b = []
p = random.randrange(4,12)
x = [random.randrange(9, 20) for i in range(p)]
print(x)

print(bubble_sort(x))

