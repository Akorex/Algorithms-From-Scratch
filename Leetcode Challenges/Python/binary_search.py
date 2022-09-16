"""Solution to Leetcode problem #704 - Binary Search

https://leetcode.com/problems/binary-search/
"""

from typing import List

# my initial approach
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = self.binary_search(nums, target, 0, len(nums) - 1)
        if result:
            return nums.index(target)
        else:
            return -1
        
    def binary_search(self, nums, target, start, end):
        if start > end:
            return False
        else:
            mid = (start + end)//2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                return self.binary_search(nums, target, start, mid - 1)
            elif target > nums[mid]:
                return self.binary_search(nums, target, mid + 1, end)

## another approach
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1