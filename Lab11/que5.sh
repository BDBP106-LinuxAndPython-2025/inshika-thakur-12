#!/bin/bash
#question5

#i)Define variables var1 with value "Testing" and var2 with value "testing"

var1="Testing"
var2="testing"

#ii)Write in a shell script, an if statement involving > comparison of the two strings. Remember to use the \ with the operator as in the last question. Use appropriate echo statements

if [ "$var1" \> "$var2" ]; then
	echo "$var1 is greater than $var2"
else
	echo "$var2 is greater than $var1"
fi

#iii) Execute the shell script and note down the result of which variable is greater than the other
#So on executing the shell script the output is: testing is greater than Testing.

#iv)Save the values of the two variables in a new file called ’teststringfile’.

echo $var1 > teststringfile
echo $var2 >> teststringfile
sort teststringfile

#If statement shows testing as the greater value according to ASCII, as t is equal to 116 and T is equal to 84.
#Sort uses a different encoding (UTF-8) So it shows Testing greater than testing.

