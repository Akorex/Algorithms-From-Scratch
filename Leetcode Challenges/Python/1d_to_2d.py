"""
Solution to Leetcode problem #2022 - Convert 1D array to 2D array

https://leetcode.com/problems/convert-1d-array-into-2d-array/description/
"""


from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # rejected case
        if len(original) != (m * n):
            return []

        ans = [[0] * n for _ in range(m)]

        for i in range(len(original)):
            row_index = i//n
            col_index = i % n

            ans[row_index][col_index] = original[i]
        return ans