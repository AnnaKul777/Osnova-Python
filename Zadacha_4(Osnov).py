# 2.	Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

coordinateX1 = float(input('Введите координату x первой точки: '))
coordinateY1 = float(input('Введите координату y первой точки: '))
coordinateX2 = float(input('Введите координату x второй точки: '))
coordinateY2 = float(input('Введите координату y второй точки: '))

distancуСoordinates = ((coordinateX2-coordinateX1)**2 + (coordinateY2-coordinateY1)**2)**0.5
print(f'Расстояние между двумя точками в пространстве составляет -> {round(distancуСoordinates, 2)}')
