#!/usr/bin/python

"""Write a program to sum all the values of a dictionary."""

def sum1(**x):
    sum = 0
    for V in x.values():
        sum += V
    print(sum)

sum1(a=1,b=4,c=87)
