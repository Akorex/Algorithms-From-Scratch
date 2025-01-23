"""
Solution to Leetcode problem #628 -> Maximum Product of three Numbers

https://leetcode.com/problems/maximum-product-of-three-numbers/description/

"""

from typing import List

# bruteforce
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        max_num = nums[-1]

        neg_products = nums[0] * nums[1] * max_num
        pos_products = nums[-2] * nums[-3] * max_num

        return max(pos_products, neg_products)


# alt solution w/out sorting
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        return max(max1 * max2* max3, max1 * min1 * min2)
