#!/usr/bin/python3

"""Thinking along the same lines of the above question, how will you swap two columns in
a 2D array? Define a 3x3 matrix with random values, and swap first and second columns
in this array."""

import numpy as np

a=np.random.randint(1,10,(3,3))
print(f'Array with size 3X3: {a}')
a[:,[0,1]]=a[:,[1,0]]
print(f'Array with swapped first and second columns: {a}')