#!/usr/bin/python

"""Write a program to find the maximum and minimum values of a dictionary."""

def max_min(**x):
    maximun_value = max(x.values())
    minimun_value = min(x.values())
    print(f'The maximum value is: {maximun_value}')
    print(f'The minimum value is: {minimun_value}')

max_min(a=56,b=34,c=4,d=23,e=425)