#!/bin/bash

#Using echo to print a multi-line message inside a script: The -e option to echo command enables the interpretation of backslash escapes. \n represents a newline character, it leads to subsequent text to be printed on a new line. \t represents a tab character, causingsubsequent text to be indented with a tab. Try the following command to understand

#how this option works-
#echo -e "This is line number 1.\n This is line number 2.\n\t This is line

#number 3 indented with a tab character". Inside a shell script, use the echo command to output the following text in the given format below. Note that each item below is indented with a tab character.

echo -e "This is line number 1, \n This is line number 2. \n\t This is line number 3 indented with a tab character."

echo -e "Tips for programming:\n\t 1. Master the fundamentals\n\t 2. Learn by doing\n\t 3. Understand the 'Why'\n\t 4. Practice regularly\n\t 5. Debug effectively\n\t 6. Read and analyse code\n\t 7. Breakdown problems\n\t 8. Utilize resources\n\t 9. Don't fear errors\n\t 10. Start small and iterate"
