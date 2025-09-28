#!/usr/bin/python3

#Write a program to extract elements of a list, if it occurs more than k times.

A=int(input("Enter the number of elements: "))
K=int(input("Enter the number of occurences: "))
L=[]
C=0
for i in range(0,A):
    B=input("Enter the element: ")
    L.append(B)
Result=[]
for i in L:
    C=0
    for j in L:
        if i==j:
            C=C+1
    if C>K and i not in Result:
        Result.append(i)
print(Result)