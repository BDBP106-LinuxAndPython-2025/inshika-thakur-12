#!/usr/bin/python3

"""Explore the set_printoptions() function to pretty-print a numpy array by
suppressing the scientific notation (like 1e10)."""

import numpy as np

np.set_printoptions(suppress=True)
a=np.array([1e1,1e2,1e3], dtype=np.int16)
print(f'pretty print: {a}')