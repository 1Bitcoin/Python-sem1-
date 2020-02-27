def merge(lst1, lst2):
    len_lst1 = len(lst1)
    len_lst2 = len(lst2)
    merged = [0] * (len_lst1 + len_lst2)

    q = i = j = 0
    while  i < len_lst1 and j < len_lst2:
        if lst1[i] <= lst2[j]:
            merged[q] = lst1[i]
            i += 1
        else:
            merged[q] = lst2[j]
            j += 1
        q += 1

    while i < len_lst1:
        merged[q] = lst1[i]
        i += 1
        q += 1
    while j < len_lst2:
        merged[q] = lst2[j]
        j += 1
        q += 1

    return merged

def merge_sort(mass):
    len_mass = len(mass)
    if len_mass < 2:
        return mass
    else:
        m = len_mass // 2    
        return merge(merge_sort(mass[:m]), merge_sort(mass[m:]))

def m_merge_sort(mass):
    mass = [[x] for x in mass]
    while len(mass) != 1:
        temp = []
        len_mass = len(mass)
        for j in range(0, len_mass-1, 2):
            temp.append(merge(mass[j], mass[j+1]))
        if len_mass % 2:
            t = temp.pop()
            temp.append(merge(t, mass[len_mass-1]))
        mass = temp
        
    return mass[0]  


if __name__ == '__main__':
    a = [3,4,2,34,3,24,1,2,332,1,3,2,58, -8]
    print(merge_sort(a[:]))
    print(m_merge_sort(a[:]))

    print('\n', a, sep='')
