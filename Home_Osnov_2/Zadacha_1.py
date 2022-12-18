
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

print('Здравствуйте!')
number = float(input('Введите число:'))

summa = 0
if number < 0:
    number = number * -1

number = str(number)
number = number.split('.')
number = number[0] + number[1]
number = int(number)

while number > 0:
    summa += number % 10
    number = number // 10

print(f'Сумма цифр равна -> {int(summa)}')
