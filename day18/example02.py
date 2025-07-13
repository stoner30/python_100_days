"""
平面上的点
"""


class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def distance_to(self, other):
        """该点与另一点的距离"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f'({self.x}, {self.y})'


point1 = Point(3, 5)
point2 = Point(6, 9)
print(point1.distance_to(point2))
