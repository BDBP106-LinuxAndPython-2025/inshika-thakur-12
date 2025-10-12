#!/usr/bin/python3

"""Write a program to find the sum of all the elements in a list using
lambda and reduce functions."""

from functools import reduce
List=[14, 565, 54, 406, 230]

Sum=reduce(lambda x, y: x + y,List)

print("Sum of all elements:", Sum)
