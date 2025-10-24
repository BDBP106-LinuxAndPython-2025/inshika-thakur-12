#!usr/bin/python3

"""Q7.)Implement the Fibonacci function with parameter n. Call fibonacci(100) and use a
decorator function to log the time taken to run this function."""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("Fibonacci(100):", fibonacci(100))