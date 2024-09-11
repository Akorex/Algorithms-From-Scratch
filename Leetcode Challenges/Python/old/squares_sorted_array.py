"""
Solution to Leetcode problem #977 - Squares of a sorted array
https://leetcode.com/problems/squares-of-a-sorted-array/

"""


import collections
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[i] * nums[i])
        
        ans = sorted(result)
        return ans

# approach 1 but better
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [v**2 for v in nums]
        arr.sort()
        return arr

# using a deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = collections.deque(nums)
        reverse = []

        while ans:
            left = ans[0] ** 2
            right = ans[-1] ** 2

            if left > right:
                reverse.append(left)
                ans.popleft()
            else:
                reverse.append(right)
                ans.pop()
        return reverse[::-1]