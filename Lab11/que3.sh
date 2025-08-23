#!/bin/bash
#To check if a string is empty or not.

#-z operator

echo "Input string name:"
read n

if [ -z "$n" ]; then
	echo "String is empty."
else
	echo "String is not empty."
fi

#-n operator

echo "Input string name:"
read n

if [ -n "$str" ]; then
	echo "String is not empty."
else
	echo "String is empty."
fi

