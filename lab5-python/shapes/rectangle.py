from shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self._width = width
        self._height = height
    
    def get_shape_type(self):
        return "Rectangle"

    def get_perimeter(self):
        return self._width * 2 + self._height * 2
    
    def get_area(self):
        return self._width * self._height
