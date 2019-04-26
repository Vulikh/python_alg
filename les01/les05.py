# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
#  (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль 
#  (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и 
#  отдельно вывести наименования предприятий, чья прибыль ниже среднего.


import collections


companiesQuantity = int(input('Введите количество компаний '))
Company = collections.namedtuple('Company', ['name', 'q1','q2', 'q3', 'q4', 'sum'] )
company = []
companies = []
upCompanies = []
downCompanies = []
averOver = 0


for _ in range(companiesQuantity):
	name = input(f'Введите название компании {_+1} ')
	company.append(name)
	sum = 0
	for quarter in range(4):
		q = int(input(f'Прибыль за {quarter+1} квартал '))
		sum+= q
		company.append(q)
	company.append(sum)
	c = Company._make(company)
	companies.append(c)
	company = []


for company in companies:
	averOver += company.sum 

averOver = averOver / companiesQuantity

print(f'Средняя прибыль компаний за год {averOver}')

for company in companies:
	if company.sum > averOver:
		upCompanies.append(company)
	elif company.sum < averOver:
		downCompanies.append(company)

print('Комgании с прибылью выше среднего:')

for company in upCompanies:
	print(f'Компания {company.name} заработала {company.sum}')

print('Комgании с прибылью ниже среднего:')

for company in downCompanies:
	print(f'Компания {company.name} заработала {company.sum}')









