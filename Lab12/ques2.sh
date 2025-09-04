#!/bin/bash

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

