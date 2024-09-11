"""
Solution to Leetcode problem - #217 - Contains duplicate
https://leetcode.com/problems/contains-duplicate/

"""

from typing import List

# solution 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = []

        for num in nums:
            if num in seen:
                return True
            seen.append(num)
        return False
    

# solution 2

class Solutionn:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False