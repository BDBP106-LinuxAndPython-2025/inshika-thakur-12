#!/usr/bin/python3

"""Write a Python script that reads in a piece of text and prints it out masking out
email addresses. Thus and email address ”helloworld@python.com” should become
”h********d@python.com”."""

import re
text=input("Enter a piece of text: ")

def mask_email(match):
    email = match.group()
    name, domain = email.split('@')
    if len(name) > 2:
        name = name[0] + '*'*(len(name)-2) + name[-1]
    else:
        name = '*' * len(name)
    return name + '@' + domain
pattern=re.sub(r'[a-z0-9._%]+@[a-z0-9._]+\.[a-z]{2,}',mask_email, text)
print(pattern)