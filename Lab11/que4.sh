#!/bin/bash

#Previous script
#val1=Jayashree
#val2=Nagesh
#if [ $val1 > $val2 ]; then 
#	echo "$val1 is greater than $val2"
#else 
#	echo "$val1 is lesser than $val2"
#fi

#In the previous script the variables $val1 and $val2 were not enclosed in double quotes due to which a new file named "Nagesh" was created so in order to run the code correctly we enclosed the variables in double quotes and in order to get the output "Jayashree is lesser than Nagesh" I added two square brackets instead of two.

#Correct script

val1=Jayashree
val2=Nagesh

if [[ "$val1" > "$val2" ]]; then
       echo "$val1 is greater than $val2"
else
       	echo "$val1 is lesser than $val2"
fi

