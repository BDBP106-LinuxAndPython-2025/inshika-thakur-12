#!/usr/bin/python

#Write a script to check if a number is palindrome or not.

num=int(input("Enter the number: "))
original=num
reversed_num=0
while num > 0:
    r1=num%10
    reversed_num=(reversed_num*10)+r1
    num=num//10
    
if original==reversed_num:
    print(f"Your number {original} is a palindrome")
else:
    print(f"Your number {original} is not a palindrome")


