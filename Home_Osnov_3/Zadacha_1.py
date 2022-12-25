# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

size = int(input('Введите длину списка: '))
my_list = []
elem_list = []
summa_number = 0
for i in range(size):
    my_list.append(randint(-30, 30))

for i in range(len(my_list)):
    if i % 2 == 1:
        elem_list.append(my_list[i])
        summa_number += my_list[i]

print(f'Задан следующий список {my_list} -> на нечётных позициях элементы {elem_list} ответ: {summa_number}')

