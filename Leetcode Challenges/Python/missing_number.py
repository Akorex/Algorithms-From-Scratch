"""
Solution to Leetcode problem #268 - Missing Number
https://leetcode.com/problems/missing-number/description/

"""
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
            

class Solutionn:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if nums[0] != 0:
            return 0
        
        if nums[-1] != n:
            return n

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
            

class Solutionnn:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_sum = sum(nums)
        range_sum = n * (n+1)//2

        dff = range_sum - num_sum

        return dff
