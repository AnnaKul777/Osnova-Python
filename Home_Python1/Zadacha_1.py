# 1.	Создайте программу для игры с конфетами, человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока, делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint as Ra

def human(candy):
    hod_human = int(input('Сколько конфет вы хотите взять: '))
    if hod_human > 28:
        print('Количество конфет привышает максимальный объем шага (больше 28), введите количество меньше 28.')
        return human(candy)
    if hod_human <= 0:
        print('Не корректное количество конфет, введите число больше 0.')
        return human(candy)
    if hod_human > candy:
        print('Введено количество больше конфет, чем конфет в наличии. Введите корректное число.')
        return human(candy)
    candy -= hod_human
    print(f'Осталось {candy} конфет!')
    return candy

def bot(candy):
    hod_bot = Ra(1, 28)
    if candy <= 28: hod_bot = candy
    if candy <= 57 and candy >= 30:
        hod_bot = candy - 29
    print(f'Бот выбрал убрать со стола {hod_bot} конфет')
    candy -= hod_bot
    print(f'Осталось {candy} конфет!')
    return candy

position = Ra(1, 2)
pos_1 = 1
pos_2 = 2

amount_candy = int(input('Введите общее количество конфет: '))

if position == pos_1:
    print('Первый ход за тобой!!')
    while amount_candy > 0:
        a = human(amount_candy)
        if a == 0:
            print('Вы победили')
            break
        b = bot(a)
        if b == 0:
            print('Вы проиграли')
            break
        amount_candy = b

if position == pos_2:
    print('Первый ходит Бот')
    while amount_candy > 0:
        a = bot(amount_candy)
        if a == 0:
            print('Вы проиграли')
            break
        b = human(a)
        if b == 0:
            print('Вы победили')
            break
        amount_candy = b
