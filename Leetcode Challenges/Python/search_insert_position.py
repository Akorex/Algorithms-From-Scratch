"""
Solution to Leetcode problem #35 - Search Insert Position

https://leetcode.com/problems/search-insert-position/
"""
from typing import List

# initial attempt
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # use binary search to find target
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2
            
            if target < nums[mid]:
                right = mid - 1
                
            elif target > nums[mid]:
                left = mid + 1

            elif target == nums[mid]:
                return mid
        
        # return the index 
        if target < nums[mid]:
            return mid
        else:
            return mid + 1
        

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left