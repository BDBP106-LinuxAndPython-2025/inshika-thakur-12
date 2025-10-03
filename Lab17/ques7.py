#!/usr/bin/python

"""Write a program with a function to find whether a given triangle with sides a, b, c is
isosceles, scalene or equilateral triangle, also provide a test case output from the program."""
# from ques4 import result


def triangle(a, b, c):
    result = ""
    if a + b <= c or a + c <= b or b + c <= a:
        print("Not a valid triangle")

    elif a == b == c:
        result = "equilateral"
    elif a == b or b == c or a == c:
        result = "isosceles"
    else:
        result = "scalene"
    return result

print(f"Type of triangle:", triangle(a =5, b=5, c=5))
