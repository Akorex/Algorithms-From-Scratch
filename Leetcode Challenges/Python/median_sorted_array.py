"""
Solution to Leetcode problem #4 - Median Sorted array

https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = nums1 + nums2
        merged.sort()

        length = len(merged)
        
        if length%2 == 0:
            temp = length//2
            x, y = merged[temp], merged[temp-1]
            return float((x + y)/2)
        else:
            temp = int((length + 1)/2 - 1)
            return float(merged[temp])
        

class Solution:
    def findMediamSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        length = len(merged)
        mid = length//2

        if length%2 == 0:
            x, y = merged[mid], merged[mid - 1]
            return float((x + y)/2)
        else:
            return float(merged[mid])