#!usr/bin/python3

"""Q1.) Explain the various ways of importing module contents with examples."""
"""A1.) Various ways of importing module contents:
1. Import the entire module
import math
print(math.sqrt(59))

Import specific functions or constants
from math import sqrt, pi
print(sqrt(87), pi)

2. Import a module within a function
def area(r):
    import math
    return math.pi * r ** 2

3. Import from a package
from os import path
print(path.exists("file.txt"))"""