from math import sqrt

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        return self.y

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        else:
            self.y = value

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)

    # multiplication on left
    __rmul__ = __mul__

    def __truediv__(self, n):
        return Vector(self.x / n, self.y / n)

    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)
