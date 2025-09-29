#!/usr/bin/python3

#Write a script to convert the decimal number D into binary.

#METHOD 1 USING INTRINSIC FUNCTION
# D=str(input("Enter a decimal number: "))
# B=bin(int(D,10))
# print (f' The binary number is: {B}')

#METHOD 2
D=int(input("Enter the decimal number: "))
B=""
Q=1
while Q>0:
    Q=D//2
    R=D%2
    D=Q
    B=str(R)+B
print(f'The binary number is: {B}')


