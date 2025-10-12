#!/usr/bin/python3

"""Write a program to filter out the odd elements of the Fibonacci series
 for the first n terms."""

n=int(input("Enter number of terms: "))
Fibonacci=[0, 1]
for i in range(2, n):
    Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])

EvenFibonacci = list(filter(lambda x: x % 2 == 0, Fibonacci[:n]))

print("Fibonacci series:", Fibonacci[:n])
print("Even elements:", EvenFibonacci[:n])