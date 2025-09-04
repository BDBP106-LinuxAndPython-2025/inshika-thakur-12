#!/bin/bash

#question 1
#i) To print all the lines that has "and" in it.
#sed -n '/and/p' ques1.txt

#ii)To change the instances of the word "Language" into "lang"
#sed 's/language/lang/g' ques1.txt

#iii)To delete all the lines that has the word is
#sed '/is/d' ques1.txt

#iv) To find a way to insert line numbers at the beginning of each line
#sed -n 'p;n' ques1.txt

#v)To remove the first and second lines only
#sed '1,2d' ques1.txt
 
#vi)To print every other line in the above file
#sed = ques1.txt | paste - -

#vi)To substitute first instance of ‘Python’ by ‘python’ and ‘language’ into ‘lang’ using one sed command.
#sed -e '1s/Python/python/' -e '1s/language/lang/' ques1.txt
