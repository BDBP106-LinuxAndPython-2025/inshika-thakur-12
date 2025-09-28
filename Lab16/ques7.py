#!/usr/bin/python3

#Write a script to trim leading whitespace characters from a string, S.

S=input("Enter a string with leading whitespace: ")
l=len(S)
for i in range(0,l):
    while S[i]==" ":
        i=i+1
    print(S[i:])
    break