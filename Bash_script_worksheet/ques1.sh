#!/bin/bash

#The script should take an integer input and check if it is prime or not.
read -p "Enter the integer that you want to check:" N
if [ $N -eq 1 ]; then
	echo "1 is neither prime nor composite"
else
Prime=1
for (( i=2; i*i<=N; i++ ))
do
	if (( N%i == 0 )); then
		Prime=0
		break
	fi
done
if [ $Prime -eq 1 ]; then
	echo "$N is a prime number."
else
	echo "$N is not a prime number."
fi
fi

