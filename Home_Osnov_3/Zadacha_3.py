# 3.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

def list_number(new_list, number):
    for i in range(number):
        new_list.append(round(uniform(1, 10), 2))

size = int(input('Введите длину списка: '))
my_list = []
list_number(my_list, size)
my_list = list(map(str, my_list))

for i in range(len(my_list)):
    my_list[i] = my_list[i].split('.')
    my_list[i][0] = '0.'
    my_list[i] = my_list[i][0] + my_list[i][1]
my_list = list(map(float, my_list))

max_numb = my_list[0]

for num1 in my_list:
    if my_list[0] != 0:
        min_numb = my_list[0]
    else:
        pass

for num2 in my_list:
    if num2 > max_numb:
        max_numb = num2
    elif num2 < min_numb and num2 != 0:
        min_numb = num2
difference = max_numb - min_numb

print(f'Список => {my_list} max {max_numb} и min {min_numb}, разница между элементами => {difference}')
