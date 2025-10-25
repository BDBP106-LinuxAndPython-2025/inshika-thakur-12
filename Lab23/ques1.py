#!usr/bin/python

"""Write a regular expression that accepting a 3-digit integer between 000 and 255.
Implement this in a script and test it for various possibilities"""

import re
a=input("enter a three digit number starting from 000-255")
pattern=r'^([0-1]\d{2}|2[0-4]\d|25[0-5])$'
if re.match(pattern,a):
    print("perfect match")
else:
    print("not perfect match")