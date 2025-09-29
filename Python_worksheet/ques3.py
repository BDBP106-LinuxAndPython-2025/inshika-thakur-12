#!/usr/bin/python3

#Write a script that computes the number of 1s in a binary representation of a decimal number, N.

D=int(input("Enter the decimal number: "))
B=""
Q=1
C=0
#C IS COUNT

while Q>0:
    Q=D//2
    R=D%2
    if R==1:
        C=C+1
    D=Q
    B=str(R)+B
print(f'The binary number is: {B}')
print(f'The number of 1s in binary number of the given decimal number is: {C}')