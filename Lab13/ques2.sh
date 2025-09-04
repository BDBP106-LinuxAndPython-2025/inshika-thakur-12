#!/bin/bash

#i)Find a way to print the people’ names who are scored less than 25 in their subjects.
#gawk '$2<25 {print $1 }' ques2.txt

#ii)Print the student whose Physics score is given.
#gawk '$3=="Physics" {print $1}' ques2.txt

#iii)find a way to rewrite the data into a csv format in a new file called data2.csv
#gawk '{ print $1 "," $2 "," $3 }' ques2.txt > data2.csv

