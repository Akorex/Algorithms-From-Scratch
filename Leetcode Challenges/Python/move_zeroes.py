"""
Solution to Leetcode problem #283 - Move Zeroes

https://leetcode.com/problems/move-zeroes/

"""
from typing import List
# initial attempt - doesn't work for all cases
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == 0:
                nums[i], nums[i + 1] = nums[i+1], nums[i]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0

        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1

        while idx < len(nums):
            nums[idx] = 0
            idx += 1



class Solutionn:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        
        for i in range(len(nums)):
            #print(i)
            #print(f"{nums} \n")
            if nums[i] != 0:
                nums[anchor], nums[i] = nums[i], nums[anchor]
                anchor += 1
        return nums
    


if __name__ == '__main__':
    l = [0, 1, 0, 3, 12]
    sol = Solutionn()
    print(sol.moveZeroes(l))