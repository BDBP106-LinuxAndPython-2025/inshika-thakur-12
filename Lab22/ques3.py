#!/usr/bin/python3

"""Implement matrix multiplication of matrices A and B without using any external packages as an
instance method in a class called LinearAlgebra. Get the no. of rows and columns and elements of
each matrix from the user. Raise errors in case the condition for matrix multiplication is not met.
Once you have a working code for this, decorate a function that returns the matrices A and B using
@property. Then also define a setter function to allow the modification of A and B, since the user
may make mistakes in inputting the matrices and should be able to change elements as desired.
Lastly, define a custom decorator for calculating time in multlplying matrices A and B of size 50x50."""

import time

class LinearAlgebra:
    def __init__(self):
        self._A = None
        self._B = None

    @property
    def matrices(self):
        return self._A, self._B

    @matrices.setter
    def matrices(self, matrices_tuple):
        if len(A[0]) != len(B):
            raise ValueError("Matrix A and Matrix B must be same size")
        A, B = matrices_tuple
        self._A = A
        self._B = B

print("Enter dimensions for Matrix A")
row_A = int(input("Rows: "))
col_A = int(input("Columns: "))
print("\nEnter elements of Matrix A row-wise:")
A = [[int(input(f"A[{i + 1},{j + 1}]: ")) for j in range(col_A)] for i in range(row_A)]

print("\nEnter dimensions for Matrix B")
row_B = int(input("Rows: "))
col_B = int(input("Columns: "))
print("\nEnter elements of Matrix B row-wise:")
B = [[int(input(f"B[{i + 1},{j + 1}]: ")) for j in range(col_B)] for i in range(row_B)]

def multiplication_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Execution time: {:.6f}'.format(end_time - start_time))
        return result
    return wrapper

@multiplication_time
def mltply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += (A[i][k] * B[k][j])
    print("\nResultant Matrix:", result)

mltply(A, B)