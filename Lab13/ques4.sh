#!/bin/bash

#Visit the PDB website, and download the protein with ID 1HK0 in the pdb format. With this, use gawk to extract the atoms of all phenyl alanine residues of this protein and save it in a new file called PHE_atoms.xyz

gawk '$4 == "PHE" && $1 == "ATOM" {print $7 $8 $9}' 1HK0.pdb > PHE_atoms.xyz
#$1 == "ATOM" - se;ects only atom records. $4 == "PHE" - selects only PHE residues.
