#!/bin/bash

#A script that finds files older than 7 days and compresses them into a .tar.gz file with the date of compression in the name in the format YYYYMMDD.

Date=$(date '+%Y%m%d')
tar -czvf old_file"$Date" $( find . -type f -mtime +7 )

#While running this, I got error saying that it cannot tar the files, as all the files in this directory is not older than 7 days
