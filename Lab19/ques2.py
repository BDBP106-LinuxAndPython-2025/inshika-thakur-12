#!/usr/bin/python3

"""Convert the temperature from celsius to fahrenheit (like que1) but
using lambda expression."""

TempInCelsius=[23, 54, 100, 43]
result=list(map(lambda x: x*9/5+32, TempInCelsius))
print(f'The temperature in Fahrenheit is {result}')
