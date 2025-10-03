#!/usr/bin/python

"""Remove all duplicate words from a given sentence using a dictionary. (Hint: Use the
set() function might be useful here.)"""

S="my name is inshika and inshika is my name"
word=S.split()
#splits the string and separates each word
N=set(word)
#convets the above word into set
F=" ".join(N)
print(F)