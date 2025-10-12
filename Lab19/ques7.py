#!/usr/bin/python3

"""Write a function analyse_dna(sequence) that defines an inner function
gc_content() to calculate GC% . The outer function should print whether the
given DNA is AT rich or GC rich sequence."""

def analyse_dna(sequence):
    def gc_content(sequence):
        gc_count=sequence.count('G')+sequence.count('C')
        return (gc_count / len(sequence))*100

    percent_gc=gc_content(sequence)

    if percent_gc>50:
        print(f"The DNA is GC rich. GC%={percent_gc}")
    else:
        print(f"The DNA is AT rich. AT%={percent_gc}")

analyse_dna("ATGCCGACTACGTACGACTAGCTAG")