#!/bin/bash

#Write a bash script that defines a function called divide that takes two numbers as arguments and prints their quotient and remainder. Make sure to keep all the variables within the function as local variables and also prints the result up to 2 decimal places.This function also should check and make sure that division by zero does not happen.

read -p "Enter first number: " x
read -p "Enter second number: " y

a=$1
b=$2

divide() {

if [ "$2" -eq 0 ]; then
	echo "Error: division by zero"
	return
fi

q=$(echo "scale=2; $1/$2" | bc)
r=$(echo "scale=2; $1%$2" | bc)

echo "Quotient: $q"
echo "Remainder: $r"
}
divide $x $y

