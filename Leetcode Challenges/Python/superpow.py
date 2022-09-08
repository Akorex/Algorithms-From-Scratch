"""Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely 
large positive integer given in the form of an array.


The solution to this Leet Code problem was inspired by this solution (https://leetcode.com/problems/super-pow/discuss/400893/Python-3-(With-Explanation)-(Handles-All-Test-Cases)-(one-line)-(beats-~97))
which introduced the concept of Euler's totient theorem
"""

class Solution:
    def superPow(self, a, b) -> int:
        b = int(''.join(map(str, b)))
        totient_result = b % 1140
        totient_result += 1140 # so we don't get 0
        a_reduced = a % 1337
        result = (a_reduced ** totient_result) % 1337
        
        return result