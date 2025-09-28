#!/usr/bin/python3

#Write a program to remove all occurrences of an element from a list, L.

a=int(input("enter number of elements: "))
w=(input("enter element to be removed: "))
L=[]
for i in range(0,a):
    b=input("enter elementl: ")
    L.append(b)

for i in L[:]:
    if i==w:
        L.remove(i)
print(L)