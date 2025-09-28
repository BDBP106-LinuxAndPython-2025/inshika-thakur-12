#!/usr/bin/python3

#Write print alternate characters of a string, S.

S=input("Enter a string: ")
h=len(S)
for i in range(0,h,+2):
    print(S[i],end=" ")