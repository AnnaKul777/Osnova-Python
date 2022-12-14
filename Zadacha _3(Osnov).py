# 1.	Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

numberFourth = int(input('Введите номер четверти (число от 1 до 4): '))

if numberFourth < 1 or numberFourth > 4:
    print('Введено не корректное число, строго введите число от 1 до 4')
elif numberFourth == 1:
    print(f'Диапазон возможных координат в {numberFourth} четверти: X > 0 and Y > 0')
elif numberFourth == 2:
    print(f'Диапазон возможных координат в {numberFourth} четверти: X < 0 and Y > 0')
elif numberFourth == 3:
    print(f'Диапазон возможных координат в {numberFourth} четверти: X < 0 and Y < 0')
elif numberFourth == 4:
    print(f'Диапазон возможных координат в {numberFourth} четверти: X > 0 and Y < 0')