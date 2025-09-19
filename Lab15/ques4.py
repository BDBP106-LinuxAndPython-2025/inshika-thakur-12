#!/usr/bin/python

#Take input in degrees and print the values of all 6 trigonometric functions for this angle. Remember to write line of code to convert your input to radians before finding trigonometric values

import math

Degree=float(input("Enter angle in degrees: "))

Radian=math.radians(Degree)
print("sin",math.sin(Radian))
print("cos",math.cos(Radian))
print("tan",math.tan(Radian))
print("cosec", 1/math.cos(Radian))
print("sec", 1/math.cos(Radian))
print("tansec", 1/math.tan(Radian))
