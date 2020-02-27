m = " ".join([x for x in input('string ').split()
                if not ('A'<=x[0]<='Z' or 'А'<=x[0]<='Я')])
print(m)
print('Длина новой строки: ',len(m))
