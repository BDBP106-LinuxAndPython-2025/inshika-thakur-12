#!/bin/bash
#Getting the username of the logged in user
logged_in_user="$(whoami)"
#Checking if the user is logged in
if [ -n "$logged_in_user" ]; then
	echo "The logged-in user is: $logged_in_user"
else
	echo "User is not logged in"
fi

#ERRORS
#LINE 3: The $(whoami) was not inside double quotes
#LINE 5: In the if block there was one circular bracket instead of square bracket so I relaced the circular bracket with square bracket. The then should be on the same line.
#LINE 5: Here the logged_in_user was typed as loged_in_user due to which the the loop was directly entering the else block and giving the output User is not logged in. 
#LINE 6: The $logged-in_USER should be written as logged_in_user
