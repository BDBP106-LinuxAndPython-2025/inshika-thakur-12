#!/usr/bin/python

#Write a code to get the Fibonacci numbers beginning with f0 = 0 and f1 = 1 up to f25.Note: You’ll have to think about how to swap numbers. In case you are not familiar,Fibonacci numbers are those belonging to the Fibonacci series where each number is thesum of the previous two numbers. For example, 1,2,3,5,8,. . . . In this question, theFibonacci series will start from the numbers 0,1.

a=[0,1]
for i in range(2,25):
    a.append(a[i-1]+a[i-2])
print(a)
