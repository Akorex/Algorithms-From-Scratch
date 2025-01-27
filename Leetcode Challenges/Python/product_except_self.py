"""
Solution to Leetcode problem #238 - Product of Array except self

https://leetcode.com/problems/product-of-array-except-self/description/

"""

from typing import List

# initial approach, not O(n)
# Time Limit Exceeded
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            ans[i] = product

        return ans

## accepted approach

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans
        