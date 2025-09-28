#!/usr/bin/python3

#Write a program to find the even numbers in a list, L.

L=[2,76,23,58,32,68,44]
for i in L:
    if ((i%2)==0):
        print(i,"=even number")
    else:
        print(i,"=odd number")