# 3.	Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ
# ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

# from random import randint
#
# original_list = []
#
# for i in range(1, 7):
#     original_list.append(randint(-10, 100))
# print(f'Исходный список -> {original_list}')
#
# for j in range(1, 4):
#     temp = original_list[j-1]
#     original_list[j-1] = original_list[-j]
#     original_list[-j] = temp
# print(f'Новый список, после перемешивания список -> {original_list}')

# НОВОЕ РЕШЕНИЕ
from random import randint as Ra
from random import sample
orig_list = [Ra(-10, 100) for i in range(1, 7)]       # list complication
print(f'Исходный список -> {orig_list}')
res = sample(orig_list, len(orig_list))
print(f'Новый список, после перемешивания список -> {res}')

