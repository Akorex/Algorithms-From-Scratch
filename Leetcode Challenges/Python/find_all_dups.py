"""
Solution to Leetcode problem 442 - Find all duplicates in an array

https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

"""

from typing import List

# works but doesnt follow requirements -> O (nlogn)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                ans.append(nums[i])
        return ans
    
# works & follows requirements

class Solutionn:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for key, value in seen.items():
            if value == 2:
                ans.append(key)
        return ans
    
# works and follows requirements+
class Solutionnn:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            
            if nums[idx] < 0:
                ans.append(idx + 1)
            else:
                nums[idx] = -nums[idx]
        return ans

# another solution
class Solutionnnn:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        checker = set()
        ans = []

        for num in nums:
            if num in checker:
                ans.append(num)
            checker.add(num)
        return ans