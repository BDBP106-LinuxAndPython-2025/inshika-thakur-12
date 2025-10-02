#!/bin/bash

#Display a menu with options: 1) Show date, 2) Show calendar, 3) show logged-in users, 4) Exit. The script should display these options, execute the appropriate command according to the option.

while true
do
echo Menu
echo 1 date
echo 2 calender
echo 3 logged-in users
echo 4 exit
read -p "Enter the choice number from above: " i
	case $i in
		1) echo Current date and time:
		   date
	      	   ;;
		2) echo Calender:
	           cal
		   ;;
		3) echo Logged-in user: 
		   who 
		   ;;
		4) echo Exiting the menu
		   break
		   ;;
		*) echo Invalid user!
		   ;;
	esac
done
