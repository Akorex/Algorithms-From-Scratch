"""
Solution to Leetcode problem #867 - Transpose Matrix

https://leetcode.com/problems/transpose-matrix/description/
"""

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        ans = []

        for i in range(cols):
            row_x = []
            for j in range(rows):
                temp = matrix[j][i]
                row_x.append(temp)
            ans.append(row_x)

        return ans