#!/usr/bin/python

"""Write a program with a function to calculate the area of a triangle using the formula,
where a, b, c are sides of the triangle, also providing a test case output from the program
Area=(s(s − a)(s − b)(s − c) where 2s = a + b + c)^1/2."""

import math
def area_of_triangle(a, b, c):
    s=(a+b+c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return Area

a,b,c=7,10,5
print(f'sides of triangle: a={a}, b={b}, c={c}')
print(f'Area of triangle: {area_of_triangle(a, b, c)}')




