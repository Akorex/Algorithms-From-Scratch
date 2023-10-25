"""
Solution to Leetcode problem #347 - Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
"""
import collections
from typing import List


# initial approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        temp = [] # stores values
        ans = []

        for key, value in count.items():
            temp.append(value)
        
        temp.sort()
        temp = temp[::-1]

        for i in temp:
            for j in count:
                if count[j] == i and j not in ans:
                    ans.append(j)
        return ans[:k]
    
# improved approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        temp = [] # stores values
        ans = []

        for key, value in count.items():
            temp.append(value)

        for i in range(k):
            max_freq = 0
            max_freq_num = 0

            for key, value in count.items():
                if value > max_freq:
                    max_freq = value
                    max_freq_num = key
            ans.append(max_freq_num)
            count.pop(max_freq_num)
        return ans