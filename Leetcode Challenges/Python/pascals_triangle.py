"""
Solution to Leetcode problem #118 - Pascal's Triangle

https://leetcode.com/problems/pascals-triangle/description/

"""

from typing import List




class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        if numRows == 0:
            return ans
        ans.append([1])

        for i in range(1, numRows):
            current = [1]
            prev = ans[i - 1]

            for j in range(1, len(prev)):
                current.append(prev[j-1] + prev[j])
            current.append(1)
            ans.append(current)

        return ans