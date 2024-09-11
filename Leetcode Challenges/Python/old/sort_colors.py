"""
Solution to Leetcode problem #75 - Sort Colors

https://leetcode.com/problems/sort-colors/description/
"""
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # applying the selection sort algorithm

        n = len(nums)
        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            
            # swap the elements
            nums[i], nums[min_index] = nums[min_index], nums[i]