"""SOlution to Leetcode problem #304 - Range Sum Query 2D

https://leetcode.com/problems/range-sum-query-2d-immutable/
"""
class NumMatrix: # not working
    def __init__(self, matrix):
        if not matrix:
            return
        rows, cols = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                self.sum[i + 1][j + 1] = self.sum[i + 1][j] + self.sum[i][j+1] + matrix[i][j] - self.sum[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sum[row2+1][col2 + 1] + self.sum[row1][col2+ 1] - self.sum[row2+1][col1] + self.sum[row1][col1]