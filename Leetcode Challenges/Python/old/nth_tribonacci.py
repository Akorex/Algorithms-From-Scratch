"""
Solution to Leetcode problem #1137 - Nth Tribonacci number

https://leetcode.com/problems/n-th-tribonacci-number/
"""

class Solution:
    def __init__(self):
        self.res = {0: 0, 1:1, 2:1}

    def tribonacci(self, n: int) -> int:
        if n < 1:
            return 0

        for i in range(3, n+1):
            self.res[i] = self.res[i - 1] + self.res[ i - 2] + self.res[i - 3]

        return self.res[n]