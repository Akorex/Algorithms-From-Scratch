
"""
Solution to Leetcode Problem #704 - Binary Search

https://leetcode.com/problems/binary-search/description/

"""


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid
        return -1
        