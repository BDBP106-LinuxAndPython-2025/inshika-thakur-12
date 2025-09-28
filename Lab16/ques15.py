#!/usr/bin/python3

#Write a program to extract words from a string list, L whose first character is k.

a=int(input("enter number of elements: "))
w=(input("enter first letter of elements to be removed: "))
L=[]
for i in range(0,a):
    b=input("enter element: ")
    L.append(b)

for i in L[:]:
    if i.startswith(w):
        L.remove(i)
print(L)