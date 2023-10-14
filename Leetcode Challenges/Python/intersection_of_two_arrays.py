"""
Solution to Leetcode problem #349 - Intersection of two arrays.

https://leetcode.com/problems/intersection-of-two-arrays/description/
"""
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        ans = []

        for num in n2:
            if num in n1:
                ans.append(num)
        return ans