# A. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#
# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
import random

def create_equation(n):
    equation = {}
    for i in range(n, -1, -1):
        if i == n:
            while True:
                koef = random.randint(-100, 100)
                if koef != 0:
                    break
            equation[i] = koef
        else:
            equation[i] = random.randint(-100, 100)
    return equation

a = int(input('Введите максимальную степень: '))
eq1 = create_equation(a)
print(eq1)
eq2 = create_equation(a)
print(eq2)

polynomial1 = []
for i in range(len(eq1) - 1, -1, -1):
    polynomial1.append(str(f'{eq1[i]}x**{i}'))
print(polynomial1)

polynomial2 = []
for i in range(len(eq2) - 1, -1, -1):
    polynomial2.append(str(f'{eq2[i]}x**{i}'))
print(polynomial2)

dict1 = {}
for i in range(len(polynomial1)):
    dict1[len(polynomial1) - (i + 1)] = polynomial1[i]
print(dict1)

dict2 = {}
for j in range(len(polynomial2)):
    dict2[len(polynomial2) - (j + 1)] = polynomial2[j]
print(dict2)

for i in range(len(dict1)):
    dict1[i] = dict1[i].split('x')
for j in range(len(dict2)):
    dict2[j] = dict2[j].split('x')

print(dict1)
print(dict2)

result = []

for n in range(len(dict1) - 1, -1, -1):
    sum = int(dict1[n][0]) + int(dict2[n][0])
    result.append(str(f'{sum}x**{n}'))
print(result)

result = ' + '.join(result)
print(f'Финальный ответ: {result}')
