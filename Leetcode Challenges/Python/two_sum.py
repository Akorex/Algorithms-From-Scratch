"""
Solution to Leetcode problem #1 - Two Sum

"""
from typing import List

# brute force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
# don't fully get
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            elif num not in seen:
                seen[num] = i