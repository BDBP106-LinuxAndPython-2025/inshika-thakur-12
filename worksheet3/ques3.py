#!/usr/bin/python

"""Define a dictionary containing 10 fruits and their colours. Make sure that the colours
are repeated as values. Write a loop to iterate over the key-value pairs, and check which
all fruits are green in colour (this means that your dictionary should contain at least two
fruits with green as its value (for this example to work well)."""

D={"apple":"red", "cherry":"red", "mango":"yellow", "pear":"green", "avocado":"green", "tangerine":"orange", "banana":"yellow", "blueberry":"blue", "blackberry":"purple", "kiwi":"green"}
L={}
for key,value in D.items():
    if value=="green":
        L[key]=value
print(f'All fruits that are green in colour:' ,L)
