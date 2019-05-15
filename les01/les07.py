
import timeit 
import random

array = []

for i in range(50):
	array.append(random.randint(-100,99))


print('Исходный массив')
print(array)

# Сортировка слиянием

def mergeSort(array):

	def merge(left, right):

		result = []

		while len(left) > 0 and len(right) > 0:
			if left[0] < right[0]:
				result.append(left[0])
				left = left[1:]
			else:
				result.append(right[0])
				right = right[1:]

			if len(right) == 0:
				result += left
			elif len(left) == 0:
				result += right

		return result

	if len(array) < 2:
		return array

	middle = len(array) // 2 
	left = mergeSort(array[:middle])
	right = mergeSort(array[middle:])
	return merge(left, right)


#Сортировка пузырьком

def bubleSort(array):

	a = array

	for i in range(len(a)):
		for j in range(len(a) - 1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]

	return a 


merge_time = timeit.timeit('mergeSort', setup = 'from __main__ import mergeSort', number = 10000)
buble_time = timeit.timeit('bubleSort', setup = 'from __main__ import bubleSort', number = 10000)


print('Сортировка слиянием')
print(mergeSort(array))
print(f'{merge_time}')
print('Сортировка пузырьком')
print(bubleSort(array))
print(f'{buble_time}')

#Не совсем понимаю почему сортировки пузырьком и слиянием показывают одно и то же время(примерно) по timeit





