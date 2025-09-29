#!/usr/bin/python3

#Write a script to find the sum of squares of first N numbers

N=int(input("Enter the number until which you want to find the sum of squares: "))
sum=0
for i in range(N+1):
    sum=sum+i**2
print(sum)
