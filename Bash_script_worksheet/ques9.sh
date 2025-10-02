#!/bin/bash

#Create an array of 5 numbers. The script should print the largest number, smallest number and sum of all numbers in the array.

N=(5 18 22 15 19)
sum=0
max=${N[0]}
min=${N[0]}

for i in "${N[@]}"; do
	sum=$((sum + i))

	if [ "$i" -gt "$max" ]; then
		max=$i
	fi
	if [ "$i" -lt "$min" ]; then
		min=$i
	fi
done

echo "Array: ${N[0]}"
echo "Largest number in the array: $max"
echo "Smallest number in the array: $min"
echo "sum of numbers in the array: $sum"
