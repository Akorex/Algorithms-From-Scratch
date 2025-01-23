"""
Solution to Leetcode problem #152 - Maximum Product Subarray

https://leetcode.com/problems/maximum-product-subarray/
"""
from typing import List

# initial approach, doesn't pass all cases
# wrong because of the following:
# Incorrect initialization of currMax which is wrong when all the numbers in an array are negative
# not considering negative elements
# not considering single elements
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 0

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            tempMax = nums[i-1] * nums[i]

            if tempMax > currMax:
                currMax = tempMax
        return currMax
    

# correct approach
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            curr_min = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)

            prev_max = curr_max
            prev_min = curr_min

            ans = max(ans, curr_max)

        return ans


# optimized

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            temp_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_min = min(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_max = temp_max

            result = max(result, curr_max)

        return result