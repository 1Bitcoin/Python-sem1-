import random
p = random.randrange(3,9)
x = [random.randrange(1,9) for i in range(p)]
print(x)

summ = 0
number = 0
for i in range(p):
    summ += x[i]
    number += 1
middle_value = summ // number
print(middle_value)

element = x[0]
eps = abs(middle_value - x[0])
for z in x:
    if abs(middle_value - z) < eps:
        eps = middle_value - z
        element = z
print(element)
    
