a = str(input('First number: '))
b = str(input('Second number: '))


max_len = len(a)
min_len = len(b)

if len(a) > len(b): # 1234 and 0023
    new_b = str('0' * (max_len - min_len) + b)
    new_a = a
    
elif len(a) < len(b):
    max_len, min_len = min_len, max_len
    new_a = str('0' * (max_len - min_len) + b)
    new_b = b
    
else:
    new_a = a
    new_b = b

 #'11001101'
 #'10001001'
 #'--------'
#'101010110'

m = []
temp = 0
for i in range(max_len - 1, -1, -1):
    p = int(new_a[i]) + int(new_b[i]) + temp
    temp = p // 4
    p %= 4
    m.append(p)
    
if temp != 0:
    m.append(temp)

print(m)
print()
for i in range(len(m)):
    print(m[len(m)-i-1], end = " ")

 #'1203'
 #'0131'
 #'--------'
#' 1012'















    

    
