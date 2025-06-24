import time
import math

def timing_decorator(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print(f"Time taken by '{func.__name__}': {end - start:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def cube(n):
    return n ** 3

@timing_decorator
def square_root(n):
    return math.sqrt(n)

num = 64
print(f"Cube of {num}: {cube(num)}")
print(f"Square root of {num}: {square_root(num)}")
