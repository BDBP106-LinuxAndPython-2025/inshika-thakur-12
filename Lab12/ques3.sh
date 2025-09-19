#!/bin/bash

#Write a shell script to make the user input a number and making use of the until loop, print the multiplication table of that number up to 15.

echo "enter a number: "
read num

i=1
until [ $i -gt 15 ];
do
	echo "$num * $i = $[num * i]"
	i=$[$i+1]
done
