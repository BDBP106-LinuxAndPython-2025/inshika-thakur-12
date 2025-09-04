#!/bin/bash

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
