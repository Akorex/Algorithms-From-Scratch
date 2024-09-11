"""
Solution to Leetcode problem #29 - Divide Two Integers

https://leetcode.com/problems/divide-two-integers/description/

"""
import unittest

def divide(dividend: int, divisor: int) -> int:

    # handle division by zero
    if divisor == 0:
        return 2**31 - 1
    
    # handle overflow case
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    
    # get the sign of the result
    sign = 1
    if dividend < 0:
        dividend = -dividend
        sign = -sign

    if divisor < 0:
        divisor = -divisor
        sign = -sign

    # find the largest multiple of the divisor less or equal to dividend
    multiple = 1

    while dividend >= (divisor << 1):
        divisor <<= 1
        multiple <<= 1


    # perform division using binary search
    quotient = 0

    while multiple > 0:
        if dividend >= divisor:
            dividend -= divisor
            quotient += multiple
        
        divisor  >>= 1
        multiple >>= 1

    # apply the sign and return

    return sign * quotient

class Test(unittest.TestCase):
    
    test_cases = [
        (15, 5, 3), 
        (20, 4, 5), 
        (100, 0, 2**31 - 1), 
        (3, 4, 0)
    ]

    def test_divide(self):
        for [dividend, divisor, quotient] in self.test_cases:
            assert divide(dividend, divisor) == quotient

if __name__ == '__main__':
    unittest.main()