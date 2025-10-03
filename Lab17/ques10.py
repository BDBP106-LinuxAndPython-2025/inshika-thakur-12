#!/usr/bin/python

"""Write a function called nextPrime that finds and returns the first prime number larger
than some integer, n. The value of n will be passed to the function as its only parameter.
The main program should read an integer from the user and display the first prime
number larger than the entered value."""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nextPrime(n):
    next = n + 1
    while True:
        if is_prime(next):
            return next
        next += 1

#MAIN PROGRAM
n = int(input("Enter an integer: "))
result = nextPrime(n)
print(f"The first prime number larger than {n} is {result}.")