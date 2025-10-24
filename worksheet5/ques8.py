#!/usr/bin/python3

"""Q8.) In the above exercise, let’s use an in-built decorator function called lru_cache, where
lru stands for least recently used – It caches/stores the results of function calls, so
that if the same input occurs again, it reuses the stored result instead of recomputing it.
Least recently used means that it keeps the most recent results and discards the oldest
ones if the cache gets full. We have control over the size of this cache, An example usage
is given below.
from functools import lru_cache
@lru_cache(maxsize=None)
def factorial(n):
if n==0 or n==1: return 1
if n>1: return n*factorial(n-1)
(i) Use a similar setup for the Fibonacci series calculation with maxsize=5. What is
the time difference you see with and without the use of lru_cache?
(ii) Provide a docstring with ‘”This function outputs the sum of n Fibonacci num-
bers”’ inside the function. Print fibonacci.__doc__ and observe the output.
(iii) Use a custom decorator log_time to print the datetime.now() value at entry
and exit for every func.__name__ call with the n (args) value."""
from functools import lru_cache
from datetime import datetime
import time

def log_time(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Entering {func.__name__} with args={args}")
        result = func(*args, **kwargs)
        print(f"[{datetime.now()}] Exiting {func.__name__} with args={args}")
        return result
    return wrapper

@lru_cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_no_cache(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

n = 52
start = time.time()
print(f"Fibonacci({n}) with lru_cache:", fibonacci(n))
print("Time with lru_cache:", time.time() - start)

start = time.time()
print(f"Fibonacci({n}) without lru_cache:", fibonacci_no_cache(n))
print("Time without lru_cache:", time.time() - start)

# Print the docstring
print("Docstring of fibonacci function:", fibonacci.__doc__)