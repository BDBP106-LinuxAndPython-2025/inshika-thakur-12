#!/usr/bin/python3

"""Q5.)Define a module called prime that contains a function isPrime() that returns whether
the passed argument is prime or not. Using this module and function, write another
program containing a function printPrimes() that prints the first n prime numbers.
A5.)"""
import primes

def printPrimes(n):
    count = 0
    num = 2
    while count < n:
        if primes.isPrime(num):
            print(num)
            count += 1
        num += 1

# Example usage
printPrimes(10)  # prints the first 10 prime numbers



