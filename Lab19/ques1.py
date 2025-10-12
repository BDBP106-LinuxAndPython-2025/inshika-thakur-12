#!/usr/bin/python3

"""1) Write a program to convert temperature in Celsius to
Fahrenheit using map function."""

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
TempInCelsius=[23, 54, 100, 43]
result=list(map(celsius_to_fahrenheit,TempInCelsius))
print(f' The result in fahrenheit is {result}')