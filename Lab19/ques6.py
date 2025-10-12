#!/usr/bin/python3

"""Write a function called cell_metabolism that takes the number of glucose and
oxygen molcules, that contains an inner function energy_output() to calculate
ATP yield (assume 1 glucose+6 oxygen gives 38 ATP). The function should
return the total ATP produced."""

def cell_metabolism(O,G):
    ATP=0
    while G>0 and O>=6:
        G=G-1
        O=O-6
        ATP=ATP+38

    return ATP
Oxygen=int(input("Enter the number of oxygen molecules: "))
Glucose=int(input("Enter the number of glucose molecules: "))

ATP=cell_metabolism(Oxygen, Glucose)
print(f'Total ATP produced: {ATP}')