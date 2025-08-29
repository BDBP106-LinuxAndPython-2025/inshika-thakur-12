#!/bin/bash

ls #it will list all the files in the directory
ls > listoffiles #it will create a newfile and will redirect the output into that file
ls 1> listoffiles #it will redirect the successful output into the file
ls -l . newdir #it will list the files and will display that there is no newdir present
ls -l . newdir 1>presentfiles 2>filesnotpresent #it will redirect the successful output into a new file i.e present files and the unsuccessful output into the other new file that is files nt present. 

ls -l . newdir >listoffiles

#Here on running the command ls -l . newdir >listoffiles, we get error in the output because there is no newdir and ls -l got saved in listoffiles.
