#  1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


numberWeek = int(input('Введите число от 1 до 7: '))

if numberWeek >= 1 and numberWeek <= 5:
    print(f'{numberWeek} является рабочим днем недели')
elif numberWeek == 6 or numberWeek == 7:
    print(f'{numberWeek} является выходным днем недели')
elif numberWeek < 1 or numberWeek > 7:
    print(f'{numberWeek} это число не корректное, введите от 1 до 7')

