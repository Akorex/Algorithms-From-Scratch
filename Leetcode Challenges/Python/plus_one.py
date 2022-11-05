"""
Solution to Leetcode problem #66 - Plus One

https://leetcode.com/problems/plus-one/
"""
from typing import List

# initial
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits))) + 1
        ans = list(str(num))
        return ans

# one liner
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int(''.join(map(str, digits))) + 1))

