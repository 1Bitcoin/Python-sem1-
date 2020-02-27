# Дана строка требуется определить содержится ли в ней
# заданная подстрока и если содержится то
# вывести номер ее позиции в строке
from sys import exit
string = input('исходная строка ')
podstr = input('подстрока ')
if podstr == '':
    print('bad')
    exit()
k = 0
if podstr in string:
    print('она содержится')

for i in range(len(string)):
    if string[i] == podstr[0]:
        number = i
        t = 1
        buf = i+1
        if len(podstr) == 1:
            print(number)
            exit()
        while string[buf] == podstr[t]:
            if buf + 1 <= len(string) - 1 and t + 1 <= len(podstr)-1:
                buf += 1
                t += 1
            else:
                if string[buf] == podstr[len(podstr)-1]:
                    print(number)
                    exit()
        else:
            if string[buf] == podstr[len(podstr)-1]:
                print(number)
                exit()
