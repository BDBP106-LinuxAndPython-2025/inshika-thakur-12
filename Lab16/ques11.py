#!/usr/bin/python3

#Write a program to print the duplicate elements in a list, L.

N=[]
D=[]
print("Enter numbers and type done once you are done: ")
while True:
    item=input(">")
    if item.lower()=="done":
        break
    N.append(item)
print(N)
for i in N:
    if N.count(i)>1:
        D.append(i)
print(D,"=Duplicate elements")