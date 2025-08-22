#!/bin/bash
#prompts user to enter age and check if it is greater than or equal to 18

echo "Input your age:"
read n
echo "Your age is:" $n

if [ "$n" -ge 18 ]; then
	echo "Your are an adult"
else
	echo "You are a minor"
fi

