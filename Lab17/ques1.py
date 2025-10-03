#!/usr/bin/python

"""Write a program to iterate over a dictionary and print the key-value pairs."""

def var(**x):
    for key,value in x.items():
        print(key, value)

var(apple='red',banana='yellow')