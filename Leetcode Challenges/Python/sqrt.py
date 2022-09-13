"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""
import math

def mysqrt(x):
    """Returns the approximate square root of x using binary search"""

    if x == 0 or x == 1:
        return x

    left = 0
    right = x

    while left < right:
        # mid = (left + right) / 2 can overflow if right > Integer.MAX_VALUE - left
        mid = left + (right - left) /2

        if (mid > x /mid):
            right = mid - 1
        else:
            left = mid + 1
 
            if (left > x / left):
                return mid
    left = int(left)
    return left

print(mysqrt(25))