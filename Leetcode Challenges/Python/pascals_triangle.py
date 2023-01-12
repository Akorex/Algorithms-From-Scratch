"""
Solution to Leetcode problem #118 - Pascal's Triangle

https://leetcode.com/problems/pascals-triangle/

"""
class Solution:
    def generate(self, numRows):
        results = [[1], [1, 1]] # row 0 and row 1

        # start filling from row 2
        for i in range(2, numRows):
            row = [1]

            for j in range(1, len(results[i - 1])): # needs to generate this amount of numbers
                ans = results[i - 1][j] + results[i - 1][j - 1]
                row.append(ans)
                row.append(1)

                results.append(row)
        return results[::numRows]