#!/usr/bin/python

#Write a program to check if an input letter is a vowel or consonant

letter=input("Enter the letter you want to check: ")
if letter in 'aeiouAEIOU':
    print("The letter is a vowel")
else:
    print("The letter is a consonant")
