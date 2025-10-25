#!/usr/bin/python3

"""Write a Python script to check if a given string contains an email address or not."""

import re
mid=input("enter a string")
pattern=r'[a-z0-9\.\_\-\%]+@[a-z0-9\.\_]+\.[a-z]{2,}'
match=re.search(pattern,mid)
if match:
    print("the string contains an email address:", match.group())
else:
    print("the string does not contain email address")