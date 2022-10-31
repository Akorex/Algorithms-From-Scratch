"""
Solution to Leetcode problem #26 - Remove Duplicates from a Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""

from typing import List

# initial approach - not accepted
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        seen = []
        
        while start <= end:
            if nums[start] not in seen:
                seen.append(nums[start])
                start += 1
            else:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
        nums = sorted(nums)
        return start

# accepted approach
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1
        
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[start] = nums[i+1]
                start += 1
                
        return start