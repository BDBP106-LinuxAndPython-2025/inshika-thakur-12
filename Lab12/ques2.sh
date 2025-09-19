#!/bin/bash

#Write a shell script to print only even numbers between 0 and 50. (Note: think aboutwhat is the condition to be tested as well as the for-loop structure.)

function question {
n=0
while [ $n -le 50 ]
do
	if (( $n%2==0)); then
		echo $n
	fi
        n=$[$n+1]
done
}
value=$(question)
echo $value

