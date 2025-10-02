#!/bin/bash

#A script that prints the current time only every 10 seconds for a minute.

for a in {1..6}
do 
	echo Current time is $(date '+%H:%M:%S')
	if [ $a -lt 6 ]; then
		sleep 10
	fi
done
