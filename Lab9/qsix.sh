#!/bin/bash

#(6) Write a shell script to do the following, all in one script:
#• Print the value of HOME variable
#• Calculate the following: 23934/44343 using bc command and EOF method
#• List files in your HOME that start with ‘D’
#• Filter the line(s) in /etc/passwd that have your username
echo "The value of home variable is $HOME"

var=$(bc << EOF
scale=3
23934/44343
EOF
)
echo "The answer of 23934/44343 is:" $var

var1=$(ls $HOME/D*)
echo "ALl files in home that starts with D are:" $var1

var2=$(grep "$USER" /etc/passwd)
echo "Lines with /etc/passwd with USER are:" $var2
