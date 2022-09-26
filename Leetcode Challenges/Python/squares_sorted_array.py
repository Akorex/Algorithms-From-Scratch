"""
Solution to Leetcode problem #977 - Squares of a sorted array
https://leetcode.com/problems/squares-of-a-sorted-array/

"""


from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[i] * nums[i])
        
        ans = sorted(result)
        return ans