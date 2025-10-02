#!/bin/bash

#A script that prints a mini-system report that includes a) current date and time, b) logged-in users, c) system uptime and d) top 5 processes by memory usage.

echo Mini-system report:
echo a. Current date and time:
date
echo b. Logged-in users:
who
echo c. System uptime: 
uptime -p
echo Top 5 processes by memory usage:
top -b -o %MEM | head -n 12
