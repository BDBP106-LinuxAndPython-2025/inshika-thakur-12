#!/usr/bin/python3

"""Q6.)11. You’re going to write an interactive calculator! User input is assumed to be a formula
that consists of a number, an operator (at least + and -), and another number, separated
by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the
resulting list is valid:
• If the input does not consist of 3 elements, raise a FormulaError, which is a custom
Exception.
• Try to convert the first and third input to a float (like so: float_value = float(str_value)).
Catch any ValueError that occurs, and instead raise a FormulaError
• If the second input is not ’+’ or ’-’, again raise a FormulaError
• If the input is valid, perform the calculation and print out the result. The user is
then prompted to provide new input, and so on, until the user enters quit.
 """
class FormulaError(Exception):
    pass
while True:
    s = input("Enter math expression: ")
    if s == "quit":
        break
    try:
        a, b, c = s.split()       # split input
        x = float(a)
        y = float(c)
        print(x + y) if b == "+" else print(x - y)
    except:
        print("Invalid input")