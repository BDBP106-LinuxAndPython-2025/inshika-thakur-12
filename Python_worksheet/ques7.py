#!/usr/bin/python3

#Write a script to replace all occurrences of a character, c, with another character, d.

S=input("Enter a string: ")
C=input("Enter the character that you need to replace: ")
D=input("Enter another character that you need to replace with: ")

if C in S:
    S=S.replace(C,D)
    print(f'The new script with replaced characters is: {S}')
else:
    print(f'The character {C} is not in {S}')