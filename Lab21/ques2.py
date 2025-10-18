#!/usr/bin/python3

"""Idea of inheritance- parent and child classes. Extend the Quadrilateral class with two
child classes - Square and Rectangle. In the constructor of the child classes, call the
parent’s constructor with a single side or 2 sides as the case may be. Define functions
getArea() in the child classes that return the area of the square or the rectangle."""

class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

class Square(Quadrilateral):
    def __init__(self, side):
        super().__init__(side, side, side, side)

    def getArea(self):
        return self.side1 ** 2

class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)

    def getArea(self):
        return self.side1 * self.side2


sq = Square(5)
print("Area of the given square is:", sq.getArea())

rect = Rectangle(4, 6)
print("Area of the given rectangle is:", rect.getArea())
