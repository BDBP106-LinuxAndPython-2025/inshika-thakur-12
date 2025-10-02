#!/bin/bash

#A script that counts the number of words, lines and characters in a given text file.

read -p "Enter the text file name: " File
Lines=$(wc -l < $File)
Character=$(wc -m < $File)
Words=$(wc -w < $File)
echo "The number of lines in the text file: $Lines"
echo "The number of characters in the text file: $Character"
echo "The number of words in the text file: $Words"
