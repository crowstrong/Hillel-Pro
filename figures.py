import math
from abc import ABC, abstractmethod


class IShape(ABC):
    @abstractmethod
    def square(self):
        return 0


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def square(self):
    #     return 0

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Parallelogram(Shape):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y)
        self.height = height
        self.width = width
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def square(self):
        return self.width * self.height

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Rectangle(Parallelogram):

    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width, 90)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, x, y, a, b, c):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


if __name__ == '__main__':
    r = Rectangle(0, 0, 10, 20)
    r1 = Rectangle(10, 0, -10, 20)
    r2 = Rectangle(0, 20, 100, 20)
    print(r.square())
    print(r1.square())
    print(r2.square())

    c = Circle(10, 0, 10)
    c1 = Circle(100, 100, 5)
    print(c.square())
    print(c1.square())

    p = Parallelogram(1, 2, 20, 30, 45)
    p1 = Parallelogram(1, 2, 10, 20, 40)
    print(p.square())
    print(p1.square())

    t = Triangle(0, 0, 3, 4, 5)
    print(t.square())
