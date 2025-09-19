#!/bin/bash

#Write a function to check if a directory exists, and if it does not exist, to create the directory. If the directory exists, then the function should list the files in the directory.

filename=$1
function ques6 {
	if [ -e $filename ]; then
	ls
else
	mkdir $filename
	fi
}
val=$(ques6)
echo $val
