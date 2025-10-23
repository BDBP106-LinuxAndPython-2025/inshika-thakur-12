#!/usr/bin/python3

"""Write a decorator called @track_calls that counts how many times a function has been
called. It also should print the function name and the number of calls each times it is
executed. Instead of printing the output to the screen, log the output in a file."""

def track_calls(func):
    func.count = 0
    def wrapper(*args, **kwargs):
        func.count += 1
        output = f'{func.__name__} is called for {func.count} times \n'
        file=open("result.txt", "w")
        file.write(output)
    return wrapper

@track_calls
def func1():
    pass
func1()
func1()
func1()
func1()
func1()
func1()
func1()
func1()
func1()
func1()