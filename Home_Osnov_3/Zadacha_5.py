# 5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи.

lenght = int(input('Введите длину списка: '))

fibon = []
nefibon = []
fibon.append(0)
fibon.append(1)
nefibon.append(0)
nefibon.append(1)

for i in range(lenght-1):
    f = fibon[i] + fibon[i + 1]
    fibon.append(f)

for j in range(lenght - 1):
    fi = nefibon[j] - nefibon[j + 1]
    nefibon.append(fi)

for k in range(1, len(fibon)):
    fibon.insert(0, nefibon[k])

print(f'Список: {fibon}')



