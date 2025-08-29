#!/bin/bash

read -ra numbers < nums.txt

for numbers in $(cat nums.txt);
do
	echo "Original: $numbers"
	echo "Doubles: $[numbers * 2]"
done



