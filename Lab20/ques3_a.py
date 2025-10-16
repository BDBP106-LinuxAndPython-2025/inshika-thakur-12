#!/usr/bin/python3

"""(a) Create a simple text file containing the following string matrix, and save it as
‘stringmatrix.dat’. This should be saved as a separate program called ”Q3 a.py”.
(Hint: For those aware of ascii values for alphabets and know how to use them, the
ascii value of ‘A’ is 65, and one can get the alphabet string by calling chr(65).)
A B C D
E F G H
I J K L"""

with open("stringmatrix.dat", "w") as file:
    start_ascii=65

    for r in range(3):
        line_chars=[]
        for col in range(4):
            char=chr(start_ascii + r*4 +col)
            line_chars.append(char)

        file.write("".join(line_chars)+'\n')
print("stringmatrix.dat created successfully")