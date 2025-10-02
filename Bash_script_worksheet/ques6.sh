#!/bin/bash

#A script to generate the multiplication table for a given number from 1 to 20.

read -p "Enter a number to generate its multiplication table: " N
echo "Multiplication Table for $N:"
for i in {1..20}; do
    result=$((N * i))
    echo "$N x $i = $result"
done

