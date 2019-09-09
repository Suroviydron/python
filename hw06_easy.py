__author__ = 'Ablezgov Andrey'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt

class Triangle:

    def __init__(self, point1, point2, point3, a = None, b = None, c = None, p = None, s = None, h = None):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

        self.a = sqrt((self.point2[0] - self.point1[0])**2 + (self.point2[1] - self.point1[1])**2)
        self.b = sqrt((self.point3[0] - self.point2[0])**2 + (self.point2[1] - self.point3[1])**2)
        self.c = sqrt((self.point3[0] - self.point1[0])**2 + (self.point3[1] - self.point1[1])**2)

    def Perimeter(self):
        self.p = (self.a + self.b + self.c)
        return round(self.p, 1)

    def Square(self):
        p2 = self.p / 2
        self.s = sqrt(p2 * (p2 - self.a) * (p2 - self.b) * (p2 - self.c))
        return round(self.s, 1)

    def High(self):
        self.h = 2 * self.s / self.a
        return round(self.h, 1)

Triangle1 = Triangle([2, 1],[6, 6],[9, 0])
print(f'Периметр первого треугольника: {Triangle1.Perimeter()}')
print(f'Площадь первого треугольника: {Triangle1.Square()}')
print(f'Высота первого треугольника: {Triangle1.High()}')

Triangle2 = Triangle([0, 0],[0, 3],[3, 0])
print(f'Периметр второго треугольника: {Triangle2.Perimeter()}')
print(f'Площадь второго треугольника: {Triangle2.Square()}')
print(f'Высота второго треугольника: {Triangle2.High()}')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:

    def __init__(self, point1, point2, point3, point4, a = None, b = None, c = None, h = None, p = None, s = None):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

        self.a = self.point4[0] - self.point3[0]
        self.b = self.point2[0] - self.point1[0]
        self.h = self.point1[1] - self.point3[1]
        self.c = round(sqrt(self.h**2 + (self.point1[0] - self.point3[0])**2), 1)

    def Perimeter(self):
        self.p = self.a + self.b + self.c * 2
        return self.p

    def Square(self):
        self.s = (self.a + self.b)/2 * self.h
        return round(self.s, 1)

Trap1 = Trapeze([2,7], [6, 7], [1, 1], [7, 1])
print(f'Длины сторон: нижней - {Trap1.a}, верхней - {Trap1.b}, боковых - {Trap1.c}')
print(f'Периметр трапеции: {Trap1.Perimeter()}')
print(f'Площадь трапеции: {Trap1.Square()}')