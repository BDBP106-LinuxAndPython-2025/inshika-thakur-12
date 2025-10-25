#!/usr/bin/python3

"""Test if a DNA sequence contains an EcoRI restriction site using regular expressions. dna
= ”ATCGCGAATTCAC” pattern = GAATTC"""

seq="ATCGCGAATTCAC"
pattern = "GAATTC"
import re
site=bool(re.search(pattern,seq))
if site==True:
    print("Eco R1 site is present in the sequence.")
else:
    print("Eco R1 site is not present in the sequence.")