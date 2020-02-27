def buble_sort(mass):
    '''
сортировка пузырьком
    '''
    len_mass= len(mass)
    for i in range(len_mass, 0, -1):
        need = False
        for j in range(1, i):
            if mass[j-1] > mass[j]:
                mass[j-1], mass[j] = mass[j], mass[j-1]
                need = True
        if not need: break
            
    return mass


def shaker(mass):
    '''
основан на пузырке
только в отличии него
делается два прохода
слева направо
справа налево 
    '''
    right = len(mass)
    left = 0
    swap = True
    while left <= right and swap:
        swap = False
        for i in range(left, right-1):
            if mass[i] > mass[i+1]:
                mass[i], mass[i+1] = mass[i+1], mass[i]
                swap = True
        right -= 1

        for i in range(right, left, -1):
            if mass[i-1] > mass[i]:
                mass[i], mass[i-1] = mass[i-1], mass[i]
                swap = True
        left += 1
    return mass


def comb(mass):
    '''
сортировка расчёсткой
    '''
    len_mass = len(mass)
    gap = len_mass
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap // 1.247))  # minimum gap is 1 
        swaps = False
        for i in range(len_mass - gap):
            j = i + gap
            if mass[i] > mass[j]:
                mass[i], mass[j] = mass[j], mass[i]
                swaps = True
    return mass


def m_comb(mass):
    len_mass = len(mass)
    gap = int(len_mass // 1.247)
    while gap:
        if 8 < gap < 11:
            gap = 11
        swaps = False
        for i in range(len_mass-gap):
            j = i + gap
            if mass[i] > mass[j]:
                mass[i], mass[j] = mass[j], mass[i]
                swaps = True
        gap = int(gap//1.247) or swaps
    return mass

