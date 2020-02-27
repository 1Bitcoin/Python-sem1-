matr = [

'   Однажды, в студёнуюю зимнюю   ', 
' пору. Я из лесу',
'  вышел. Был сильный',
' мороз. Гл   яжу, поднимается медленно в',
'  гору. Лошадка,    везущая воросту     ',
'    воз. И, шевствую ва  жно,в спокойствии   ',
'       чинном. Лошадку медленно везет под уздцы мужичок'

    ]
len_max = 0

for i in matr:
    print(i)
print()

# Выравнивание по левому краю.


for i in matr:
    u = len(i)
    j = 0
    k, k1 = 0, 0
    while i[j] == ' ':
        j += 1
        k1 += 1
    while i[u - 1] == ' ':
        k += 1
        u -= 1
    i = i[k1:len(i) - k]
    print(i)
    if len(i) > len_max:
        len_max = len(i)

print()

# Выравнивание по правому краю.
for i in matr:
    u = len(i)
    j = 0
    k, k1 = 0, 0
    while i[j] == ' ':
        j += 1
        k1 += 1
    while i[u - 1] == ' ':
        k += 1
        u -= 1
    i = i[k1:len(i) - k]
    i = ' '*(len_max-len(i)) + i
    print(i)

print()
# Выравнивание по ширине
for i in matr:
    count = 0
    k2 = 0
    u = len(i)
    j = 0
    k, k1 = 0, 0
    while i[j] == ' ':
        j += 1
        k1 += 1
    while i[u - 1] == ' ':
        k += 1
        u -= 1
    i = i[k1:len(i) - k]
    ln = len(i)
    ln_del = len_max - ln

    for y in i:
        if y == ' ':
            count += 1
    if (ln_del)//(count) == 0:
        i = i.replace(' ', ' '*2,ln_del)
        print(i)
    elif (ln_del)%(count)!= 0:
        i = i.replace(' ', ' '*(((ln_del)//(count))+1))
        i = i.replace(' '*((ln_del)//(count)+1), ' '*((ln_del)//(count)+2), (ln_del)%(count))
        print(i)
    else:
        i = i.replace(' ', ' '*((ln_del)//(count)+1))
        print(i)
print()
# Замена слова.
string = 'медленно'
stringn = 'хуй'
for i in matr:
    lenStrOld = len(string)
    while i.find(string) > 0:
        h = i.find(string)
        i = i[:h] + stringn + i[h+lenStrOld:]
    print(i)
print()

# Удаление слова.
for i in matr:
    lenStrOld = len(string)
    while i.find(string) > 0:
        h = i.find(string)
        i = i[:h-1]+ i[h+lenStrOld:]
    print(i)

# Количество слов длины 2, 3 и тд
mi_len = 0
ch = 0
must = 0
kolvo = 0
v = 1
for i in matr:
    u = len(i)
    j = 0
    k, k1 = 0, 0
    while i[j] == ' ':
        j += 1
        k1 += 1
    while i[u - 1] == ' ':
        k += 1
        u -= 1
    i = i[k1:len(i) - k] + '@'
    for x in i:
        if x.isalnum():
            ch += 1
            if ch > mi_len:
                mi_len = ch
        else:
            ch = 0
    ch = 0
    for z in range(2,mi_len+1):
        for x in i:
            if x.isalnum():
                
                must += 1
            elif must == z:
                kolvo += 1
            
            if x.isalnum() == False:
                must = 0
        must = 0
        if kolvo !=0:
            print('Кол-во слов длиной',z,'в',v,'строке равно:', kolvo)
        kolvo = 0
    mi_len = 0
    v += 1
    print()
            
                
        


    

