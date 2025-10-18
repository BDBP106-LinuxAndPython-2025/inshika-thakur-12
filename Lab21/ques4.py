#!/usr/bin/python3

"""Write a Python function checkList that accepts a list and an index, and prints the
element of the list at the index position. Catch the IndexError and TypeError and
display appropriate messages. Call the function for (a) number list and index, (b) A
string input and index, (c) A boolean value (True) and index and (d) A string input and
incorrect index."""

def checkList(lst, index):
    try:
        print("Element at index", index, "is:", lst[index])
    except IndexError:
        print("IndexError: The index is out of range.")
    except TypeError:
        print("TypeError: Invalid input type for list or index.")

checkList([10, 20, 30, 40], 2)


checkList("Hello", 1)


checkList(True, 0)

checkList("Hello", 10)
