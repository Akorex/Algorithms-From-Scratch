"""
Solution to Leetcode problem #200 - Num Islands

https://leetcode.com/problems/number-of-islands/description/

"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            "mark every island using dfs"
            # base case
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            
            grid[r][c] = '0'  # mark as visited
            dfs(r + 1, c) # down
            dfs(r-1, c) # up
            dfs(r, c+1) # right
            dfs(r, c-1) # left
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c) # mark all 1s as visited
        return num_islands