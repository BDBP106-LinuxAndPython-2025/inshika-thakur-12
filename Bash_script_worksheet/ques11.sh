#!/bin/bash

#In a directory, rename all files with extension .txt to have a prefix old

for File in *.txt
do
	mv $File old_$File
done
