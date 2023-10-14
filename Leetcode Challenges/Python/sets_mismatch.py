"""
Solution to Leetcode problem #645 - Set Mismatch

https://leetcode.com/problems/set-mismatch/description/
"""
from typing import List

# initial bruteforce approach
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]: 
        ans = []
        range_ans = [i for i in range(1, len(nums) + 1)]

        # find the duplicate entry
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                ans.append(nums[i])

        # find the missing entry
        for num in range_ans:
            if num not in nums:
                ans.append(num)
        return ans
    
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]: 
        ans = []

        # find the duplicate entry
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                ans.append(nums[i])

        # find the missing entry
        ans.append(sum(range(len(nums) + 1)) - sum(set(nums)))

        return ans
        
# interesting approach
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        true_sum = n * (n+1)//2
        actual_sum = sum(nums)
        set_sum = sum(set(nums))

        return [actual_sum - set_sum, true_sum - set_sum]