#!/bin/bash

#A script that takes a .csv file and prints only the first and third columns.

read -p "Enter a csv file: " File
if [ ! -f $File ]; then
	echo "The file does not exist"
else
	awk '{ print $1, $3 }' "$File"
fi
