array = [6, 1, 5, 2, 4, 3, 10, 5, 7, 8, 9, 23, 0]

# is find sum of all elements in array
summ = 0
k = 0
for number in range(len(array)):
    summ += array[number]
    k += 1
    
middle = summ // k
ind = 0

# find index middle elements
for num in array:
    ind += 1
    if int(num) == middle:
        break
if middle in array:
    
    p = len(array) - ind
    ind -= 1

    # dell elem that is equal to middle value of elements in array
    for i in range(p):
        array[ind], array[ind + 1] = array[ind + 1], array[ind]
        ind += 1

    print('This is a modifield array')
    print(array[:len(array) - 1])

    # or another way

    print()
    print('This is a modifield array too')
    for num in range(len(array) - 1):
        if num == len(array) - 2:
            print(array[num])
        else:
            print(array[num], end = ', ')
else:
    print('Среднего значениея (', middle, ') нет в массиве')

    
    
    
