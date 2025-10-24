#!usr/bin/python3

"""Q3.) How are packages different from modules? How are modules different from functions?
And how are methods different from functions?
A3.) A module is basically just a single Python file where you can write functions,
classes, or variables. It’s like one piece of code saved in a file. On the other hand,
apackage is a folder that contains a bunch of these modules organized together.
It also has a special file called init.py which tells Python that this folder is a
package. So, packages help to keep related modules grouped in a nice structure

Modules vs Functions:
A module is a Python file that can have many things inside it like functions, classes,
or variables all together. A function is just a small block of code that does one
specific job and can be called to run whenever needed.

Methods vs Functions:
A method is like a function, but it belongs to an object or a class, so you have to
call it on that object (for example, "hello".upper() is a method of the string
"hello"). A function is independent and doesn’t need an object to be called (for
example, len("hello") is a function you can call directly).
"""