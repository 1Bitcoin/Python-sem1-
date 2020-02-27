def insertion_sort(mass):
    len_mass = len(mass)
    for i in range(1, len_mass):
        v = mass[i]
        j = i
        while mass[j-1] > v and j > 0:
            mass[j] = mass[j-1]
            j -= 1
        mass[j] = v
    return mass


def barrier_insertion_sort(mass):
    i = 2
    n = len(mass)
    mass.append(mass[0])
    while i <= n:
        if mass[i-1] > mass[i]:
            mass[0] = mass[i]
            j = i - 1
            while mass[j] > mass[0]:
                mass[j+1] = mass[j]
                j -= 1
            mass[j+1] = mass[0]
        i += 1
    del mass[0]
    return mass


def binary_insertion_sort(mass):
    len_mass = len(mass)
    for i in range(1, len_mass):
        key = mass.pop(i)
        low, up = 0, i
        while low < up:
            mid = (low + up) // 2
            if mass[mid] < key:
                low = mid + 1
            else:
                up = mid
        mass.insert(low, key)
    return mass


def Shell(mass):
    '''
сортировка Шелла

общий смысл
отсортировать каждый t-ый элемент
и с каждой итерацией уменьшать шаг (t)
(для справки это сортировка
разновидность сортировок вставками)
    '''
    len_mass = len(mass)
    
    t = len_mass//2
    while t > 0:
        for i in range(len_mass - t):
            j = i
            while j > -1 and mass[j] > mass[j+t]:
                mass[j], mass[j+t] = mass[j+t], mass[j]
                j -= 1
        t //= 2
    return mass
