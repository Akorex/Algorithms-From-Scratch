"""
Solution to Leetcode problem #4 - Median of two sorted arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge and sort the arrays
        merged = nums1 + nums2
        merged.sort()

        length = len(merged)
        if length % 2 != 0:
            idx = int(((length + 1)/2 ) - 1)
            return float(merged[idx])

        else:
            res = int(length/2)
            x, y = merged[res], merged[res - 1]
            return float((x + y)/2)