#!/usr/bin/python3

"""Write a Python script that scans through a given piece of text and extracts
all unique email addresses from it."""

import re
text=input("enter a text")
pattern=r'[a-z0-9\.\_\-\%]+@[a-z0-9\.\_]+\.[a-z]{2,}'
emails=re.findall(pattern,text)
unique=set(emails)
if unique:
    print("unique emails")
    for email in unique:
        print(email)
else:
    print("no unique emails")
