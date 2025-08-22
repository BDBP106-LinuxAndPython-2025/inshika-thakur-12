#!/bin/bash
#enter a nuber and check if it is negative, positive or zero

echo "Enter a number"
read n
echo "The file:" $n

if [ "$n" -gt 0 ]; then
	echo "The number is positive"
elif [ "$n" -eq 0 ]; then
	echo "The number is zero"
else 
	echo "The number is negative"
fi

