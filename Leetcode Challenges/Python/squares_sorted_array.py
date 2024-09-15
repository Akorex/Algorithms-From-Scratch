"""
Solution to Leetcode problem #977 - Squares of Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/description/

"""
from typing import List


# very trivial solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [num*num for num in nums]

        squares.sort()

        return squares

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans.append(nums[left] * nums[left])
                left += 1
            else:
                ans.append(nums[right] * nums[right])
                right -= 1
        return ans[::-1]