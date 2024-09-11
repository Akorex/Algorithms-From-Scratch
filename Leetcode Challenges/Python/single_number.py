"""
solution to leetcode problem #136 - Single Number

https://leetcode.com/problems/single-number/

"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for key, value in seen.items():
            if value == 1:
                return key