#!/bin/bash

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

