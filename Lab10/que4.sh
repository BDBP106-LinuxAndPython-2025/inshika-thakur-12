#!/bin/bash
#to check if a file exists and if a file is executable

echo "Input the file name"
read n
echo "The file:" $n

if [ -f "$n" ]; then
	echo "The file exists"
	exit 200
	echo $?
	#Prints 200 if file exists
else 
	echo "File does not exist."
	exit 201
	#Prints 210 if file does not exists.
fi

#After you input the file name outside vi it will show whether the file exists or not. If it exists and you give the command <echo $?> It should give the output as 200 and if the file name that you gave as input does not exist then it should give the output as 201 on giving the command echo$? 
#i) To check if the correct exit code is generated <echo $?> should execute exit 200 if the file exists and exit 201 if the file does not exist.
#ii) If we give the command <echo $?> after the if block then, if we are giving a file that exists in the input then it gives output with a 0 even though we have set it to 200 and the end but if the input has file that does not exist then it simply gives the output: File does not exist. 
#iii) If we give the command echo $? after exit 200 or exit 201 then, it will return 200 for files that exist and 201 for files that does not exist because <echo $?> is below exit command.
