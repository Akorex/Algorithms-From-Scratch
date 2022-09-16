"""Solution to Leetcode problem #303 - Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/

"""
from typing import List

# initial approach - exceeds the Time Limit
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum


# accepted approach
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0]
        for num in nums:
            self.nums.append(self.nums[-1] + num)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]


# preferred but seems slower
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left: right + 1])
