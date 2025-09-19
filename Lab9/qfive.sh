#!/bin/bash

#By extension the shell interprets arguments to any script as $1, $2 etc. See the example below to understand how this works. Create the following shell script:
#!/bin/bash
#echo "My name is $1"
#Save the above script as name.sh. Then make it executable using the chmod command, and execute it as follows: ./name.sh <yourname>. The output will be (in my case)

#My name is Jayashree. $1 is the first argument to the shell script which is automatically read in and used in the execution of the script.
#(i) Write a script to print your name as well as the MSc program you are in by using $1 and $2.
#(ii) Now add the 4 echo lines from your previous question to this script and executethe script. What are the values of the special variables? Take a snapshot of the output and upload this png/jpeg file with a name with this question number.

echo "My name is $1"
echo "I am in $2 course"
#So here $1 is the argument that we want to take outside vi (input)
#(ii) The 4 echo command from prev code

var1=$(who ; echo $?)
echo "The output is:" $var1
var2=$(date ; echo $0)
echo "The second output is:" $var2
var3=$(uname ; echo $#)
echo "The third output is:" $var3
var4=$(date ; echo $@)
echo "The fourth output is:" $var4

