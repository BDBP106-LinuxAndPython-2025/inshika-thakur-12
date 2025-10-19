#!/usr/bin/python3

"""Write a list comprehension to create a list of names that start with ‘’H’ or ‘ase; in a
given list of protein names. For example,
proteins=["Hexokinase", "Amylase","Hemoglobin", "Catalase", "Actin"]"""

proteins = ["Hexokinase", "Amylase", "Hemoglobin", "Catalase", "Actin"]
filtered_proteins = [p for p in proteins if p.startswith('H') or p.endswith('ase')]
print(filtered_proteins)