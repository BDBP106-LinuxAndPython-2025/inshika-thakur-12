#!/usr/bin/python3

"""Write a program to extract all vowels in a given string using list comprehension."""

def ExtractVowels(strng):
    vowels = "aeiouAEIOU"
    return [char for char in strng if char in vowels]

result=ExtractVowels(input("Enter the string: "))
print(result)

