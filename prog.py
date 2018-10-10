'''
@author: Bielocyca Yura
name of programm: Spacemans caculator
date of developing: 10.10.2018, 12:20
description: We have list of spscemans and do something with it
'''
spacemans = [
    ['Крошев', 175, 75],
    ['Ёжиков', 169, 74],
    ['Нюшева', 164, 73],
    ['Барашев', 189, 60],
    ['Копатычев', 171, 87],
    ['Лосяшев', 199, 80],
    ['Пинов', 169, 67],
    ['Совуньева', 198, 79],
]
total_Weight = 0
min_Size = 400
max_Size = 0
name_of_Max =''
name_of_Min =''
for name, size, weight in spacemans:
	if size > max_Size:
		max_Size=size
		name_of_Max = name
	total_Weight=weight+total_Weight
	if size < min_Size:
		min_Size=size
		name_of_Min = name
	print('Космонавт ',name,', рост - ',size, 'см, вес -',weight,'кг')
print('Всего космонавтов:', len(spacemans), 'человек')
print('Максимальный рост - ',max_Size,'см у ',name_of_Max)
print('Минимальный рост - ',min_Size,'см у ',name_of_Min)
print('Общий вес космонавтов:',total_Weight,'кг')
# Нужно вывести на консоль список всех космонавтов в формате
#     Космонавт AAA, рост - BBB см, вес - CC кг
# А затем нужно вывести общее число космонавтов,
# минимальный и максимальный рост (с указанием имен) 
# и общий вес космонавтов
# в формате
