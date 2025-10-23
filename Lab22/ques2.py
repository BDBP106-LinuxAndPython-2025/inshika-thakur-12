#!/usr/bin/python3

"""Create a decorator to measure the execution time of a function. Please demonstrate
using a sample function (add sleep for checking) and a decorator for this sample function
that measures the execution time."""

import time
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Execution time: {:.3f}'.format(end_time - start_time))
        return result
    return wrapper
@measure_execution_time
def sleep_for(seconds):
    time.sleep(seconds)
    print('Sleeping for {} seconds'.format(seconds))

sleep_for(3)