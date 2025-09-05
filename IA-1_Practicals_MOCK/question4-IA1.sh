#!/bin/bash

file="fileque4.txt"

while read column1 column2 column3
do 
	echo "col1: $column1: col2: $column2 col3: $column3"
done < "$file"

#on running this command:
#COMMAND: bash <filename>
#OUTPUT: col1: pink: col2: purple col3: blue
#	 col1: grey: col2: black col3: red
#	 col1: white: col2: green col3: orange
#	 col1: yellow: col2: brown col3: silver
#	 col1: golden: col2: maroon col3: lavender

