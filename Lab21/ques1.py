#!/usr/bin/python3

"""Create a class called Quadrilateral that takes in four parameters - side1, side2, side3 and
side4. Write two functions isSquare() and isRectangle() that checks for all the sides
being equal (for a square) and the opposite sides being equal (for a rectangle), and returns
True/False. Create an instance of the Quadrilateral with (a) all sides being different,
(b) Opposite sides being same, (c) all sides being the same. Print the appropriate output."""


class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def isSquare(self):
        return self.side1 == self.side2 == self.side3 == self.side4

    def isRectangle(self):
        return (self.side1 == self.side3 and self.side2 == self.side4
        or self.side1 == self.side2 and self.side3 == self.side4
        or self.side1 == self.side4 and self.side2 == self.side3
        and not self.isSquare())

print("a)")
x=Quadrilateral(2,7,2,3)
print("is square:",x.isSquare())
print("isRectangle():",x.isRectangle())

print("b)")
x=Quadrilateral(4,3,4,3)
print("is square:",x.isSquare())
print("isRectangle():",x.isRectangle())

print("c)")
x=Quadrilateral(8,8,8,8)
print("is square:",x.isSquare())
print("isRectangle():",x.isRectangle())