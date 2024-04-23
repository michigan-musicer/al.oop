# Task 3: include the Triangle class.
from rectangle import Rectangle

def main():
    shapes = []
    shapes.append(Rectangle("r1", 3, 4))
    shapes.append(Rectangle("r2", 5, 2))
    # Task 3: create two Triangle objects named t1 and t2.
    # t1 should have side lenghts 4, 4, 4, and t2 should have
    # side lengths 5, 3, 4.

    # When running the code below, t1 should have a perimeter of 12 and an area of about 6.93.
    # t2 should have a perimeter of 12 and an area of exactly 6.

    for shape in shapes:
        print(shape.get_type())
        print(shape.get_perimeter())
        print(shape.get_area())
