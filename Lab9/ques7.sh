#!/bin/bash

# Write a shell script that calculates the energy-mass equivalence (Energy = mass∗speed2) of an object with mass of 1kg moving with the speed of light (what is this value?). Note: It’s best to invoke bc command with multiple expressions using EOF approach.

var=$(bc << EOF 
scale=3
m=1
s=3*10^8
e=m*s*s
e
EOF
)
echo "The final answer is:" $var

