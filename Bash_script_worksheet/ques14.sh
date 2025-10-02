#!/bin/bash

#A script that monitors the memory usage (free -m) for 5 minutes and prints a warning if free memory is below 500MB.

M=$( free -m | awk '/^Mem:/ {print $4}' )
if [ $M -lt 500 ]; then
	echo WARNING: FREE MEMORY IS BELOW 500MB
else
	echo The system is having $M MB of free memory
fi
#So, here if you give the command free -m in the terminal, you will get the information about the memory, the 4th column is for the free memory hence we used the awk and the $4 in the command line.
