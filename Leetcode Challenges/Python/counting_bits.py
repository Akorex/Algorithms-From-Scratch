"""Solution to Leetcode problem #338 - Counting Bits
https://leetcode.com/problems/counting-bits/

Intuition to this solution is inspired by https://leetcode.com/problems/counting-bits/discuss/1808002/A-very-very-EASY-to-go-EXPLANATION
"""
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(len(ans)):
            ans[i] = self.solve(i)
        return ans
    
    def solve(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if (n % 2 == 0):
            return self.solve(n/2)
        else:
            return 1 + self.solve(n//2)