#!/usr/bin/python3

"""Check for the presence of a BisI restriction site using regular expression character groups:
A character group is a pair of square brackets with a list of characters inside them. dna
= ”ATCGCGAATTCAC” pattern = GCNGC, where N represents any base, i.e. A, T, G, C"""

import re
seq= "ATCGCGAATTCAC"
site=bool(re.search("GC[ATGC]GC",seq))
if site==True:
    print("The sequence has the site")
else:
    print("The sequence does not have a site")