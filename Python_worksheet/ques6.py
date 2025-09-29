#!/usr/bin/python3

#Write a script to find the highest frequency character in a string, S.

S=input("Enter the string: ")
for i in S:
    H=S.count(i)
print(H)
