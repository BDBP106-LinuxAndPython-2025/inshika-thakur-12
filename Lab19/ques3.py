#!/usr/bn/python3

"""Write a program to convert a tuple of angles into a list of tuples with
each tuple containing the sine and cosine of an angle"""

import math

def SinCosineTup(tupleOfAngles):
    result = []
    for angle in tupleOfAngles:
        sinValue = math.sin(angle)
        cosValue = math.cos(angle)
        result.append((sinValue, cosValue))
    return result

angles = (0, math.pi/5, math.pi/2, math.pi/8, math.pi/56)

# Convert
sinCosineList = SinCosineTup(angles)
print(sinCosineList)