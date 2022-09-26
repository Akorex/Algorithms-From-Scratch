"""
Solution to Leetcode problem #287 - Find the Duplicate Number

https://leetcode.com/problems/find-the-duplicate-number/

Requires to not modifty the list & a constant space ops
"""

from typing import List

# uses the sorted() function. Test cases passed but does not satisfy requirement
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return nums[i - 1]

# uses a list to store seen values, but exceeds time limit
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = []
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            else:
                seen.append(nums[i])

# using binary search
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid, count = (left + right)//2, 0

            for num in nums:
                if num <= mid:
                    count += 1
                if count <= mid:
                    left = mid + 1
                else:
                    end = mid

        return end