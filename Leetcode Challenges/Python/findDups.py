"""
Solution to Leetcode problem #287 - Find the duplicate number

https://leetcode.com/problems/find-the-duplicate-number/description/
"""
from typing import List


# this works but doesn't follow requirements
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(1, len(nums) + 1):
            if nums[i-1] == nums[i]:
                return nums[i]
            

# works & follows requirement

class Solutionn:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]
        return -1