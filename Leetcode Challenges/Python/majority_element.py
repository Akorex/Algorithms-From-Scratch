"""
Solution to Leetcode challenge #169 - Majority Element
https://leetcode.com/problems/majority-element/

"""
from typing import List
import collections

# initial approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] = count.get(num) + 1
            else:
                count[num] = 1
        max_count = max(count.values())
        dic_index = list(count.keys())[list(count.values()).index(max_count)]
        return dic_index
    
# method 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        return max(count.keys(), key = count.get)
    

# initial approach rewritten
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        max_count = max(count.values())
        dic_index = list(count.keys())[list(count.values()).index(max_count)]
        return dic_index


# bruteforce approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = len(nums)//2

        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > max_count:
                return num


# randomization approach
import random

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate