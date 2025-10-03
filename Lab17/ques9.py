#!/usr/bin/python

"""A DNA sequence encodes each amino acid making up a protein as a three-nucleotide sequence called a codon. For example,
the sequence fragment AGTCTTATATCT contains the codons AGT, CTT, ATA, TCT if read from the first position. If read from
the second position, it yields the codons GTC, TTA, TAT and if read from the third position we get TCT, TAT, ATC.
Write a function to extract the codons into a list of 3-letter strings given a sequence and from what position
(input as an integer) the sequence should be read. As an example, output the 3-letter strings from the sequence
GTTTCGATTATAACG read from the (i) 1st position and (ii) 3rd position."""

def extract_codons(seq, position):
    startIndex=position-1
    codons=[]
    for i in range(startIndex, len(seq) - 2, 3):
        codon=seq[i:i+3]
        codons.append(codon)
    return codons

seq="GTTTCGATTATAACG"

codons_1=extract_codons(seq,1)
print("Codons from 1st position:", codons_1)

codons_3=extract_codons(seq, 3)
print("Codons from 3rd position:", codons_3)

