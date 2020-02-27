matr = [

'   Однажды в сffg  f тудёнуюю зимнюю   ', 
' пору ага. медленно Я иdd dd Aaaз лесу',
'  вышелada da . Был сильный нехороший и противный холодный',
' мороз. медленно Гляжувв поddd     ме 4+45654+4-5+55 дленно f22+3-4+3-4fg fggается fuf fff медленно в',
'  гору. Лошадка медленно в  езуапапр 3+2+10ща fg я несущ ая много плохого хворосту     ',
'    воз. И шевствую важн fg о, в спокойствии   ',
'       чинном. медленно fg Лошадк 6+4-6-5 у ве зета вф под уздцы мужичок'

    ]
len_max = 0

for i in matr:
    print(i)
print()

'''# Выравнивание по левому краю.
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
    ' '.join(i.split())
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
    i = ' '.join(i.split())
    ln = len(i)
    ln_del = len_max - ln
    A = i.split()
    A2 = i.split()
    for y in i:
        if y == ' ':
            count += 1
    if ln_del == 0:
        print(i)
    elif (ln_del)//(count) == 0:
        ff = 0
        llenn = len(A)
        for tt in range(llenn-(ln_del+1)):
            A.pop()
            ff += 1
        i = '  '.join(A) + ' ' + ' '.join(A2[len(A2)-ff:])
        print(i)
    elif (ln_del)%(count)!= 0:
        zam  = ' '*((ln_del)//(count)+1)
        i = zam.join(i.split())
        fm = 0
        A3 = i.split()
        A4 = i.split()
        llenn2 = len(A3)
        for tm in range(llenn2 - ((ln_del)%(count)+1)):
            A3.pop()
            fm += 1
        msm = ' '*((ln_del)//(count)+1)
        rdd = ' '*(((ln_del)//(count))+2)
        i = rdd.join(A3) + zam + zam.join(A4[len(A4)-fm:])
        print(i)
    else:
        mk = ' '*((ln_del)//(count)+1)
        i = mk.join(i.split())
        print(i)
print()'''

'''# Замена слова. 
wordforreplace = 'медленно'
newword = 'хуй'
word = ""
for item in range(len(matr)):
    wholeitem = ""
    for letter in matr[item]:
        if letter.isalpha():
            word += letter
        else:
            if word == wordforreplace:
                word = newword
                wholeitem += word + ' '
                word = " "
            else:
                wholeitem += word + ' '
                word = ""
    word= ""
    matr[item] = wholeitem
print()
for i in matr:
    print(i)
print()'''

'''# Удаление слова. 
wordfordel = 'хуй'
word = ""
for item in range(len(matr)):
    wholeitem = ""
    for letter in matr[item]:
        if letter.isalpha():
            word += letter
        else:
            if word == wordfordel:
                word = ''
                wholeitem += word + ' '
                word = " "
            else:
                wholeitem += word + ' '
                word = ""
    word= ""
    matr[item] = wholeitem
print()
for i in matr:
    print(i)
print()'''

# Вычисление выражения строках.
for item in range(len(matr)):
    coin = []
    summ = 0
    copp = ""
    buf = ""
    i = 1
    for letter in range(len(matr[item])):
        mar = matr[item]
        if mar[letter].isdigit() and not mar[letter-1].isdigit() and not mar[letter-1] == '+' and not mar[letter-1] == '-':
            buf += mar[letter]
            copp += mar[letter]
            while mar[letter+i].isdigit():
                buf += mar[letter+i]
                buf += mar[letter+i]
                i += 1
            else:
                while mar[letter+i] == "-" or mar[letter+i] == "+":
                    
                    while mar[letter+i] == "+":
                        buf += ' '
                        copp += '+'
                        i += 1
                        if mar[letter+i].isdigit():
                            buf += mar[letter+i]
                            copp += mar[letter+i]
                            i += 1
                            while mar[letter+i].isdigit():
                                buf += mar[letter+i]
                                copp += mar[letter+i]
                                i += 1
                        coin = buf.split()
                        summ = int(coin[0])+int(coin[1])
                        buf = str(summ)
                        
                    
                    else:
                        while mar[letter+i] == "-":
                            buf += ' '
                            copp += '-'
                            i += 1
                            if mar[letter+i].isdigit():
                                buf += mar[letter+i]
                                copp += mar[letter+i]
                                i += 1
                                while mar[letter+i].isdigit():
                                    buf += mar[letter+i]
                                    copp += mar[letter+i]
                                    i += 1
                            coin = buf.split()
                            summ = int(coin[0])-int(coin[1])
                            buf = str(summ)
            print(copp)
            print(summ)
            buf = ""
            i = 1
            
            
            '''wordforreplace = copp
            newword = summ
            word = ""
            for item in range(len(matr)):
                wholeitem = ""
                for letter in matr[item]:          
                    if letter.isalpha():
                        word += letter
                    else:              
                        if word == wordforreplace:
                            word = newword
                            wholeitem += word + ' '
                            word = " "
                        else:
                            wholeitem += word + ' '
                            word = ""
                word= ""
                matr[item] = wholeitem'''
            copp = ""
            

'''
for i in matr:
    print(i)
print()                     
       '''         
            
            
            
'''
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
    print()'''
            
                
        


    

