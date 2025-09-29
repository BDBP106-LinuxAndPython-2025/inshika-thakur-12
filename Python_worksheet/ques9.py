#!/usr/bin/python3

#Write a program to find the minimum and maximum number in a list, L.

B=input("Enter the elements of the list: ").split()
min=int(B[0])
max=int(B[0])
for i in B:
    if int(i)<min:
        min=int(i)
    if int(i)>max:
        max=int(i)
print(f'The minimum element is {min}')
print(f'The maximum element is {max}')