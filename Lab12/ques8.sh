#!/bin/bash

#The Linux system handles every object as a file. This includes the input and output process. Each file object is identified using a file descriptor, which is a non-negative integer that uniquely identifies open files in a session. The bash reserves the first three file descriptors (0,1 and 2) for special purposes. The file descriptor 0 stands for STDIN (standard input), 1 for STDOUT (standard output) and 2 for STDERR (standard error).The workings of these are shown below. Try these commands first to understand howthese work.
#(i) Understanding STDOUT and STDERR
#ls
#ls > listoffiles
#ls 1> listoffiles
#The symbol > automatically redirects any non-error output of the screen to listoffiles.
#The 1 > means that the standard output in particular to the listoffiles. Now try the following command where the directory called newdir does not exist.
#ls -l . newdir
#ls -l . newdir 1>presentfiles 2>filesnotpresent

#Explain what happened in the newdir example. Did you notice that the successful part of the ls command went to presentfiles and the error part went to filesnotpresent file?

# What is the result of ls -l . newdir >listoffiles ? Explain how this command worked.

ls #it will list all the files in the directory
ls > listoffiles #it will create a newfile and will redirect the output into that file
ls 1> listoffiles #it will redirect the successful output into the file
ls -l . newdir #it will list the files and will display that there is no newdir present
ls -l . newdir 1>presentfiles 2>filesnotpresent #it will redirect the successful output into a new file i.e present files and the unsuccessful output into the other new file that is files nt present. 

ls -l . newdir >listoffiles

#Here on running the command ls -l . newdir >listoffiles, we get error in the output because there is no newdir and ls -l got saved in listoffiles.
