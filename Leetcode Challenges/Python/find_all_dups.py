"""
Solution to Leetcode problem #442 - Find all the duplicates in an array
useful link https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

"""
from typing import List

# trivial solution. solves in O(nlogn)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # trivial soln
        ans = []
        nums = sorted(nums)
        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                ans.append(nums[i-1])
        return ans

# hash map  method
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return ans

# hashmap written in another way
class Solution:
    def findDuplicates(self, nums:List[int]) -> List[int]:
        ans = []

        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                ans.append(num)
            else:
                nums[num - 1] *= -1
        return ans


# not recommended O(n*n) solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans.append(nums[i])