#!/bin/bash
#to check if a file exists and if a file is executable

echo "Input the file name"
read n
echo "The file:" $n

if [ -f "$n" ]; then
	echo "The file exists"
if [ -x "$n" ];then
	echo "File is executable"
else 
	echo "File is not executable"
fi
else 
	echo "File does not exist."
fi
