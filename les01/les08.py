# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, 
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib

s = input('Введите строку ')
count = 0
sub_strings = []

for i in range(len(s)):
	for j in range(len(s)+1):
		string = s[i:j]
		if string:
			print(string)
		hashed = hashlib.sha256(string.encode('utf-8')).hexdigest()
		if s[i:j] and hashed not in sub_strings and s[i:j] != s:
			count+=1
			sub_strings.append(hashed)

print(f'Всего {count} подстрок')

