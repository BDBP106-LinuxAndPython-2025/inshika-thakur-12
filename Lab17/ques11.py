#!/usr/bin/python

"""A magic date is a date where the date multiplied by the month is equal to the two-digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60 which is the two-digit year. Write a function that determines whether
or not a date is a magic date. Use your function to create a main program that finds
and displays all of the magic dates in the 20th century."""

def isMagicDate(day,month,year):
    last2dig = year % 100
    return day * month == last2dig

day=int(input("Enter day (1-31): "))
month=int(input("Enter month (1-12): "))
year=int(input("Enter full year (e.g., 1960): "))

if isMagicDate(day,month,year):
    print(f"{day:02d}/{month:02d}/{year} is a magic date!")
else:
    print(f"{day:02d}/{month:02d}/{year} is NOT a magic date.")


