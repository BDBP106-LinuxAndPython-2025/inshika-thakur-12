#!/usr/bin/python3

"""(2) Here’s a DNA sequence with the bits that we want to extract in bold:
ACTGCATTATATCGTACGAAATTATACGCGCG Extract the bits of the string that match the
pattern (highlighted in bold) using findall():"""

import re
DnaSequence = "ACTGCATTATATCGTACGAAATTATACGCGCG"
pattern = "CG"
matches = re.findall(pattern, DnaSequence)
print(matches)
