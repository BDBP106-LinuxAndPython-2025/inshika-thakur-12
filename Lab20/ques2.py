#!/usr/bin/python3

"""(2) Creating your own package. Create a package (folder) called utils with an empty
__init__.py. Inside utils create two python files called math_utils.py and string_utils.py.
The former should contain functions to perform operations such as addition, subtraction,
multiplication, division and getting remainder with two numbers as inputs. The latter file
should contain functions to convert lower case to upper case, upper case to lower case and
to concatenate strings. In a different program, import math_utils and string_utils to
use the modules to print the output for the following: a) 34 and 45, b) ’BDBH’ and ’101’."""

from utils import math_utils, string_utils

a,b=34,45
print("\nMath Operations:")
print(f'Addition: {math_utils.add(a,b)}')
print(f'Subtraction: {math_utils.subtract(a,b)}')
print(f'Multiplication: {math_utils.multiply(a,b)}')
print(f'Division: {math_utils.divide(a,b)}')
print(f'Remainder: {math_utils.remainder(a,b)}')

x1,x2='BDBH','101'
print(f'\nString Operations:')
print(f'To convert the string to lowercase: {string_utils.to_lowercase(x1)}')
print(f'To convert the string to uppercase: {string_utils.to_uppercase(x2)}')
print(f'To concatenate the two strings: {string_utils.concatenate(x1,x2)}')