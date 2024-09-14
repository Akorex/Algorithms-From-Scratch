
"""
Solution to Leetcode problem #2239 - Find Closest Number to Zero

https://leetcode.com/problems/find-closest-number-to-zero/

"""

from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distances = [abs(x) for x in nums]
        min_distance = min(distances)
        idx_min_distance = [i for i, dst in enumerate(distances) if dst == min_distance]

        ans = nums[idx_min_distance[0]]

        for idx in idx_min_distance:
            if nums[idx] > ans:
                ans = nums[idx]
        return ans