def qsort(mass):
    '''
быстрая сортировка
используется доп массивы и рекурсия
    '''
    len_mass = len(mass)
    if len_mass < 2:
        return mass

    x = mass[len_mass//2]

    less, equal, more = [], [], []

    for el in mass:
        if el == x:
            equal.append(el)
        elif el > x:
            more.append(el)
        else:
            less.append(el)
    return qsort(less) + equal + qsort(more)


def quicksort(mass, l, r):
    if l >= r:
        return
    i, j = l, r
    x = mass[(l+r)//2]
    while i <= j:
        while mass[i] < x:
            i += 1
        while mass[j] >  x:
            j -= 1

        if i<=j:
            mass[i], mass[j] = mass[j], mass[i]
            i += 1
            j -= 1
            
    quicksort(mass, l, j)
    quicksort(mass, i, r)

    return mass


def quicksort_witout_rec(mass):
    stack = [0, len(mass)-1]
    
    while stack:
        r = stack.pop()
        l = stack.pop()

        i, j = l, r
        x = mass[(l+r)//2]

        while i <= j:
            while mass[i] < x: i += 1
            while mass[j] > x: j -= 1

            if  i <= j:
                mass[i], mass[j] = mass[j], mass[i]
                i += 1
                j -= 1
        if l < j:
            stack.extend([l, j])
        if i < r:
            stack.extend([i, r])
    return mass

if  __name__ == '__main__':
    a = [9,87,5,3,2,1,0,4,6,3,24,-8]

    print(qsort(a[:]))
    print(quicksort(a[:], 0, len(a)-1))
    print(quicksort_witout_rec(a[:]))

    print(a)
    
