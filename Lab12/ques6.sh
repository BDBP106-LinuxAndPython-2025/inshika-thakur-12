#!/bin/bash

#Write a bash script that defines a function called maximum that takes two numbers as arguments and prints the maximum of the two.

n=$1
m=$2
function maximum {
	if [ $n -gt $m ]; then
		echo $n "is the greatest"
	elif [ $m -gt $n ]; then
		echo $m "is greatest"
	fi
}
value=$(maximum)
echo $value
