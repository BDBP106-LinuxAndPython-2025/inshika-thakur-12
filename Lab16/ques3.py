#!/usr/bin/python3

#Write a script to check if a given number, N, is prime or not

N=int(input("Enter the number: "))
is_prime=True
if N<=1:
    print(f'{N} is not a prime number')
elif N==2:
    print(f'{N} is a prime number')
elif N%2==0:
    print(f'{N} is not a prime number')
else:
    for i in range(3,N):
        if N%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(f'{N} is prime number')
    else:
        print(f'{N} is not a prime number')
