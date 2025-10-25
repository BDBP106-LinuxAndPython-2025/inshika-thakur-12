#!/usr/bin/python3

"""Write a regular expression that matches integers from 0 to 255. (Note that this is different
from the question above. Implement this in a script and test for various possibilities."""

import re
a=input("enter a nummber from 0 to 255")
pattern=r'^(\d|0\d|\d{2}|[0-1]\d{2}|2[0-4]\d|25[0-5])$'
if re.match(pattern,a):
    print("perfect match")
else:
    print("no match")