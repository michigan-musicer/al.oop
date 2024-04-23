from triangle_solution import Triangle 
from rectangle import Rectangle

def main():
    shapes = []
    shapes.append(Rectangle("r1", 3, 4))
    shapes.append(Rectangle("r2", 5, 2))
    shapes.append(Triangle("t1", 4, 4, 4))
    shapes.append(Triangle("t2", 5, 3, 4))

    for shape in shapes:
        print(shape.get_type())
        print(shape.get_perimeter())
        print(shape.get_area())
