"""

Программа: Вычисление суммы чисел бесконечного ряда 

Автор: Мясненко Дмитрий Алексеевич ИУ7-15Б 

"""

import math as m

# Ввод значений
E, x = map(float, input("Введите эпсилон и значение x: ").split())
h, n_max = map(int, input("Введите шаг и количество итераций: ").split())

# Значения для форматирования и задание 
print("\n" * 5)
line = "-" * 67
header = "|   Значение n  |      Значение          |         Сумма          |"  #esk
flag = (E > 0) and (0 < x <= 1) and (h > 0) and (n_max > 0)
iteration = 0
out = "|{:^15.10g}|{:^24.12g}|{:^24.12g}|"
n = 1
Sum = x
New_summ = 0
h_flag = 0

# Проверка на ввод значений
if not flag:
	print("Введены не верные значения")
else:
	print(line)
	print(header)
	print(line)

	# Вычисление ряда
	while abs(New_summ - Sum) > E and iteration <= n_max:
		iteration += 1 
		h_flag += 1
		new_zn = ((m.pow(-1,n + 1) * m.pow(x,(2 * n + 1))) / (4 * m.pow(n,2) + 1))
		Sum = New_summ
		New_summ += new_zn

		# Вывод через шаг
		if h_flag == h or n == 1:
			h_flag = 0
			print(out.format(n, new_zn, New_summ))
		n += 1

	# Конечный вывод
	if iteration > n_max:
		print("Количество итераций превышено")
	else:
		print("Сумма ряда с точностю E: {:.12g}".format(New_summ))
		print("Сошлось за {} итераций".format(iteration))






