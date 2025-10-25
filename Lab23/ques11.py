#!/usr/bin/python3

"""Write a regular expression to split the DNA string wherever we see a base that isn’t A,
T, G or C. if the dna = ”ACTNGCATRGCTACGTYACGATSCGAWTCG”, the output
should be [’ACT’, ’GCAT’, ’GCTACGT’, ’ACGAT’, ’CGA’, ’TCG’]"""

import re
seq = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
bases=re.split("[^ATGC]+", seq )
print(bases)