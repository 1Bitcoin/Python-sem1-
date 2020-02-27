s = input('Введите строку: ').strip()
l = len(s)

list_ch = []
len_ch = 0
m = s[0].lower() == s[0]

for i in range(l):
    if s[i] == ' ':
        if s[i-1] != ' ' and m:
            list_ch.append(' ')
            len_ch += 1
        m = s[i+1].lower() == s[i+1]
    elif m:
        list_ch.append(s[i])
        len_ch += 1
if m:
    list_ch.append(s[l-1])
    len_ch += 1
else:
    list_ch.pop()
    len_ch -= 1

print(''.join(list_ch))
print(len(list_ch))
print(len_ch)
