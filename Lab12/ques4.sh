#!/bin/bash

#Create a simple text file called nums.txt with few numbers in the same line, for example 2 3 5 7. Then read these numbers in a shell script into a variable array called numbers using the following command: read -ra numbers < nums.txt . Print the elements of this variable array, and using a for loop, print the result of doubling of each number in the array.

read -ra numbers < nums.txt

for numbers in $(cat nums.txt);
do
	echo "Original: $numbers"
	echo "Doubles: $[numbers * 2]"
done



