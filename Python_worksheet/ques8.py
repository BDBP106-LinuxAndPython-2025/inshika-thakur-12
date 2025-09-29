#!/usr/bin/python3

#Write a program to find the sum and average of numbers in a list, L.

A=int(input("Enter the number of elements: "))
L=[]
S=0
for i in range(A):
    B=int(input("Enter the element: "))
    L.append(B)
for i in L:
    S=S+i
    A=S/len(L)
print(f'The sum of all numbers in list is: {S}')
print(f'The average of all numbers in list is: {A}')
