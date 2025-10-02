#!/bin/bash

#Ask the user for a filename, and check if it exists. If it exists, is the file readable and writable.

read -p "Enter a filename: " File
if [ -e $File ]; then
	echo "The file exists."
	if [ -r $File ]; then
		echo "The file is readable."
	else
		echo "The file is not readable."
	fi
	if [ -w $File ]; then
		echo "The file is writable."
	else
		echo "The file is not writable."
	fi
else
	echo "The file does not exist."
fi
