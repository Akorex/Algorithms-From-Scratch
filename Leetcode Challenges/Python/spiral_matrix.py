"""
Solution to Leetcode problem #54 - Spiral Matrix

https://leetcode.com/problems/spiral-matrix/

Interesting soln - https://leetcode.com/problems/spiral-matrix/solutions/20571/1-liner-in-python-ruby/
"""

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []

        while matrix:
            spiral += matrix[0] # append the first row
            matrix.pop(0) # remove the appended row
            [row.reverse() for row in matrix] # reverse each row
            matrix = [list(y) for y in zip(*matrix)]
        return spiral


# soln from Leetcode link above
def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])