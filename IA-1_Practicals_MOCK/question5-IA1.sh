#!/bin/bash

echo "Input your arguments:" $1 $2 $3 $4

if [ $# -eq 4 ]; then
 	echo $1
	echo $2
	echo $3
	echo $4
else
	echo ERROR 
fi
