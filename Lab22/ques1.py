#!/usr/bin/python

"""Create a logging decorator to record function calls, arguments, and return values. For
example, if we have an add function shown below and invoke it as add(2,3), create a
decorator that prints the following:
# add function
def add(a, b):
return a + b
# the decorator should print
Calling add with args: (2, 3), kwargs: {}
add returned: 5"""

def logging_calls(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {format(func.__name__)} with {args}, {kwargs}')
        result = func(*args, **kwargs)
        print('Returned: {}'.format(result))
        return func(*args, **kwargs)
    return wrapper
@logging_calls
def add(a, b):
    return a + b

add(2,3)
