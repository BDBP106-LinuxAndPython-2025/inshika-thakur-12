#!/usr/bin/python

#Write a program to find the roots of a quadratic equation. Figure out what the inputs should be and also have provision to deal with cases where you end up getting complex roots.

import cmath

A=float(input("Enter value of A: "))
B=float(input("Enter value of B: "))
C=float(input("Enter value of C: "))
D=B**2 - 4*A*C
Root1=(- B - cmath.sqrt(D)) / (2*A)
Root2=(- B + cmath.sqrt(D)) / (2*A)
print("Roots: ", Root1, Root2)

