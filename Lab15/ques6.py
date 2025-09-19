#!/usr/bin/python

#Write a program to print the sum of the digits in a number.

A=int(input("Enter the number: "))
sum=0
while A > 0:
    r1=A%10 #gives the last digit (like when A is divided by 10)
    sum += r1 #adds the last digit(remainder) to sum 
    A=A//10 #It will reset the value of A to quotient of A when divided by 10, and this value will now enter while loop)
print (f"Sum of digits is: {sum}") 
#print("sum of digits: ", sum) can also be used instead of the other print statement

