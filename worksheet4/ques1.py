#!/usr/bin/pyhton3

"""Write a list comprehension to extract all even gene lengths from a list of genes.
For example, gene_lengths=[450,300,725,1024,512,815]."""

gene_lengths = [450, 300, 725, 1024, 512, 815]
even_gene_lengths = [len for len in gene_lengths if len % 2 == 0]
print(even_gene_lengths)