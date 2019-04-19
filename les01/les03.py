import random

# # 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

numbers = [0] * 8

for number in range(2,100):
	for _ in range(2,10):
		if number % _ == 0:
			numbers[_-2] += 1


for i in range(len(numbers)):
	print(i+2,f'{numbers[i]}')


# # 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих 
# позициях первого массива стоят четные числа.

numbers = []

indexNum = []

[numbers.append(int(i)) for i in input('Введите массив чисел')]

index = 0

for i in numbers:
	if i % 2 == 0:
		indexNum.append(index)
	index += 1

print(f'Индексы четных элементов {indexNum}')

# # 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

a = []

for i in range(10):
	a.append(random.randint(0,10)) 

print(f'Массив до смены элементов местами {a}')

minIndex = 0
maxIndex = 0

for i in range(len(a)):
	if a[minIndex] > a[i]:
		minIndex = i
	elif a[maxIndex] < a[i]:
		maxIndex = i

a[minIndex], a[maxIndex] = a[maxIndex], a[minIndex]		

print(f'Массив после {a}')


# # 4. Определить, какое число в массиве встречается чаще всего.


numbers = []
count = 0
maxNumber = 0

for i in range(20):
 	numbers.append(random.randint(0,10))

for num in numbers:
	currentCount = 0
	for _ in range(len(numbers)):
		if num == numbers[_]:
			currentCount += 1
		if currentCount > count:
			maxNumber = num
			count = currentCount
			

print(f'Массив {numbers}')
print(f'Чаще всего встречается элемент {maxNumber}')


# # 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

a = []
pos = 0

for i in range(10):
	a.append(-random.randint(1,10))

minimum = a[0]	

for i in range(len(a)):
	if a[i] < 0 and minimum < a[i]:
		minimum = a[i]
		pos = i

print(f'Массив {a}')
print(f'Максимальный отрицательный элемент {minimum}')
print(f'Его позиция {pos}')


# # 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
#  и максимальный элементы в сумму не включать.
# # 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), 
# так и различаться.
# # 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных
# элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

a = [[0 for i in range(4)] for j in range(5)]

for i in range(5):
	for j in range(3):
		a[i][j] = int(input(f'Введите элемент {i} {j} '))
		a[i][3] += a[i][j]

for _ in a:
	print(_)


# # 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.