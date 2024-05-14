from triangle_solution import Triangle
import math

class RightTriangle(Triangle):
    def __init__(self, base, height):
        self._side1 = base
        self._side2 = height
        self._side3 = math.sqrt(base ** 2 + height ** 2)

    def get_area(self):
        return self._side1 * self._side2 / 2
    