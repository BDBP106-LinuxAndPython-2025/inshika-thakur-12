#!/usr/bin/python

#Write a program to find the distance between 2 points, input is coordinates for the two points.

import math
x1=int(input("Enter the x1 coordinate: "))
x2=int(input("Enter the x2 coordinate: "))
y1=int(input("Enter the y1 coordinate: "))
y2=int(input("Enter the y2 coordinate: "))

distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
print(f'distance = {distance}')
