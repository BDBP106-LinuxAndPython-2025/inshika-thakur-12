#!/usr/bin/python3

"""We know how to reverse the elements in a 1D array- a[::-1]. How would you reverse
the rows in a 2D array? How would you reverse the columns in a 2D array?"""

import numpy as np
b=np.arange(4)
c=b.reshape(2,2)
print(f'The array to be reversed: {c}')
print(f'------------------------------')

#To reverse the rows
A=c[::-1]
print(f'The array with reversed rows: {A}')
print(f'---------------------------------')

#To reverse the columns
A=c[:,::-1]
print(f'The array with reversed columns: {A}')