#!/bin/bash
#Difference between -e,-s and -f.

#example
echo "Input file name:"
read n
#-e checks whether a file exists or not.(regardless of the type of file, directory etc.)
if [ -e "$n" ]; then
	echo "The file exists"
else 
	echo "File does not exist."
fi
#-s checks if a file exists and if it is empty or not.
if [ -s "$n" ]; then
	echo "File is not empty."
else 
	echo "File is empty"
fi
#-f checks if the file is regular or not. 
if [ -f "$n" ]; then
	echo "It is a regular file"
else
	echo "The file is not a regular file."
fi




