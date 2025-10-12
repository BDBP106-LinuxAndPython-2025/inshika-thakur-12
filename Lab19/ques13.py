#!/usr/bin/python3

"""Write a program to concatenate a list of strings to make a sentence using
 reduce function."""

from functools import reduce

words = ["My", "name", "is", "Inshika", "Thakur"]

concat_str = reduce(lambda x, y: x + y, words)

print(concat_str)
