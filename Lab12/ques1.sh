#!/bin/bash

#Write a shell script to print numbers from 0 to 10.
#
i=0
while [ $i -le 10 ]
do
	echo $i
	i=$((i+1))
done

