"""
Solution to Leetcode problem #74 - Search a 2D Matrix

https://leetcode.com/problems/search-a-2d-matrix/
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # find a likely location for target
        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = (left + right)//2

            if matrix[mid][-1] == target: # already found target
                return True
            elif matrix[mid][-1] < target: 
                left = mid + 1
            else:
                right = mid - 1

        if left >= len(matrix): #because it is out of bounds
            return False

        row = left # row is where target is.

        
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
        return False





