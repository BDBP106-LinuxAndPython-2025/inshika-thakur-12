#!usr/bin/python3

"""Q4.)Define a module called factorial that contains a function to find the factorial
of a given integer. Using this function, find the permutation and combination of the
given inputs.
A4.) """
from math import factorial
def permutation(n, r):
    """nPr = n! / (n-r)!"""
    return factorial(n) // factorial(n - r)

def combination(n, r):
    """nCr = n! / (r! * (n-r)!)"""
    return factorial(n) // (factorial(r) * factorial(n - r))

# Example usage
n = 21
r = 7

print(f"{n}P{r} =", permutation(n, r))
print(f"{n}C{r} =", combination(n, r))