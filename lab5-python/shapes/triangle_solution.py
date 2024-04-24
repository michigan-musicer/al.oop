from shape import Shape
import math

class Triangle(Shape):
    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def get_shape_type(self):
        return "Triangle"
    
    def get_perimeter(self):
        return self._side1 + self._side2 + self._side3
    
    def get_area(self):
        return math.sqrt( (self._side1  + self._side2 + self._side3) \
                        * (-self._side1 + self._side2 + self._side3) \
                        * (self._side1  - self._side2 + self._side3) \
                        * (self._side1  + self._side2 - self._side3)) / 4
