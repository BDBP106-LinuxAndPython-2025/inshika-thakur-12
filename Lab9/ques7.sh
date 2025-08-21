#!/bin/bash

var=$(bc << EOF 
scale=3
m=1
s=3*10^8
e=m*s*s
e
EOF
)
echo "The final answer is:" $var

