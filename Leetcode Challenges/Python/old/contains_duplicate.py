"""
Solution to Leetcode problem - #217 - Contains duplicate
https://leetcode.com/problems/contains-duplicate/
"""


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False