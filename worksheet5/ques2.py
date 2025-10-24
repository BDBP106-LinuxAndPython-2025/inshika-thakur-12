#!usr/bin/python3

"""Q2.) How does python knows where to search for packages and modules
A2.) When I try to import a module in Python, the interpreter looks for that
module in a specific order. First, it checks the current directory (where my script
is located). If it doesn’t find the module there, it then looks in the folders
listed in the PYTHONPATH environment variable (if I have set one). If the module
is still missing, Python finally searches its standard library and any other
built-in locations. All these places where Python looks are stored in
a list called sys.path, which I can see and even change while my program runs"""