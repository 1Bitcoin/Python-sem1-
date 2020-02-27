def BinSearch(li, x):
    
    i = 0
    j = len(li)-1
    m = int(j/2)
    
    while li[m] != x and i < j:
        if x > li[m]:
            i = m+1
        else:
            j = m-1
        m = int((i+j)/2)
    if i > j:
        return print('Нет такого')
    else:
        return m
li = [1,2,4,5,6,7,8,9,11]
x = int(input('x '))
print('index', x, '=',BinSearch(li, x))
