
import timeit

START = 2
END = 99


def first_numbers(start, end):

	numbers = [0] * 8

	for number in range(start,end):
		for _ in range(2,10):
			if number % _ == 0:
				numbers[_-2] += 1


	for i in range(len(numbers)):
		print(f'Числу {i+2} кратны {numbers[i]} чисел')


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


first_alg = timeit.timeit('first_numbers', setup = 'from __main__ import first_numbers', number = 10000)
second_alg = timeit.timeit('second_numbers', setup = 'from __main__ import second_numbers', number = 10000)

print(f'Скорость выполнения алгоритмов при {END - START + 1} чисел')
print(f'Первый выполнился за {first_alg} сек')
print(f'Второй выполнился за {first_alg} сек')
print('_'*40)

START = 2
END = 999

first_alg = timeit.timeit('first_numbers', setup = 'from __main__ import first_numbers', number = 10000)
second_alg = timeit.timeit('second_numbers', setup = 'from __main__ import second_numbers', number = 10000)

print(f'Скорость выполнения алгоритмов при {END - START + 1} чисел')
print(f'Первый выполнился за {first_alg} сек')
print(f'Второй выполнился за {first_alg} сек')
print('_'*40)

START = 2
END = 9999

first_alg = timeit.timeit('first_numbers', setup = 'from __main__ import first_numbers', number = 10000)
second_alg = timeit.timeit('second_numbers', setup = 'from __main__ import second_numbers', number = 10000)

print(f'Скорость выполнения алгоритмов при {END - START + 1} чисел')
print(f'Первый выполнился за {first_alg} сек')
print(f'Второй выполнился за {first_alg} сек')
print('_'*40)

START = 2
END = 99999

first_alg = timeit.timeit('first_numbers', setup = 'from __main__ import first_numbers', number = 10000)
second_alg = timeit.timeit('second_numbers', setup = 'from __main__ import second_numbers', number = 10000)

print(f'Скорость выполнения алгоритмов при {END - START + 1} чисел')
print(f'Первый выполнился за {first_alg} сек')
print(f'Второй выполнился за {first_alg} сек')
print('_'*40)

START = 2
END = 999999

first_alg = timeit.timeit('first_numbers', setup = 'from __main__ import first_numbers', number = 10000)
second_alg = timeit.timeit('second_numbers', setup = 'from __main__ import second_numbers', number = 10000)

print(f'Скорость выполнения алгоритмов при {END - START + 1} чисел')
print(f'Первый выполнился за {first_alg} сек')
print(f'Второй выполнился за {first_alg} сек')
print('_'*40)


START = 2
END = 9999999999999

first_alg = timeit.timeit('first_numbers', setup = 'from __main__ import first_numbers', number = 10000)
second_alg = timeit.timeit('second_numbers', setup = 'from __main__ import second_numbers', number = 10000)

print(f'Скорость выполнения алгоритмов при {END - START + 1} чисел')
print(f'Первый выполнился за {first_alg} сек')
print(f'Второй выполнился за {first_alg} сек')
print('_'*40)


#Вывод:

# Сложность алгоритма поиска количества делителей равна 0(1)



