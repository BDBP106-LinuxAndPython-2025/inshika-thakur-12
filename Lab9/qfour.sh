#!/bin/bash

#There are four ‘special’ variables that a shell uses for its functioning. You have already seen one of these- $?. The other three are
# $0 represents the name of the script itself
# $# represents the number of arguments passed to the script
# $@ represents all the arguments passed to the script
# Write a shell script with 4 echo commands to display the value of each of these variables

var1=$(who ; echo $?)
echo "The output is:" $var1
var2=$(date ; echo $0)
echo "The second output is:" $var2
var3=$(uname ; echo $#)
echo "The third output is:" $var3
var4=$(date ; echo $@)
echo "The fourth output is:" $var4

#var1=$(who ; echo $?)
#who: prints the list of users currently logged in.
#;: separates commands.
#echo $?: prints the exit status of the last command (who). $? is a special variable holding exit status (0 means success)
#The whole $(...) captures the combined output of who and the exit status on the next line into var1.

# $0 : Name of the script
# $# : Represents the number of arguments
# $@ : All arguments (indicidually quoted) {if no arguments passed it will be empty}
# $* : All arguments (as a single word/string)

