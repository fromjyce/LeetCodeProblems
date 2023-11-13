"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

import math
def mySqrt(x: int) -> int:
    return int(math.floor(math.sqrt(x)))

print(mySqrt(8))

#Another Way of doing it

def squareRoot(n):
    x=n
    y=1.000000
    e=0.000001 
    while x-y > e:
        x=(x+y)/2
        y=n/x
    return math.floor(x)


print(squareRoot(4))