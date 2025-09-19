#!/bin/bash

#(8) Write a shell script that directs the output of ls command to a grep command to list files with extension .csv. Make sure to copy or download the two data files you have used in this course before to this directory first (these are BrainCancer.csv and Heart.csv).

var=$(ls | grep "\.csv")
echo "The files with .csv are:" $var

