"""
Solution to Leetcode problem #169 - Majority Element

https://leetcode.com/problems/majority-element/
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for key, value in seen.items():
            if value > len(nums)//2:
                return key