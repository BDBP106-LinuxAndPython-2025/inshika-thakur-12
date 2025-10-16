#!/usr/bin/python3

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ValueError("Can't divide by zero")
    return a/b

def remainder(a,b):
    return a%b