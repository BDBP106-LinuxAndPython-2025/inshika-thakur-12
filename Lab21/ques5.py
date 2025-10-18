#!/usr/bin/python3

"""Write a function that takes two numbers n1 and n2 and an operator description such as add,
subtract etc. Depending on the operation, perform the operation. Raise a ValueError if the
operator is not an arithmetic operation such as add, subtract, multiplication or division.
Catch the ValueError and ZeroDivisionError and print the appropriate messages. In the finally
block, print a completion message. Call this function with different scenarios to test the above
exceptions. Take screenshots of the output while uploading your labs to GitHub."""

def calculate(n1, n2, operation):
    try:
        if operation == "add":
            result = n1 + n2
        elif operation == "subtract":
            result = n1 - n2
        elif operation == "multiplication":
            result = n1 * n2
        elif operation == "division":
            result = n1 / n2
        else:
            raise ValueError("Invalid operation as it is not addition, subtraction or multiplication.")
        print(f"Result of {operation} between {n1} and {n2} is: {result}")
    except ValueError as ve:
        print("ValueError:", ve)
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")
    finally:
        print("Calculation has been completed.")

calculate(10, 5, "add")
calculate(10, 0, "division")
calculate(10, 5, "modulus")
calculate(10, 5, "multiplication")
calculate(10, 3, "subtract")
