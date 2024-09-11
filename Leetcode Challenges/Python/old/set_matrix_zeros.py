"""
Solution to Leetcode problem #73 - Set Matrix Zeroes

https://leetcode.com/problems/set-matrix-zeroes/description/

"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # get the number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        false_rows = [False] * rows
        false_cols = [False] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    false_rows[row] = True
                    false_cols[col] = True
        
        for row in range(rows):
            for col in range(cols):
                if false_rows[row] or false_cols[col]:
                    matrix[row][col] = 0