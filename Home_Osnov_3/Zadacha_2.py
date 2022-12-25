# 2.	Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

def new_list(roster, size):
    for i in range(size):
        roster.append(randint(1, 10))

def products_of_numbers(roster, second_list):
    if len(roster) % 2 == 0:
        twise = len(roster) // 2
        for i in range(twise):
            second_list.append(roster[i] * roster[-i - 1])
    else:
        twise = len(roster) / 2
        j = 0
        while j < twise:
            second_list.append(roster[j] * roster[-j - 1])
            j += 1

length = int(input('Введите длину списка: '))
my_list = []
prod_number = []
new_list(my_list, length)
products_of_numbers(my_list, prod_number)
print(f'Задан следующий список => {my_list}')
print(f'Произведение пар чисел списка => {prod_number}')
