#!/usr/bin/python3

"""You are given two 1D arrays. Write a function to create a new array that contains the
maximum of the respective elements in the two arrays. For example, if a=[1,2] and
b=[0,5] then the new array will be c=[2,5]."""

import numpy as np

def max_array(a,b):
    print(f'The new array is: ',np.array([a.max(),b.max()]))

a=np.array([1,2])
b=np.array([0,5])
max_array(a,b)