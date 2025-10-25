#!/usr/bin/python3

"""Check for the presence of an AvaII recognition site, which can have two different se-
quences: GGACC and GGTCC. Use regular expressions. dna = ”ATCGCGAATTCAC” pattern = GGACC
and GGTCC"""

import re
seq ="ATCGCGAATTCAC"
pattern = "GGACC"or "GGTCC"
site=bool(re.search("GAACC|GGTCC",seq))
if site==True:
    print("The Ava II site is present.")
else:
    print("The Ava II site is not present")