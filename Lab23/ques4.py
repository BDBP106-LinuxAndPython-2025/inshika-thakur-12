#!/usr/bin/python3

"""Write a Python script that accepts a line of CSV and checks if the 3rd field contains
exactly an email address or not, given that there are more than 3 fields."""

import re
l=input("enter a line from a CSV file")
pattern=r'^[a-z0-9\.\_\-\%]+@[a-z0-9\.\_]+\.[a-z]{2,}$'
field=l.split(',')
for i in range(len(field)):
    field[i]=field[i].strip()
if len(field)>3:
    third_field=field[2]
    if re.match(pattern,third_field):
        print("perfect match")
    else:
        print("no match")
else:
        print("does not have enough fields")