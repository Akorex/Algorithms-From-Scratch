"""
Solution to Leetcode problem # 41 - First Missing Positive

https://leetcode.com/problems/first-missing-positive/

"""
from typing import List

# initial solution - doesn't solve the problem in O(n) as required but O(nlogn) due to sorted()
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))

        i = 1
        for num in nums:
            if num == i:
                i += 1
            elif num > 0:
                return i
        return i


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # place each number in its correct index
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1