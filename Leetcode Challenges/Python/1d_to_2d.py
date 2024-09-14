"""
Solution to Leetcode problem #2022 - Convert 1D array to 2D array

https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

"""
from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if m * n != len(original):
            return ans

        for i in range(0, len(original), n):
            temp = original[i:i+n]
            ans.append(temp)
        return ans
