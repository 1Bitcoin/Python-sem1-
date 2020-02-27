def selection_sort(mass):
    '''
сортировка выбором
    '''
    len_mass = len(mass)
    for i in range(len_mass):
        min_i = i
        for j in range(i+1, len_mass):
            if mass[j] < mass[min_i]:
                min_i = j
        mass[min_i], mass[i] = mass[i], mass[min_i]
    return mass
