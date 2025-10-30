#!/usr/bin/python3

"""(2) Array creation and manipulation exercises. Print all the arrays in each exercise."""

"""(i) Create a 1D array from 0 to 9."""
import numpy as np
a = np.arange(10)
print(f'i) 1D array from 0 to 9 is: {a}')
print(f'------------------------------------------------------------------------------')

"""(ii) Create a boolean array of size 3x3."""
b=np.ones((3,3), dtype=bool)
print(f'ii) boolean arrat of size 3X3: {b}')
print(f'------------------------------------------------------------------------------')

"""(iii)Using syntax from list comprehension, create an array that satisfies the condition.
For example,
arr = np.arange(10)
arr = arr[ arr%2 == 1 ]
Create an array of prime numbers from 1 to 50 using a similar approach."""
a=np.array([i for i in range(10) if i%2==0])
print(f'iii) The array created using list comprehension: {a}')
#array of prime numbers from 1 to 50
primes = np.array([x for x in range(1, 51) if x > 1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))])
print(f'Array of prime numbers: {primes}')
print(f'------------------------------------------------------------------------------')

"""(iv)Create a 1D array with 20 random elements, and reshape it as a 4x5 array. Print the two arrays."""
a=np.random.randint(0,100,20)
print(f'iv) Array with 20 random elements: {a}')
#to change reshape it to 4X5
b=a.reshape(4,5)
print(f' Array reshaped as a 4X5 array: {b}')
print(f'------------------------------------------------------------------------------')

"""(v)Create two 1D arrays a and b where a has numbers ranging from 0 to 9 and b has only 1s. Then stack 
the two arrays horizontally."""
a=np.arange(10)
b=np.ones(10,dtype=int)
print(f'v) Array with numbers ranging from 0 to 9: {a}')
print(f' Array with only 1s: {b}')
#to horizontally stack the two arrays:
c=np.hstack((a,b))
print(f'Horizontally stacked two arrrays: {c}')
print(f'-----------------------------------------------------------------------------')

"""(vi)Define two 1D arrays, where array a has list of first 100 numbers, and b has first 100 prime numbers.
Obtain a new array that is the intersection of these two arrays (Hint: use np.intersect1d())"""
a=np.arange(1,101)
b=np.array([x for x in range(1,1000) if x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))])
A=(b[:100])
print(f'vi) Array having first 100 prime numbers: {a}')
print(f' Array having first 100 prime numbers: {A}')
c=np.intersect1d(a,b)
print(f'The intersection of the two arrays a and b is: {c}')
print(f'-----------------------------------------------------------------------------')

"""(vii) Use the above two arrays with the aim this time to remove items from a that are in b. (We are doing a-b
operation, use np.setdiff1d())"""
a=np.arange(1,101)
print(a)
b=np.array([x for x in range(1,1000) if x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))])
A=(b[:100])
print(A)
c=np.setdiff1d(a,b)
print(f'vii) New array with items that has all elements of a except those that are not in b: {c}')
print(f'-----------------------------------------------------------------------------')

"""(viii)Use the above two arrays with the aim of getting the indices of common elements between the two
arrays. (Hint: Use np.where(a==b))"""
a=np.arange(1,101)
b=np.array([x for x in range(1,1000) if x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))])
A=(b[:100])
c=np.where(a==A)
print(f'viii) New array with indices of common elements: {c}')
print(f'-----------------------------------------------------------------------------')

"""(ix)Extract the elements of the array a above that are greater than 5 and less than 20."""
a=np.arange(1,101)
b=(a[5:19])
print(f'ix)Array that has elements greater than 5 and less than 20: {b}')
print(f'-----------------------------------------------------------------------------')
