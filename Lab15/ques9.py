#!/usr/bin/python

#Write a program to reverse a number and print the reversed number.

num=int(input("Enter a number: "))
reversed_num=0
while num > 0:
    r1=num%10
    reversed_num=(reversed_num*10)+r1
    num=num//10
print(reversed_num)
    

