class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius

    def __contains__(self, point: Point) -> bool:
        return (point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2 <= self.radius ** 2


if __name__ == '__main__':
    circle = Circle(Point(0, 0), 2)
    print(Point(-1, 3) in circle)
    print(Point(-1, 3) in circle)
    print(Point(1, 1) in circle)
