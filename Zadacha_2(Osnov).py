
# 1.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coordinateX = float(input('Введите координату Х: '))
coordinateY = float(input('Введите координату Y: '))

if coordinateX == 0 or coordinateY == 0:
    print('Число 0 является не корректным, введите любое целое число кроме 0 ;)')
elif coordinateX > 0 and coordinateY > 0:
    print('Точка расположена в I четверти плоскости')
elif coordinateX < 0 and coordinateY > 0:
    print('Точка расположена в II четверти плоскости')
elif coordinateX < 0 and coordinateY < 0:
    print('Точка расположена в III четверти плоскости')
elif coordinateX > 0 and coordinateY < 0:
    print('Точка расположена в IV четверти плоскости')
