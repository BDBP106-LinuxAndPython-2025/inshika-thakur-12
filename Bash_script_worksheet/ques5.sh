#!/bin/bash

#A script that takes a word and a filename, then prints the lines where the word appears.

read -p "Enter the name of the file:" Filename
read -p "Enter the word that you want to find:" Word
grep $Word $Filename
