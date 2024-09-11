"""
Solution to Leetcode problem 448 - Find All Numbers Disappeared in an array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

"""
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        set_nums = set(nums)

        for i in range(1, len(nums)+1):
            if i not in set_nums:
                res.append(i)

        return res