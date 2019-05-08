from pympler import asizeof

START = 2
END = 1000000

def first_numbers(start, end):

	numbers = [0] * 8

	for number in range(start,end):
		for _ in range(2,10):
			if number % _ == 0:
				numbers[_-2] += 1


	


	for i in range(len(numbers)):
		print(f'Числу {i+2} кратны {numbers[i]} чисел')

	print(f'Массив numbers занимает {asizeof.asizeof(numbers)} байт памяти')
	print(f'Переменная i занимает {asizeof.asizeof(i)} байт памяти')
	print(f'Общие затраты памяти {asizeof.asizeof(numbers) + asizeof.asizeof(i)} байт')


def second_numbers(start, end):

	a = 1
	b = 9
	frq = 0
	x = start

	while a != b:
		a += 1
		while x < end:
			if x % a == 0:
				frq += 1
			x += 1
		print(f'Числу {a} кратны {frq} чисел')
		x = start
		frq = 0

	
	print(f'Переменная a занимает {asizeof.asizeof(a)} байт памяти')
	print(f'Переменная b занимает {asizeof.asizeof(b)} байт памяти')
	print(f'Переменная frq занимает {asizeof.asizeof(frq)} байт памяти')
	print(f'Переменная x занимает {asizeof.asizeof(x)} байт памяти')
	print(f'Общие затраты памяти {asizeof.asizeof(a) + asizeof.asizeof(b) + asizeof.asizeof(frq) + asizeof.asizeof(x)} байт')



first_numbers(START,END)
second_numbers(START,END)


# В виду одинаковой сложности алгоритмов алгоритм second_numbers предпочтительней т.к. использует меньше оперативной памяти