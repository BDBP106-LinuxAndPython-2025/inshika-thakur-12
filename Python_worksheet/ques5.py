#!/usr/bin/python3

#Write a script to find the first occurrence of a character, c, in a string S.

S=input("Enter the string: ")
C=input("Enter the character that you need to find: ")
I=S.find(C)
if I!=-1:
    print(f"The first occurrence of '{C}' is at index {I}.")
else:
    print(f"The character '{C}' is not found in the string.")