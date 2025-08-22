#!/bin/bash

echo "Input a number: "
read n

if [ "$n" -gt 100 ]; then
	echo "The number is greater than 100."
else
	echo "The number is not greater than 100."
fi

#ERRORS
#LINE 6: There was only one circular bracket and two square brackets. So in order to make the code work we will either replace the two square brackets with one aand the circular bracket with one square bracket or the circular bracket with two square brackets
#LINE 11: There was an if block statement which was not needed.
