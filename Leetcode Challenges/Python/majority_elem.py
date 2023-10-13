"""
Solution to Leetcode challenge #169 - Majority Element
https://leetcode.com/problems/majority-element/

"""

from typing import List
import collections

# naive solution, exceeds timelist
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 # stores the max count
        ans = nums[0] # stores the element with highest count

        for num in nums:
            freq = nums.count(num)
            
            if freq > count:
                count = freq
                ans = num
        return ans
    
## approach 2 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = max(set(nums), key = nums.count)

        return ans


## aproach 3 - using collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        max_count = max(count.values())

        ans = list(count.keys())[list(count.values()).index(max_count)]
        return ans


if __name__ == '__main__':
    l = [1, 1, 1, 2, 3]

    print(l.count(1))