#!/bin/bash

#A script that prints the current disk usage, and if the usage is above 80% print a warning message

usage=$(df / | tail -1 | gawk '{print $5}' | tr -d '%')
#df shows the disk space usage for file system
#/ is for root directory
#tr command will remove the % sign for comparison

echo "Current disk usage: $usage%"
if [ "$usage" -gt 80 ]; then
    echo "WARNING: Disk usage is above 80%!"
fi


