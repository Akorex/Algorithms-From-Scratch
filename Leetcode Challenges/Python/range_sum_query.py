"""
Solution to leetcode #303 - Range Sum Query Immutable

https://leetcode.com/problems/range-sum-query-immutable/description/

"""
from typing import List

# initial attempt
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        ans = 0

        while left <= right:
            ans += self.nums[left]
            left += 1
        return ans


# prefix sum
class NumArrayy:

    def __init__(self, nums: List[int]):
        self.nums = [0]

        for num in nums:
            self.nums.append(self.nums[-1] + num)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]

        
        